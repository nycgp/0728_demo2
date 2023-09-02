import socket
import time

def client_program():
	# host=socket.gethostname()
	host="192.168.1.14"
	port=12345

	s =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect((host,port))

	while True:

		# 向服务器发送信息
		s.send(b'Hello,world,bbbbbbbbbbbbbbbbb')
		print("***发送成功111111111***")
		time.sleep(2)

		# 接收服务器发来的信息
		# data =s.recv(1024)
		# print("Receive data:%s" %str(data))

	# 关闭连接
	s.close()

if __name__ =="__main__":
	client_program()