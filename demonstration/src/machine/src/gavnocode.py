#!/usr/bin/env python

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
server_address = ('192.168.1.54', port)
sock.bind(server_address)
c1 = 1;c2 = 1;t = 1;g = 1;p = 1;d = 1   #1/0 - working or not working

c1_adress = ('192.168.1.64', port)#Clients adresses IP
c2_adress = ('192.168.1.47', port)
t_adress = ('192.168.1.45', port)
g_adress = ('192.168.1.46', port)
p_adress = ("192.168.1.59", port)
d_adress = ('192.168.1.57', port)

def GetUDPdata(sock, delay):
    while True:
        global c1,c2,t,g,p,d
        data, _ = sock.recvfrom(512)
        data = data.decode()
        data_pars = data.split(":")

        
        data_pars = data.split(":")
        if data_pars[0] == "c1":
            c1 = int(data_pars[1])
        if data_pars[0] == "c2":
            c2 = int(data_pars[1])
        if data_pars[0] =="t":
            t = int(data_pars[1])
        if (data_pars[0]=="g"):
            g = int(data_pars[1])
        if data_pars[0] == "p":
            p = int(data_pars[1])
        if data_pars[0] == "d":
            d = int(data_pars[1])
        rospy.sleep(delay)

class BallOnTheTBPos1(smach.State):
    
    def __init__(self):
        
        smach.State.__init__(self,outcomes=['carry the ball', 'break', 'finish'])
        self.command = "t:0#".encode()   #Command for Tb3

    def Tb3Pos1(self):
        global t, sock, t_adress
        sent = sock.sendto(self.command,t_adress)
        rospy.sleep(0.2)
        while t!=0:
            rospy.sleep(0.2)
        return 'carry the ball'

    def execute(self,userdata):
        rospy.loginfo('carrying the ball to position 2')
        return self.Tb3Pos1()
        if 1==2:
            return 'break'
        if 1==2:
            return 'finish'

class BallOnTheTBPos2(smach.State):
    
    
    def getpositionAngle(self, x,y):
        x_p=x-350
        y_p=y+125
        X = (x_p*math.cos(math.pi/4)+(y_p)*math.sin(math.pi/4))
        Y = (x_p*math.sin(math.pi/4) + y_p*math.cos(math.pi*3/4))
        fi = math.atan2(Y,X)
        Y-=30*math.sin(fi)
        X-=30*math.cos(fi)

        X+=15
        print(X,Y,"manipulator")
        return X,Y

    def __init__(self):
        smach.State.__init__(self,outcomes=['take the ball', 'break','finish'])
    
        self.command5="g:-190:-230:0:1:1#".encode()
        self.command6="g:-190:-230:0:0:0#".encode()#command for angle manipulator
        self.command7="g:-190:-230:0:1:0#".encode()
        
    
    
    def AngleManipulator(self):
        self.camera_data = rospy.wait_for_message("/markers", MarkerArray)
        while((self.camera_data.header.frame_id != "camera2") or (self.camera_data.markers[0].pose.pose.position.y <0.15) or (self.camera_data.markers[0].pose.pose.position.x < 0.1 )):
            self.camera_data = rospy.wait_for_message("/markers", MarkerArray)
        y = 1000*(self.camera_data.markers[0].pose.pose.position.y)
        x = 1000*(self.camera_data.markers[0].pose.pose.position.x)
        print(x,y,"camera")
        x,y = self.getpositionAngle(x,y)
        
        self.command1="g:{}:{}:0:1:0#".format(x,y).encode()##command for angle manipulator
        self.command2="g:{}:{}:0:0:0#".format(x,y).encode()#command for angle manipulator
        self.command3="g:{}:{}:0:0:1#".format(x,y).encode()#command for angle manipulator
        self.command4="g:{}:{}:0:1:1#".format(x,y).encode()#command for angle manipulator
        global g,g_adress,sock
        sent = sock.sendto(self.command1,g_adress)
        rospy.sleep(0.2)
        while g!=0:
            rospy.sleep(0.2)
        sent = sock.sendto(self.command2,g_adress)
        rospy.sleep(0.2)
        while g!=0:
            rospy.sleep(0.2)
        sent = sock.sendto(self.command3,g_adress)
        rospy.sleep(0.2)
        while g!=0:
            rospy.sleep(0.2)
        sent = sock.sendto(self.command4,g_adress)
        rospy.sleep(0.2)
        while g!=0:
            rospy.sleep(0.2)
        sent = sock.sendto(self.command5,g_adress)
        rospy.sleep(0.2)
        while g!=0:
            rospy.sleep(0.2)
        sent = sock.sendto(self.command6,g_adress)
        rospy.sleep(0.2)
        while g!=0:
            rospy.sleep(0.2)
        sent = sock.sendto(self.command7,g_adress)
        rospy.sleep(0.2)
        while g!=0:
            rospy.sleep(0.2)
        return 'take the ball'

    def execute(self,userdata):
        rospy.loginfo('taking the ball and putting it on the line')
        return self.AngleManipulator()
        if 1==2:
            return 'break'
        if 1==2:
            return 'finish'

