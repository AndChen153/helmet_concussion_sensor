#!/usr/bin/env python
#from adxl345 import ADXL345
import adxl345
import time
import os
from math import floor
#adxl345 = ADXL345()
first=time.time()
entry=1 # to separate file names by number of events recorded
trial=0 # to monitor if the program is turned off during the run

c=floor(1.3)

run=True
while run == True:
    os.system ("ifconfig | grep 192.168 > /home/pi/adxl345-python/networkstatus")
    f=open('/home/pi/adxl345-python/networkstatus' , 'r')
    j=f.read()
    if j:
        run=False
        print (j)



accel = adxl345.ADXL345()

accel.setRange(adxl345.RANGE_16G)

#os.system ('scp /home/pi/adxl345-python/playernum_10_is_online pi@192.168.1.100:/home/pi/Downloads')

print ('online')
while True:
    #final = time.time() -first
    #final = str(round(final,2))
    axes = accel.getAxes(True)
    if axes['x']>7 or axes['y']>7 or axes['z']>7:
	final = time.time() -first
	final = str(round(final,2))
        a="FieldTest2\t2018-09-11\t" + str(axes['x']) +"\t" + str(axes['y']) +"\t" + str(axes['z']) +"\t" + final +"\t" + str(trial) + "\n"
        # data in order xG yG zG time trialNumber
        filenum=str(floor(entry))
        s = open('/home/pi/adxl345-python/playernum_10_data'+filenum, 'a')
        s.write(a)
        print (a)
        s.close()
        entry=entry+0.03
        trial=trial+1
        #os.system ('scp /home/pi/adxl345-python/playernum_10 pi@192.168.1.100:/home/pi/Downloads')



