import threading
import socket as s
clint = s.socket()
clint.connect(('localhost',62000))
name = input('Enter your name sir :')
clint.send(bytes(name,'utf-8'))
greeting = (clint.recv(1024).decode())
print(greeting)
while True:
    msgg = (clint.recv(1024).decode())
    print(msgg)
    msg2 = input('Say something to server:/your turn \n')
    clint.send(bytes(msg2,'utf-8'))