#!/usr/bin/env python3

import rospy
import smach
import _thread as thread
import socket
import sys
import smach_ros
import select
from aruco_msgs.msg import Marker, MarkerArray
import math

port = 9090
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('192.168.0.109', port)
sock.bind(server_address)
c1_state = 1;c2_state = 1;t_state = 1;g_state = 1;p_state = 1;d_state = 1   #1/0 - working or not working

c1_adress = ('192.168.0.105', port)#Clients adresses IP
c2_adress = ('192.168.0.106', port)
t_adress = ('192.168.0.110', port)
g_adress = ('192.168.0.102', port)
p_adress = ("192.168.0.101", port)
d_adress = ('192.168.0.103', port)

def GetUDPdata(sock, delay):
    while True:
        global c1_state,c2_state,t_state,g_state,p_state,d_state
        data, _ = sock.recvfrom(512)
        data = data.decode()
        data_pars = data.split(":")

        
        data_pars = data.split(":")
        if data_pars[0] == "c1":
            c1_state = int(data_pars[1])
        if data_pars[0] == "c2":
            c2_state = int(data_pars[1])
        if data_pars[0] =="t":
            t_state = int(data_pars[1])
        if (data_pars[0]=="g"):
            g_state = int(data_pars[1])
        if data_pars[0] == "p":
            p_state = int(data_pars[1])
        if data_pars[0] == "d":
            d_state = int(data_pars[1])
        rospy.sleep(delay)


def getArucoCoordinates(camera,max_x,max_y):
    rospy.sleep(1.0)
    camera_data = rospy.wait_for_message("/markers", MarkerArray)
    while((camera_data.header.frame_id != camera) or (camera_data.markers[0].pose.pose.position.y < max_y) or (camera_data.markers[0].pose.pose.position.x < max_x )):
        camera_data = rospy.wait_for_message("/markers", MarkerArray)
    y = 1000*(camera_data.markers[0].pose.pose.position.y)
    x = 1000*(camera_data.markers[0].pose.pose.position.x)
    return x,y


class BallOnTheTBPos1(smach.State):
    
    def __init__(self):
        
        smach.State.__init__(self,outcomes=['carry the ball', 'break'])
           #Command for Tb3

    def Tb3Pos1(self):
        global t_state, sock, t_adress
        sent = sock.sendto("t:0#".encode(),t_adress)
        t_state = 1
        rospy.sleep(0.2)
        while t_state != 0:
            rospy.sleep(0.2)
        t_state = 1
        return 'carry the ball'

    def execute(self,userdata):
        rospy.loginfo('carrying the ball to position 2')
        if 1 == 2:
            return 'break'
        else:
            return self.Tb3Pos1()
        
class BallOnTheTBPos2(smach.State):

    def __init__(self):
        smach.State.__init__(self,outcomes=['take the ball', 'break'])
    
    def getPositionAngle(self, x,y):
        x_p = x-350
        y_p = y+125
        x = (x_p*math.cos(math.pi/4)+(y_p)*math.sin(math.pi/4))
        y = (x_p*math.sin(math.pi/4) + y_p*math.cos(math.pi*3/4))
        fi = math.atan2(y,x)
        y -= 30*math.sin(fi)
        x -= 30*math.cos(fi)
        #x += 15
        return x,y
        
    
    
    def getCommandLineAngle(self,x,y):
        commandLine = []
        commandLine.append('g:{}:{}:0:1:0#'.format(x,y))
        commandLine.append('g:{}:{}:0:0:0#'.format(x,y))
        commandLine.append('g:{}:{}:0:0:1#'.format(x,y))
        commandLine.append('g:{}:{}:0:1:1#'.format(x,y))
        commandLine.append('g:-190:-230:0:1:1#')
        commandLine.append('g:-190:-230:0:0:0#')
        commandLine.append('g:-190:-230:0:1:1#')
        commandLine.append('g:-190:-230:0:1:0#')
        return commandLine



    def angleManipulator(self):
        global g_state,g_adress,sock
        x_c, y_c = getArucoCoordinates("camera2",-0.15,-0.1)
        x,y = self.getPositionAngle(x_c, y_c)
        commandLine = self.getCommandLineAngle(x,y)
        
        for i, command in enumerate(commandLine):
            if i == 1:
                rospy.sleep(2.0)
            sent = sock.sendto(command.encode(), g_adress)
            g_state = 1
            rospy.sleep(0.2)
            while g_state != 0:
                rospy.sleep(0.2)
        g_state = 1
        return 'take the ball'

    def execute(self,userdata):
        rospy.loginfo('taking the ball and putting it on the line')
        return self.angleManipulator()
        if 1 == 2:
            return 'break'
        

