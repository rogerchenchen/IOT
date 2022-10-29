from esp8266_i2c_lcd import I2cLcd #import esp8266_i2c_lcd.py 的 I2cLcd class (城市可以找到檔案 因為在esp8266的函式庫都在同一個目錄)
from machine import I2C, Pin
from time import sleep

#設定LCD
i2c = I2C(scl = Pin(5), sda = Pin(4), freq = 400000) #指定 I2C 介面之 GPIO 與傳輸速率 
lcd = I2cLcd(i2c, 0x3F, 2, 16) #指定 I2C Slave 設定位置與顯示器之列數, 行數 最後一個參數代表一行可以放幾個字母 字母超過最多可放字母則移回第一行, 若最多可放字母超過顯示器可顯示字母數量 則不顯示

#設定LED
p2 = Pin(2, Pin.OUT)
#主程式
while 1:
    p2.value(0)
    lcd.putstr("LED ON") #顯示字串
    sleep(1)
    lcd.clear() #也可以改成 lcd.move_to(0, 0) 前面是行數 後面是列 LED OFF 最後的F會多出來 可用空白建替代
    p2.value(1)
    lcd.putstr("LED OFF")
    sleep(1)
    lcd.clear()








