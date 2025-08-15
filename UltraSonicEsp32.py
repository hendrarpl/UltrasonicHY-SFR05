from machine import Pin
import time

trigger_pin = Pin(18, Pin.OUT)  # Replace 15 with your actual TRIG pin
echo_pin = Pin(5, Pin.IN)    # Replace 14 with your actual ECHO pin
led = Pin(2, Pin.OUT)

def measure_distance():
    trigger_pin.value(0)
    time.sleep_us(2)
    trigger_pin.value(1)
    time.sleep_us(10)
    trigger_pin.value(0)

    pulse_start = time.ticks_us()
    while echo_pin.value() == 0:
        pulse_start = time.ticks_us()

    pulse_end = time.ticks_us()
    while echo_pin.value() == 1:
        pulse_end = time.ticks_us()

    pulse_duration = time.ticks_diff(pulse_end, pulse_start)
    distance_cm = (pulse_duration * 0.0343) / 2
    return distance_cm

while True:
    distance = measure_distance()
    print("Distance:", distance, "cm")
    if distance > 5:
        led.on()
    else:
        led.off()
    time.sleep(1)