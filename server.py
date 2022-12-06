import socket as s
server = s.socket()
server.bind(('localhost',62000))
print('waiting for connection')
server.listen(3)
while True:
    clint, add = server.accept()
    name = (clint.recv(1024).decode())
    clint.send(bytes("Thanks for connecting", 'utf-8'))
    print('secure Server connected with ', add)
    print('Name of clint :', name)
    while True:
        mes = input('Messege to clint/your turn :\n')
        clint.send(bytes(mes, 'utf-8'))
        mes2 = (clint.recv(1024).decode())
        print(mes2)

