import threading
import random

lock = threading.Lock()

def write_read_file():
    for _ in range(10):
        with open('test.txt', 'w+') as f:
            lock.acquire()
            nums = [str(random.randint(1, 10)) for _ in range(10)]
            f.write('\n'.join(nums))
            lock.release()
            f.seek(0)
            lock.acquire()
            sum = 0
            for line in f:
                sum += int(line)
            print(sum)
            lock.release()

def check_10_nums():
    for _ in range(10):
        with open('test.txt', 'r') as f:
            if len(f.readlines()) == 10:
                f.seek(0)
                lock.acquire()
                sum = 0
                for line in f:
                    sum += int(line)
                print(sum)
                lock.release()
            else:
                print("not 10 nums", len(f.readlines()))

t1 = threading.Thread(target=write_read_file)
t2 = threading.Thread(target=check_10_nums)

t1.start()
t2.start()

t1.join()
t2.join()
