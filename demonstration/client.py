import socket

UDP_IP = "192.168.1.46"
UDP_PORT = 9090
while(True):
    MESSAGE = input()


sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
