import time
first=time.time()

while True:
    final = time.time() - first
    final = str(round(final, 2))
    print(final)
    time.sleep(0.01)
