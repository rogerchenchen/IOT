from time import sleep
from machine import ADC, Pin
from mcu_def import gpio

RED = Pin(gpio.D5, Pin.OUT)
GREEN = Pin(gpio.D6, Pin.OUT)
BLUE = Pin(gpio.D7, Pin.OUT)

adc = ADC(0)
RED.value(0)
GREEN.value(0)
BLUE.value(0)

while True:
    value = adc.read()
    print(f"value = {value}, {round(value * 100 /1024)}%") #前面加f代表使用 format {}內放入要顯示的變數 round語法是四捨五入
    sleep(1)

    if value > 400:
        GREEN.value(1)
    else:
        GREEN.value(0)

