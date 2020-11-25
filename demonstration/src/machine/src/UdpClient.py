from socket import *
import sys
import math
host = '192.168.1.45'
port = 9090
addr = (host,port)

udp_socket = socket(AF_INET, SOCK_DGRAM)

while(True):
    #data = str("g:"+str(input("x :")) + ":" + str(input("y:")) + ":" + "0:" + "1" + ":0#")
    # x = int(input("x:"))
    # y = int(input("y:"))
    # x_p=x-415
    # y_p=y+125
    # X = (x_p*math.cos(math.pi/4)+(y_p)*math.sin(math.pi/4))
    # Y = (x_p*math.sin(math.pi/4) + y_p*math.cos(math.pi*3/4))
    # fi = math.atan2(Y,X)
    # Y-=20*math.sin(fi)
    # X-=20*math.cos(fi)
    # data = str(("g:{}:{}:0:0:0#").format(X,Y))
    # print (X,Y)
    data=str(input())
    print (type(data))
    if not data : 
        udp_socket.close() 
        sys.exit(1)

    data = str.encode(data)
    udp_socket.sendto(data, addr)
    data = bytes.decode(data)
data = udp_socket.recvfrom(1024)
print(data)


udp_socket.close()
