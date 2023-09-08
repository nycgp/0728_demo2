import socket

c =socket.socket()
host=socket.gethostbyname(socket.gethostname())
port=1234
print(host,port)
c.connect((host,port))
while True:
	
	mess=input("你将要对服务器做什么？").encode()
	c.send(mess)
	print("客户端收到了{0}".format(c.recv(2048)))

c.close()