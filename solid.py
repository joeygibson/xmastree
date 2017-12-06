import time

from gpiozero import LEDBoard

tree = LEDBoard(*range(2, 28), pwm=True)
for led in tree:
    led.off()

for led in tree:
    led.value = 0.2

while True:
    time.sleep(60)
    pass
