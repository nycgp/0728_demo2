import socket
import json
import os

path=os.path.dirname(os.path.realpath(__file__))
# print("源文件绝对路径",path)
"""
简单对话系统
socket 学习CSDN 网址：https://blog.csdn.net/xiaofengdada/article/details/122251915
	socket 实战小项目
	server 端监听
	client 端连接
-------------------------
json 学习  #参考学习网址：https://baijiahao.baidu.com/s?id=1770547052339004108&wfr=spider&for=pc
	1、dump在英文中有转储，转存的意思。dump函数用于将Python对象序列化为JSON，并将其写入文件对象中。它接受两个参数：要序列化的对象和目标文件对象。
	2、dumps是 dump string的缩写。dumps函数用于将Python对象序列化为JSON字符串。dumps函数不需要写入文件，而是将JSON表示的数据作为字符串返回。它接受一个参数：要序列化的对象。
	3、load函数用于从JSON文件中读取数据，并将其解析为Python对象。它接受一个参数：要读取的文件对象。
	4、loads就是 load string 的缩写。loads函数用于将JSON字符串解析为Python对象。它接受一个参数：要解析的JSON字符串。

"""

language = {'who are you':'I am chenchen','how are you':'21','where are you from':'ny'}
with open(path+os.sep+"language.json","w") as f:
	json.dump(language,f)
# print("python 对象序列化为JSON完成···")

json_string=json.dumps(language)
# print(json_string)

language2_str='{"name":"chensan","age":"27","city":"shanghai"}'
with open(path+os.sep+"language2.json","r") as f2:
	data=json.load(f2)
	print("从JSON文件中解析数据：",data)
	print(type(data))
	data.get


data2=json.loads(language2_str)
# print("打印data2信息：",data2)

host=socket.gethostbyname(socket.gethostname())
port=1234

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(5)
print("开始监听IP&port:",host,port)
conn,addr=s.accept()
print("连接的地址和端口：",addr)
while True:
	data=conn.recv(1024)
	data=data.decode()
	if not data:
		break
	print("接受的数据：",data)
	conn.sendall(language.get(data,"Nothing this is default!").encode())
conn.close()
s.close()



