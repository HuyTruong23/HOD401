import socket
import sys
import subprocess

subprocess.call('clear', shell=True)

# Enter ip
remoteSever = raw_input("Enter your ip: ")
remoteSeverIP = socket.gethostbyname(remoteSever)

# Display Ipv4
print "IPv4: ", remoteSeverIP

for port in range(1, 10000):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((remoteSeverIP, port))
    if result == 0:
        print "Port {}:   is Opened".format(port)
    sock.close