import _thread
import random
import time

from gpiozero import LEDBoard


def pulse_light(the_led, starting_value):
    print("Starting: {}".format(the_led))
    while True:
        for i in range(starting_value, 100):
            the_led.value = i / 100
            time.sleep(0.1)

        starting_value = 0

        for i in range(100, 0, -1):
            the_led.value = i / 100
            time.sleep(0.1)


tree = LEDBoard(*range(2, 28), pwm=True)

for led in tree:
    try:
        _thread.start_new_thread(pulse_light, (led, random.randint(0, 99),))
    except Exception as e:
        print("Unable to start thread for {}: {}".format(led, e))

while 1:
    pass
