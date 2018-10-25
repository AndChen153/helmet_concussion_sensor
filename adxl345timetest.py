import adxl345
import time

first=time.time()

accel = adxl345.ADXL345()

accel.setRange(adxl345.RANGE_16G)

while True:
    final = time.time() - first
    final = str(round(final,3))
    axes = accel.getAxes(True)
    a="ADXL345 accelerometer sensor \n" + str(axes['x']) +" = xGs \n" + str(axes['y']) +" = yGs \n" + str(axes['z']) +" = zGs \n" + final +"\n"
    print (a)
    s = open('/home/pi/adxl345-python/playernum10datatest', 'a')
    s.write(a)
    s.close()