class BallOnTheLine1(smach.State):
    
    def __init__(self):
        smach.State.__init__(self,outcomes=['move the ball to delta', 'break'])
        
    
    def getCommandLineConveyor1(self):
        commandLine = []
        commandLine.append('c:0:0.4:1#')
        commandLine.append('g:150:-150:0:1:0#')
        commandLine.append('t:1#')
        return commandLine

    def Conveyor(self):
        global c1_state, c1_adress, g_adress, t_adress,sock
        commandLine=self.getCommandLineConveyor1()
        sent = sock.sendto(commandLine[2].encode(),t_adress)
        sent = sock.sendto(commandLine[0].encode(),c1_adress)
        sent = sock.sendto(commandLine[1].encode(),g_adress)
        c1_state = 1
        rospy.sleep(0.2)
        while c1_state != 0:
            rospy.sleep(0.2)
        c1_state = 1
        return 'move the ball to delta'
        

    def execute(self,userdata):
        rospy.loginfo('moving the ball to delta')
        return self.Conveyor()
        if 1 == 2:
            return 'break'
        



class DeltaGrabBall(smach.State):
    
    def __init__(self):
        smach.State.__init__(self,outcomes=['grab the ball', 'break'])
        

    def getpositionDelta(self,x,y):
        y_d = - x - 15
        x_d = - y + 155
        return x_d,y_d

    def getCommandLineDelta(self,x,y):
        commandLine = []
        commandLine.append('d:{}:{}:1:0#'.format(x,y))
        commandLine.append('d:{}:{}:1:1#'.format(x,y))
        commandLine.append('d:{}:{}:0:1#'.format(x,y))
        commandLine.append('d:{}:{}:1:1#'.format(x,y))
        commandLine.append('d:-140:0:1:1#')
        commandLine.append('d:-140:0:0:0#')
        commandLine.append('d:-140:0:1:0#')
        
        return commandLine

    def DeltaGrab(self):
        global d_state,d_adress,sock
        x_c, y_c = getArucoCoordinates("camera1",-10,-10)
        x,y = self.getpositionDelta(x_c, y_c)
        commandLine = self.getCommandLineDelta(x,y)
        for command in commandLine:
            sent = sock.sendto(command.encode(),d_adress)
            d_state = 1
            rospy.sleep(0.2)
            while d_state != 0:
                rospy.sleep(0.2)
        d_state = 1
        return 'grab the ball'


    def execute(self,userdata):
        rospy.loginfo('take the ball by delta')
        return self.DeltaGrab()
        if 1 == 2:
            return 'break'
        


class BallOnTheLine2(smach.State):
    
    def __init__(self):
        smach.State.__init__(self,outcomes=['move the ball', 'break'])

    def getCommandLineConveyor2(self):
        commandLine = []
        commandLine.append('d:0:0:0:0#')
        commandLine.append('c:0:-0.5:-1#')
        return commandLine


    def Conveyor2(self):
        global c2_state, c2_adress, d_state, d_adress,sock
        commandLine = self.getCommandLineConveyor2()
        sent = sock.sendto(commandLine[0].encode(),d_adress)
        sent = sock.sendto(commandLine[1].encode(),c2_adress)
        c2_state = 1
        rospy.sleep(0.2)
        while c2_state != 0:
            rospy.sleep(0.2)
        c2_state = 1
        return 'move the ball'
        


    def execute(self,userdata):
        rospy.loginfo('moving the ball')
        return self.Conveyor2()
        if 1==2:
            return 'break'


