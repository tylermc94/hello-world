from machine import Pin, ADC, PWM # we need to import ADC to use analog inputs
import time
from servo import Servo

# set up pin 26 as an analog input
pot = ADC(Pin(26)) 
pwm_pin = PWM(Pin(16))
button = Pin(15,Pin.IN, Pin.PULL_DOWN)
servo = Servo(28)

pwm_pin.freq(1000)
# constant to convert the 0 - 65535 range to 0 - 3.3 volts
conversion_factor = 100 / 65535
led_state = 0
last_button_state = 0
max_adc = 65535

max = 65535

while True:
    current_state = button.value()
    
    pot_voltage = pot.read_u16() * conversion_factor / 100
    PWM_value = int(pot_voltage * max)
    
    if current_state == 1 and last_button_state == 0:
        led_state = not led_state  # toggle LED on/off
        time.sleep(0.2)  # debounce delay

    last_button_state = current_state

    if led_state:
        pot_value = pot.read_u16()
        pwm_pin.duty_u16(pot_value)  # set brightness
        print("Brightness:", int(pot_value / 655.35), "%")
        
        angle = int((pot_value / max_adc) * 180)
        servo.write(angle)
    
    else:
        pwm_pin.duty_u16(0)  # turn off LED
        servo.write(0)

    time.sleep(0.05)