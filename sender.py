import socket
import time
group = '224.1.1.1'
port = 5004
# 2-hop restriction in network
ttl = 2
sock = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM,
                     socket.IPPROTO_UDP)
sock.setsockopt(socket.IPPROTO_IP,
                socket.IP_MULTICAST_TTL,
                ttl)
while True:
    time.sleep(2)
    sock.sendto(b"Station 1", (group, port))