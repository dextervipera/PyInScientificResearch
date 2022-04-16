#thread
import time
import concurrent.futures

start = time.perf_counter()

def do_sth(seconds=1):
    print(f'sleeping {seconds} seconds')
    time.sleep(seconds)
    print('Wake up!')
    return "finished"


with concurrent.futures.ThreadPoolExecutor() as executor:
    f1 = executor.submit(do_sth, 1.5)

print(f1.result())
finish = time.perf_counter()

print(f'finished in {round(finish-start,2)} seconds')