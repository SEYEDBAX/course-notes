import multiprocessing
import time

seyed = None
def start_end(tm, step):
    time.sleep(tm)
    print("end", tm, " step: ", step)

def run():
    for i in range(5):
        p = multiprocessing.Process(target=start_end, args=(2, i))
        p.start()
        p.join()

    print(seyed)
    print('HI SEYED')


if __name__ == "__main__":
    run()