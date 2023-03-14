import time
import random
import threading

lock = threading.Lock()

def sequential():
    for i in range(10):
        with open(f'test-seq-{i}.txt', 'a') as f:
            for _ in range(1000000):
                f.write(str(random.randint(1, 100)) + '\n')

def generate_file(i):
    with open(f'test-thread-{i}.txt', 'a') as f:
        for _ in range(1000000):
            lock.acquire()
            f.write(str(random.randint(1, 100)) + '\n')
            lock.release()

def threaded():
    threads = []
    for i in range(10):
        t = threading.Thread(target=generate_file, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

# compare time

start = time.time()
sequential()
end = time.time()
seq_time = end - start

start = time.time()
threaded()
end = time.time()
thread_time = end - start

# print difference

print(f'difference: {seq_time - thread_time} seconds')