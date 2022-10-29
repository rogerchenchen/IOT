import network
import webrepl


class gpio:
    D0 = 16
    D1 = 5
    D2 = 4
    D3 = 0
    D4 = 2
    D5 = 14
    D6 = 12
    D7 = 13
    D8 = 15
    SDD3 = 10
    SDD2 = 9

class mcu_fun:

    def __init__(self):
        self.ip = None
        self.mqClient = None

    def connect_ap(self, ssid, pwd):
        #webrepl.stop()
        wlan = network.WLAN(network.STA_IF)     #　是STA是客戶端cliend　AP是伺服器端
        ap = network.WLAN(network.AP_IF)        #字形變全形的切回方式 左邊shift + 空白鍵
        wlan.active(True)
        ap.active(False)

        wlan.scan()
        wlan.connect(ssid, pwd)
        while not(wlan.isconnected()):
            pass

        #webrepl.start()
        print("Network Config:", wlan.ifconfig()) #ifconfig語法意思是 如果有連線 顯示它的名稱
        self.ip = wlan.ifconfig()[0]