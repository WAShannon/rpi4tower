sudo raspi-config --> Interfaces --> Enable I2C
git clone https://github.com/WAShannon/rpi4tower.git

nano rpi4tower/rpi4tower_oled.py --> Line 84, font path, change <user> as required.
nano rpi4tower/rpi4tower_oled.service --> Line 8 --> change <user> as required.
nano rpi4tower/rpi4tower_leds.service --> Line 11 --> change <user> as required.

sudo pip3 install --break-system-packages adafruit-blinka
sudo pip3 install --break-system-packages adafruit-circuitpython-ssd1306
sudo pip3 install --break-system-packages netifaces
sudo pip3 install --break-system-packages adafruit-circuitpython-neopixel





