from threading import Thread
import time

def thread_func(number):
    name = f'Thread {number}'
    print(f'{name}: starting')
    time.sleep(2)
    print(f'{name}: finishing')

print()
threads = list()
for index in range(1, 4):
    thread = Thread(name=f'Thread {index}', target=thread_func, args=(index,))
    threads.append(thread)
    print(f'Main    : before running {thread.name}')
    thread.start()
print()
for thread in threads:
    print(f'Main    : before joining {thread.name}')
    thread.join()
    print(f'Main    : {thread.name} is done')