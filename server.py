#!/usr/bin/python3
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(("127.0.0.1", 1338))
print("Listening...")

s.listen(1)

client,addr = s.accept()

while True:
    cmd = input("# ").encode()
    client.send(cmd)
    if cmd ==b"exit":
        break
    rev = client.recv(1024).decode()
    print(rev)
client.close()
s.close()