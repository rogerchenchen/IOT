from time import sleep
from machine import ADC, Pin, PWM
from mcu_def import gpio

frequency = 1000
duty_cycle = 0
value = 0

RED = PWM(Pin(gpio.D5), freq=frequency, duty=value)
GREEN = PWM(Pin(gpio.D6), freq=frequency, duty=value)
BLUE = PWM(Pin(gpio.D7), freq=frequency, duty=value)

RED.duty(0)
GREEN.duty(0)
BLUE.duty(0)

adc = ADC(0)

while True:
    value = adc.read()
    print(f"value = {value}, {round(value * 100 /1024)}%") #前面加f代表使用 format {}內放入要顯示的變數 round語法是四捨五入
    
    if value < 400 :
        value = 0
        
    RED.duty(value)
    GREEN.duty(value)
    BLUE.duty(value)
   
