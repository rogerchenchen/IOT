from esp8266_i2c_lcd import  I2cLcd
from machine import I2C, Pin
from mcu_def import gpio, mcu_fun
import network

wlan = mcu_fun()
wlan.connect_ap("SingularClass0", "Singular#1234")


i2c = I2C(scl = Pin(gpio.D1), sda = Pin(gpio.D2), freq = 400000) #指定 I2C 介面之 GPIO 與傳輸速率 
lcd = I2cLcd(i2c, 0x3F, 2, 16) # I2cLcd(設定位置,顯示器之列數, 行數) 最後一個參數代表一行可以放幾個字母 字母超過最多可放字母則移回第一行, 若最多可放字母超過顯示器可顯示字母數量 則不顯示
lcd.putstr("Network Config:") #顯示字串
lcd.move_to(0, 1) #移動游標至第二列第一行位置(跳行)
lcd.putstr(str(wlan.ip))
