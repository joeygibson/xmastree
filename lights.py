from gpiozero import LEDBoard
from gpiozero.tools import random_values
from signal import pause

tree = LEDBoard(*range(2, 28), pwm=True)
for led in tree:
    led.source_delay = 1.0
    led.source = random_values()
pause()
