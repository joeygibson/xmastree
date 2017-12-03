import random

from gpiozero import LEDBoard


def pulse_numbers(starting_point):
    num = starting_point
    increasing = num < 100

    while True:
        if increasing:
            if num < 100:
                num += 1
            else:
                num -= 1
                increasing = False
        else:
            if num > 0:
                num -= 1
            else:
                num += 1
                increasing = True

        yield num / 100


tree = LEDBoard(*range(2, 28), pwm=True)

for led in tree:
    led.source_delay = 0.1
    led.source = pulse_numbers(random.randint(0, 100))

while True:
    pass
