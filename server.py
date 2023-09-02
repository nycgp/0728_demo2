import socket

def server_program():

	# host =socket.gethostname()
	# print("***host***",host)
	host="192.168.1.14"
	port =12345

	# 创建socket 对象，参数：协议（TCP/IP），类型（SOCK_STREAM）,重用地址选项(0)
	s =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.bind((host,port))
	print("server %s %s already open" % (host,port))
	# 开始监听，等待客户端的连接
	# s.listen(5)
	conn,adress =s.accept()
	print("---Server Connection IP PORT---:%s %s" % (str(adress),port) )
	while True:
		# 接受客户端发来的信息
		data =conn.recv(1024)
		print("Receive data:%s" % str(data))
		# if not data:
		# 	break
		# 向客户端发送信息
		conn.send(b"PASS PASS PASS")
	# 关闭连接
	conn.close()
	print("*******conn close*******")

if __name__ == "__main__":
	server_program()








