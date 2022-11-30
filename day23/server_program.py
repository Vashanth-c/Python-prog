import socket
host=socket.gethostname()
port=6000
s=socket.socket()
s.bind((host,port))
s.listen(5)

print('server listening')
while True:
    conn,addr=s.accept()
    print('now connection from{}',format(addr))
    with open ('hello.txt','r') as f:
        while True:
            l=f.read(1024)
            if not l:
                break
            conn.send(l.encode())
            print('send{}',format(l))
        print('finished sending')
        conn.close()
    print('connection closed')
