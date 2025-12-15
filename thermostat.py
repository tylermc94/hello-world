from machine import Pin, ADC, PWM # type: ignore
import time

#-----Variables-----
mode = "heat"
set_temp = 70
current_temp = 68
heater_state = "off"

for _ in range(10):
    # Simulate temperature change for testing
    if heater_state == "on":
        current_temp += 1
    else:
        current_temp -= 1

    if set_temp < current_temp and mode == "heat":
        print("Heating")
        heater_state = "on"

    if set_temp >= current_temp and mode == "heat":
        print("Heater Off")
        heater_state = "off"

    print(f"Current Temp: {current_temp}, Heater: {heater_state}")
    time.sleep(0.1)