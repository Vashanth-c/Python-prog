import socket

HOST='localhost'
PORT=50008
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)
conn,addr=s.accept()
print('connected by',addr)
while True:
    data=conn.recv(1024)
    print(data)
    if not data:
        break
    conn.send('welcome'.encode())
conn.close()
