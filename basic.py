from threading import Thread
import time

def thread_func():
    name =thread.name
    print(f'{name}: starting')
    time.sleep(2)
    print(f'{name}: finishing')

print()
thread = Thread(name='Thread 1', target=thread_func)
print(f'Main    : before running {thread.name}')
thread.start()
print(f'Main    : waiting for {thread.name} to fininsh')
#thread.join()
print('Main    : finishing')