import time
from signal import pause

from gpiozero import LEDBoard

tree = LEDBoard(*range(2, 28), pwm=True)
print('LEDs: {}'.format(tree))

for led in tree:
    print('{}: off'.format(led))
    led.off()

for led in tree:
    print('{}: on'.format(led))
    led.on()
    time.sleep(2)
    led.off()

pause()
