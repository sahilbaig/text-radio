import socket
import struct
import threading 
import time


chanel_list=[]


for i in range(5004,5006):
    MCAST_PORT = i 
    MCAST_GRP = '224.1.1.1'
    sock_1 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
    sock_1.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock_1.bind(('', MCAST_PORT))
    mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)
    sock_1.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
    chanel_list.append(sock_1)

from threading import Timer
i=chanel_list[0]
global_variable=0

def task1():
    a=input()
    global global_variable
    global_variable=a
def task2():
    print(chanel_list[int(global_variable)].recv(10240))


print("You are listening to SomeMulticast Radio")
print("To change channels input selection")
print("0 : Channel 0 -> Prints  Channel 1")
print("1 : Channel 1 -> Prints  Channel 2")
while True:
    time.sleep(2)
    t1 = threading.Thread(target=task1, name='t1')
    t2 = threading.Thread(target=task2, name='t2')  
  
    # starting threads
    t1.start()
    t2.start()
    t2.join()

    


    
    # print(sock.recv(10240))
    
        