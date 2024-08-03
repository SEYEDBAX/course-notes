import time
import threading
import random

seyed = None
def start_end(tm, step):
    global seyed
    seyed = step
    time.sleep(tm)
    print("end", tm, " step: ", step)

th = []
for i in range(1000):
    t = threading.Thread(target=start_end, args=(2, i))
    t.start()
    th.append(t)

for t in th:
    t.join()

print(seyed)
print('HI SEYED')