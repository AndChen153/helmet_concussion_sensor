#!/usr/bin/env python
from adxl345 import ADXL345
import time
import os
adxl345 = ADXL345()


run=True
while run == True:
    os.system ("ifconfig | grep 192.168 > /home/pi/adxl345-python/networkstatus")
    f=open('/home/pi/adxl345-python/networkstatus' , 'r')
    j=f.read()
    if j:
        run=False
	print (j)
'''
accel = adxl345.ADXL345()

accel.setRange(adxl345.RANGE_16G)
'''
os.system ('scp /home/pi/adxl345-python/playernum_10_is_online pi@192.168.1.100:/home/pi/Downloads')
print ('online')
while True:
	axes = adxl345.getAxes(True)
	if axes['x']>2 or axes['y']>2 or axes['z']>2:
		a="ADXL345 accelerometer sensor \n"+str(axes['x']) +" = xGs \n"+str(axes['y']) +" = yGs \n"+str(axes['z']) +" = zGs \n"
                s = open('/home/pi/adxl345-python/playernum_10', 'a')
                s.write(a)
                print (a)
                s.close()
		os.system ('scp /home/pi/adxl345-python/playernum_10 pi@192.168.1.100:/home/pi/Downloads')

