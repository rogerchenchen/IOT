
import paho.mqtt.client as mqtt

#當地端城市連線伺服器得到回應, 要做的動作
def on_connect(client, userdata, flags, rc):
    print("Connected with result code" + str(rc))

    #將訂閱主題寫在on_connect上
    #如果我們失去連線或重新連線時
    #地端程式將會重新訂閱
    client.subscribe("Roger")

#當接收到從伺服器發送的訊息時要進行的動作
def on_message(client, userdata, msg):
    #轉換編碼utf-8才看得懂中文
    print(f"我訂閱的主題是:{msg.topic}, 收到訊息:{msg.payload.decode('utf-8')}")

#連線設定
#初始化地端程式
client = mqtt.Client()

#設定連線的動作
client. on_connect = on_connect

#設定接收訊息的動作
client.on_message = on_message

#設定登入帳號密碼
client.username_pw_set("singular", "1234")

#設定連線資訊(IP, )
client.connect("singularmakers.asuscomm.com", 1883, 60)

#開始連線，執行設定的動作和處理重新連結問題
#也可以手動使用其他loop函式來進行連接
client.loop_forever()