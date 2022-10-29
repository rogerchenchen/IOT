from machine import Pin
from mcu_def import gpio
from time import sleep

RED = Pin(gpio.D5, Pin.OUT) #Pin 語法拿來指定腳位 前者是指定的位置 後面是輸入或輸出
GREEN = Pin(gpio.D6, Pin.OUT)
BLUE = Pin(gpio.D7, Pin.OUT)

RED.value(0)
GREEN.value(0)
BLUE.value(0)

list1 = [RED, GREEN, BLUE]

for color in list1:
    for i in range(10):
        color.value(1)
        sleep(0.5)
        color.value(0)
        sleep(0.5)




