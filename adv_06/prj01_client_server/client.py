#可以在終端機打clear 把終端機清乾淨
import socket

s = socket.socket()
s.connect(('127.0.0.1', 5438)) # 連結到伺服器

while True:
    msg = input("Input Message:")
    s.send(msg.encode("utf8"))
    reply = s.recv(128).decode("utf8")
    if reply == "quit":
        print("Disconected")
        s.close()
        break
    print(reply)