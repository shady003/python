import socket as s
server = s.socket()
server.bind(('localhost', 63001))
print('Server Created')
server.listen(3)
while True:
    clint, address = server.accept()
    name =(clint.recv(1024).decode())
    print('clint connected')
    print("Name :", name)
    # clint.send(bytes('Hey its Saurabh server', 'utf-8'))
    while True:
        msg = (clint.recv(1024).decode())
        print(msg)