class BallOnTheLine1(smach.State):
    
    def __init__(self):
        smach.State.__init__(self,outcomes=['move the ball to delta', 'break', 'finish'])
        self.command_c1="c:0:0.4:1#".encode()#COmmand for conveyor to pos2
        self.command_g1="g:150:-150:0:1:0#".encode()#Command for angle manip up
        #self.command_g2="g:150:-150:0:1:0#".encode()#Command for angle manip return to base pose
        self.command_t="t:1#".encode()# Command for tb3 return to pos1
    
    def Conveyor(self):
        global c1, c1_adress, g_adress, t_adress,sock
        sent = sock.sendto(self.command_t,t_adress)
        sent = sock.sendto(self.command_c1,c1_adress)
        sent = sock.sendto(self.command_g1,g_adress)
        rospy.sleep(0.2)
        while g!=0 or c1!=0:
            rospy.sleep(0.2)
        return 'move the ball to delta'
        

    def execute(self,userdata):
        rospy.loginfo('moving the ball to delta')
        return self.Conveyor()
        if 1==2:
            return 'break'
        if 1==2:
            return 'finish'



class DeltaGrabBall(smach.State):
    
    def __init__(self):
        smach.State.__init__(self,outcomes=['grab the ball', 'break', 'finish'])
        
        
        self.command5="d:-140:0:1:1#".encode()#command for delta manipulator
        self.command6="d:-140:0:0:0#".encode()
        self.command7="d:-140:0:1:0#".encode()
        #command for delta manipulator

    def getpositionDelta(self,x,y):
        x+=140
        y-=15
        return x,y
    def DeltaGrab(self):
        self.camera_data = rospy.wait_for_message("/markers", MarkerArray)
        while(self.camera_data.header.frame_id != "camera1"):
            self.camera_data = rospy.wait_for_message("/markers", MarkerArray)
        x = -1000*(self.camera_data.markers[0].pose.pose.position.y)
        y = -1000*(self.camera_data.markers[0].pose.pose.position.x)
        x,y = self.getpositionDelta(x,y)
        self.command1="d:{}:{}:1:0#".format(x,y).encode()#command for delta manipulator
        self.command2="d:{}:{}:1:1#".format(x,y).encode()#command for delta manipulator
        self.command3="d:{}:{}:0:1#".format(x,y).encode()#command for delta manipulator
        self.command4="d:{}:{}:1:1#".format(x,y).encode()
        global d,d_adress,sock
        sent = sock.sendto(self.command1,d_adress)
        rospy.sleep(0.2)
        while d!=0:
            rospy.sleep(0.2)
        sent = sock.sendto(self.command2,d_adress)
        rospy.sleep(0.2)
        while d!=0:
            rospy.sleep(0.2)
        sent = sock.sendto(self.command3,d_adress)
        rospy.sleep(0.2)
        while d!=0:
            rospy.sleep(0.2)
        sent = sock.sendto(self.command4,d_adress)
        rospy.sleep(0.2)
        while d!=0:
            rospy.sleep(0.2)
        sent = sock.sendto(self.command5,d_adress)
        rospy.sleep(0.2)
        while d!=0:
            rospy.sleep(0.2)
        sent = sock.sendto(self.command6,d_adress)
        rospy.sleep(0.2)
        while d!=0:
            rospy.sleep(0.2)
        sent = sock.sendto(self.command7,d_adress)
        rospy.sleep(0.2)
        while d!=0:
            rospy.sleep(0.2)
        return 'grab the ball'


    def execute(self,userdata):
        rospy.loginfo('take the ball by delta')
        return self.DeltaGrab()
        if 1==2:
            return 'break'
        if 1==2:
            return 'finish'



class BallOnTheLine2(smach.State):
    
    def __init__(self):
        smach.State.__init__(self,outcomes=['move the ball', 'break', 'finish'])
        self.command1="d:0:0:0:0#".encode()#command for delta manipulator to come back
        self.command2="d:0:0:0:0#".encode()#command for delta manipulator to come back
        self.command_c2 ="c:0:-0.5:-1#".encode()#command for conveyor2

    def Conveyor2(self):
        global c2, c2_adress, d, d_adress,sock
        sent = sock.sendto(self.command1,d_adress)
        rospy.sleep(0.2)
        while d!=0:
            rospy.sleep(0.2)
        sent = sock.sendto(self.command2,d_adress)
        sent = sock.sendto(self.command_c2,c2_adress)
        rospy.sleep(0.2)
        while c2!=0:
            rospy.sleep(0.2)
        return 'move the ball'
        


    def execute(self,userdata):
        rospy.loginfo('moving the ball')
        return self.Conveyor2()
        if 1==2:
            return 'break'
        if 1==2:
            return 'finish'


