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

    # In a real scenario, you would read the temperature from a sensor
    # adc = ADC(Pin(34))  # Example pin for temperature sensor
    # current_temp = adc.read()  # Read temperature value
    # Convert ADC value to temperature if necessary


    # Control heater using PWM
    # pwm = PWM(Pin(15))  # Example pin for heater control
    # if heater_state == "on":
    #     pwm.duty(512)  # Set duty cycle to 50%
    # else:
    #     pwm.duty(0)    # Turn off heater
    # Clean up PWM
    # pwm.deinit()
    # Note: The above PWM code is commented out as it requires actual hardware to run.

    # For demonstration purposes, we simulate a delay
    time.sleep(1)