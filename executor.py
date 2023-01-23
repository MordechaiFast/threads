from concurrent.futures import ThreadPoolExecutor
import time

def thread_func(number):
    name = f'Thread {number}'
    print(f'{name}: starting')
    time.sleep(2)
    print(f'{name}: finishing')

print()
with ThreadPoolExecutor() as executor:
    executor.map(thread_func, range(1, 4))