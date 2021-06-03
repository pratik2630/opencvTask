import socket
ip = '10.0.2.15'
port= input("Enter port:")
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((, port))
text = input("--->")
s.send(b"{}".format(text))
msg = s.recv(1024)
print(msg)
