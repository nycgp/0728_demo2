import socket


b=socket.gethostbyname(socket.gethostname())
print("b:%s" %(b))
print(type(b))

s=socket.socket()
host = b
port = 1234
s.bind((host,port))
s.listen(5)
print("***begin listen***")
while True:
	conn,addr= s.accept()
	print("***有客户端连接进来***")
	while True:
		try:
			data = conn.recv(1024)
		except Exception as e:
			print("异常信息：",e)
		if data:
			print("服务端收到数据，我再给你发一个包！")
			try:
				conn.send(data)
			except Exception as e2:
				print("异常信息e2:",e2)
		else:
			conn.close()
			break;

if __name__ == "__main__":
	pass