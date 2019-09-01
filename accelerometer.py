import time
import board
import busio
import os
import math
import adafruit_adxl34x
import subprocess

hostname = os.popen("hostname").read().strip()

print(hostname)

try:
    os.system("sudo rm /home/pi/"+hostname+"*.txt")
    print("removed")
except:
    print("not removed")
#print ("finished removing")


i2c = busio.I2C(board.SCL, board.SDA)
accel = adafruit_adxl34x.ADXL345(i2c)

#accel.setRange(adxl345.RANGE_16G)
#accelCompareList = [0,0,0]
#axes = ["x","y","z"]
accelValuesList = [0,0,0]
allAccelValues = []
timeStart = time.time()
time.sleep(1)
print ("start time")
filenum=0
writeBool=True


while True:
    '''values = "%f %f %f"%accel.acceleration
    accelValuesList=values.split()
    for i in range (0,3):
        accelValuesList[i]=float(accelValuesList[i])'''
    
    value="%f %f %f"%accel.acceleration
    allAccelValues.append(str(value)) 
    #time.sleep(0.005)
    time.sleep(0.01)
    #accelCompareList=accelValuesList
    currentTime = (time.time()-timeStart)
    #print (currentTime)
    
    
    if (int(currentTime)%60)==0 and len(allAccelValues)>500:
        writeBool=False
        print (int(currentTime))
                 
        with open(hostname + str(filenum) + '.txt' ,'w') as filehandle:
            for j in allAccelValues:
                filehandle.write('%s\n' % j)
                
        filenum=filenum+1
        allAccelValues.clear()
        print("wrote: "+str(filenum))
        #print (allAccelValues)
        
    elif (int(currentTime)%60)!=0 and writeBool==False:
        writeBool=True
    if (int(currentTime))>1200:
        break



for i in range(0,filenum+1):
    os.system("wc -l "+ hostname + str(i) + ".txt")

os.system("sudo poweroff")