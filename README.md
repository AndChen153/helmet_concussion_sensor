# helmet_concussion_sensor
code for raspberry pi zero w and adxl 345 accelerometer

Enable i2c, ssh with raspi-config

sudo apt-get install python3-dev python3-pip python3-smbus i2c-tools -y

sudo i2cdetect -y 1 

sudo pip3 install adafruit-circuitpython-ADXL34x
