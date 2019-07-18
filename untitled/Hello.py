import socket
s = socket.socket()
host = socket.gethostname()
print(host)
port = 12345
s.bind((host,port))

s.listen(5)
while True:
    c,addr= s.accept()
    print("连接地址：",addr)
    str = "welcome to my world!"
    c.send(str.encode("utf-8"))
    c.close()