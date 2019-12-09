# xmastree

Code to drive this RPi Christmas Tree https://thepihut.com/products/3d-xmas-tree-for-raspberry-pi

## Setup for new Raspberry Pi Zero W

1. `sudo apt-get update && sudo apt-get install python3-pip`
2. `sudo pip3 install gpiozero rpi.gpio`

## Install as service

1. Copy `*.py` and `*.service` to `/home/pi`
2. Copy whichever `.service` file you want to `/etc/systemd/system`
3. Run `sudo systemctl daemon-reload`
4. Run `sudo systemctl enable lights` (or `solid`, depending on which you want)
5. Run `sudo systemctl start lights` to start it immediately.
