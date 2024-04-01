# OLED and Moodlighting for GeekPi absminitower case for raspberry pi 4.

The instructions from geekpi did not work for me, so I've re-created it as simple as I can make it.

Features:

 * OLED rotates from displaying system info and a digital clock.
 * LED ambient light according to CPU temperature.
 * Fan LEDs just a basic random color rotation.

## Install steps(starting in users home folder):
sudo raspi-config --> Interfaces --> Enable I2C
git clone https://github.com/WAShannon/rpi4tower.git

nano rpi4tower/rpi4tower_oled.py --> Line 84, font path, change <user> as required.  
nano rpi4tower/rpi4tower_oled.service --> Line 8 --> change <user> as required.  
nano rpi4tower/rpi4tower_leds.service --> Line 11 --> change <user> as required.  

sudo pip3 install --break-system-packages adafruit-blinka  
sudo pip3 install --break-system-packages adafruit-circuitpython-ssd1306  
sudo pip3 install --break-system-packages netifaces  
sudo pip3 install --break-system-packages adafruit-circuitpython-neopixel  
  
sudo cp -v ./rpi4tower/*.service /etc/systemd/system/  
  
sudo systemctl enable rpi4tower_oled.service  
sudo systemctl enable rpi4tower_leds.service  
  
reboot  



