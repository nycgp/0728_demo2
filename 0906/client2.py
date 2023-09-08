import socket
import sys

host=socket.gethostbyname(socket.gethostname())
port=1234

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
try:
	s.connect((host,port))
	print("连接服务端...   ip&port信息：",host,port)
except Exception as e:
	print("异常信息:",e)
	sys.exit()
while True:
	pass
	mess=input('you say:')
	s.sendall(mess.encode())
	data=s.recv(1024)
	data=data.decode()
	print("接受到的数据：",data)
	if mess.lower == "再见":
		break
s.close()