class ManipulatorGrabTheBall(smach.State):
    global c,b,g,p,d
    def __init__(self):
        smach.State.__init__(self,outcomes=['grab the ball by pallet', 'break', 'finish'])
        self.command6=str.encode('p:210:210:1:0#')
        self.command5=str.encode('p:210:210:0:0#')#command for Palletizier
        self.command4=str.encode('p:210:210:0:1#')
        self.command3=str.encode('p:210:210:1:1#')#command for Palletizier
        

    def getposition(self, x,y):
        x_p=x+435
        y_p=y+125 
        Y = int(x_p*math.sin(math.pi/4)+(y_p)*math.cos(math.pi/4))
        X = int(x_p*math.cos(math.pi*3/4) + y_p*math.sin(math.pi/4))
        fi = math.atan2(Y,X)
        Y-=20*math.sin(fi)
        X-=20*math.cos(fi)
        print(X,Y)
        return X,Y


    def Palletizer(self):
        self.camera_data = rospy.wait_for_message("/markers", MarkerArray)
        while(self.camera_data.header.frame_id != "camera2"):
            self.camera_data = rospy.wait_for_message("/markers", MarkerArray)
        self.x = 1000*(self.camera_data.markers[0].pose.pose.position.x)
        self.y = 1000*(self.camera_data.markers[0].pose.pose.position.y)
        X, Y = self.getposition(self.x,self.y)
        self.command2=str.encode(('p:{}:{}:1:1#').format(X,Y))#command for Palletizier
        self.command1=str.encode(('p:{}:{}:0:1#').format(X,Y))#command for Palletizier
        self.command0=str.encode(('p:{}:{}:1:0#').format(X,Y))#command for Palletizier
        global p,p_adress,sock
        sent = sock.sendto(self.command0,p_adress)
        rospy.sleep(0.2)
        while p!=0:
            rospy.sleep(0.2)
        sent = sock.sendto(self.command1,p_adress)
        rospy.sleep(0.2)
        while p!=0:
            rospy.sleep(0.2)
        sent = sock.sendto(self.command2,p_adress)
        rospy.sleep(0.2)
        while p!=0:
            rospy.sleep(0.2)
        sent = sock.sendto(self.command3,p_adress)
        rospy.sleep(0.2)
        while p!=0:
            rospy.sleep(0.2)
        sent = sock.sendto(self.command4,p_adress)
        rospy.sleep(0.2)
        while p!=0:
            rospy.sleep(0.2)
        sent = sock.sendto(self.command5,p_adress)
        rospy.sleep(0.2)
        while p!=0:
            rospy.sleep(0.2)
        sent = sock.sendto(self.command6,p_adress)
        rospy.sleep(0.2)
        while p!=0:
            rospy.sleep(0.2)    
            
        return 'grab the ball by pallet'



    def execute(self,userdata):
        rospy.loginfo('grab the ball by pallet')
        return self.Palletizer()
        if 1==2:
            return 'break'
        if 1==2:
            return 'finish'




def main():
    global sock
    rospy.init_node('smach_conveyor_state_machine')

    # Create a SMACH state machine
    sm = smach.StateMachine(outcomes=['ERROR', 'END'])
    
    thread.start_new_thread(GetUDPdata, (sock, 0.02 ))
    with sm:
        # Add states to the container
        smach.StateMachine.add('BALLONTHETBPOS1', BallOnTheTBPos1(), 
                               transitions={'carry the ball':'BALLONTHETBPOS2', 
                                            'break':'ERROR',
                                            'finish':'END'})


        smach.StateMachine.add('BALLONTHETBPOS2', BallOnTheTBPos2(), 
                               transitions={'take the ball':'BALLONTHELINE1',
                                            'break':'ERROR',
                                            'finish':'END'})


        smach.StateMachine.add('BALLONTHELINE1', BallOnTheLine1(), 
                               transitions={'move the ball to delta':'DELTAGRABBALL',
                                            'break':'ERROR', 
                                            'finish':'END'})


        smach.StateMachine.add('DELTAGRABBALL', DeltaGrabBall(), 
                               transitions={'grab the ball':'BALLONTHELINE2', 
                                            'break':'ERROR', 
                                            'finish':'END'})


        smach.StateMachine.add('BALLONTHELINE2', BallOnTheLine2(), 
                               transitions={'move the ball':'MANIPUATORGRABTHEBALL', 
                                            'break':'ERROR', 
                                            'finish':'END'})

  
        smach.StateMachine.add('MANIPUATORGRABTHEBALL', ManipulatorGrabTheBall(), 
                               transitions={'grab the ball by pallet':'BALLONTHETBPOS1', 
                                            'break':'ERROR', 
                                            'finish':'END'})

    sis = smach_ros.IntrospectionServer('server_name', sm, '/SM_ROOT')
    sis.start()
    
    # Execute the state machine
    outcome = sm.execute()

    # Wait for ctrl-c to stop the application
    rospy.spin()
    sis.stop()


if __name__ == '__main__':
    main()