class ManipulatorGrabTheBall(smach.State):
    global c_state,t_state,g_state,p_state,d_state
    def __init__(self):
        smach.State.__init__(self,outcomes=['grab the ball by pallet', 'break'])
        

    def getpositionPallet(self, x,y):
        x_p=x+435
        y_p=y+125 
        Y = int(x_p*math.sin(math.pi/4)+(y_p)*math.cos(math.pi/4))
        X = int(x_p*math.cos(math.pi*3/4) + y_p*math.sin(math.pi/4))
        fi = math.atan2(Y,X)
        Y+=20*math.sin(fi)
        X+=20*math.cos(fi)
        print(X,Y)
        return X,Y

    def getCommandLinePallet(self,x,y):
        commandLine = []
        commandLine.append('p:{}:{}:1:0#'.format(x,y))
        commandLine.append('p:{}:{}:0:1#'.format(x,y))
        commandLine.append('p:{}:{}:1:1#'.format(x,y))
        commandLine.append('p:220:250:1:0#')
        commandLine.append('p:220:250:0:0#')
        commandLine.append('p:220:250:1:1#')
        return commandLine


    def Palletizer(self):
        global p_state,p_adress,sock
        x_c, y_c = getArucoCoordinates("camera2",-10,-10)
        x,y = self.getpositionPallet(x_c, y_c)
        commandLine = self.getCommandLinePallet(x,y)
        
        for command in commandLine:
            sent = sock.sendto(command.encode(),p_adress)
            p_state = 1
            rospy.sleep(0.2)
            while p_state!=0:
                rospy.sleep(0.2)
        p_state = 1
        return 'grab the ball by pallet'



    def execute(self,userdata):
        rospy.loginfo('grab the ball by pallet')
        return self.Palletizer()
        if 1==2:
            return 'break'
        
def main():
    global sock
    rospy.init_node('smach_conveyor_state_machine', disable_signals=True)

    # Create a SMACH state machine
    sm = smach.StateMachine(outcomes=['ERROR'])
    
    thread.start_new_thread(GetUDPdata, (sock, 0.05 ))
    with sm:
        # Add states to the container
        smach.StateMachine.add('BALLONTHETBPOS1', BallOnTheTBPos1(), 
                               transitions={'carry the ball':'BALLONTHETBPOS2', 
                                            'break':'ERROR',})


        smach.StateMachine.add('BALLONTHETBPOS2', BallOnTheTBPos2(), 
                               transitions={'take the ball':'BALLONTHELINE1',
                                            'break':'ERROR',})


        smach.StateMachine.add('BALLONTHELINE1', BallOnTheLine1(), 
                               transitions={'move the ball to delta':'DELTAGRABBALL',
                                            'break':'ERROR', })


        smach.StateMachine.add('DELTAGRABBALL', DeltaGrabBall(), 
                               transitions={'grab the ball':'BALLONTHELINE2', 
                                            'break':'ERROR', })


        smach.StateMachine.add('BALLONTHELINE2', BallOnTheLine2(), 
                               transitions={'move the ball':'MANIPUATORGRABTHEBALL', 
                                            'break':'ERROR', })

  
        smach.StateMachine.add('MANIPUATORGRABTHEBALL', ManipulatorGrabTheBall(), 
                               transitions={'grab the ball by pallet':'BALLONTHETBPOS1', 
                                            'break':'ERROR', })

    sis = smach_ros.IntrospectionServer('server_name', sm, '/SM_ROOT')
    sis.start()
    
    # Execute the state machine
    outcome = sm.execute()

    # Wait for ctrl-c to stop the application
    rospy.spin()
    sis.stop()


if __name__ == '__main__':
    main()
