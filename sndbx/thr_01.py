#thread
import time
import threading

start = time.perf_counter()

def do_sth(seconds=1):
    print(f'sleeping {seconds} seconds')
    time.sleep(seconds)
    print('Wake up!')

t1 = threading.Thread(target=do_sth)
t2 = threading.Thread(target=do_sth)

t1.start()
t2.start()

t1.join()   
t2.join()

threads = []

for _ in range(10):
    t=threading.Thread(target=do_sth, args=[1.5])
    t.start()
    threads.append(t)
    
for thread in threads:
    thread.join()

finish = time.perf_counter()

print(f'finished in {round(finish-start,2)} seconds')