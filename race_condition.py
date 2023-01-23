from concurrent.futures import ThreadPoolExecutor
import threading
import time


class UnDatabase:
    def __init__(self) -> None:
        self.value = 0
        self.lock = threading.Lock()
    
    def update(self, name):
        with self.lock:
            print(f'{name}: locked')
            value = self.value
            value += 1
            time.sleep(.1)
            self.value = value
        print(f'{name}: unlocked')

db = UnDatabase()
print(f'Testing update. Starting value is {db.value}')
with ThreadPoolExecutor() as executor:
    for index in range(1,3):
        executor.submit(db.update, f'Thread {index}')
print(f'Testing update. Final value is {db.value}')