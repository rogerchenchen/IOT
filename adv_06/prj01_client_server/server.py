#自己電腦IP 127.0.0.1
import socket

HOST = 'localhost' #本機端IP 也等於127.0.0.1
PORT =  5438
s = socket.socket()
s.bind((HOST, PORT)) #bind原意為綁 之後執行s時都知道IP和PORT (類似註冊)
s.listen(5) #伺服器端最多可接受多少socket
print("server:{}, port:{}".format(HOST, PORT))
client, addr = s.accept() #伺服器端接收並回傳對象與IP位置資訊 accept()語法會回傳兩個變數 將會分別帶入前面兩個變數
print("client address:{}, port:{}".format(addr[0], addr[1])) #0項為IP, 1項為PORT

while True:
    msg = client.recv(100).decode("utf8") #接受客戶端訊息 100字元 
    print("Receive Message:" + msg)
    reply = "" #建立伺服器回應字串

    if msg == "Hi":
        reply = b"Hello!"
    elif msg == "Bye":
        client.send(b"quit")
        break
    else:
        reply = b"What???"

    client.send(reply) #回傳回應給客戶端

client.close() #關閉與客戶端溝通
s.close() #關閉伺服器
