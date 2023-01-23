from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
import threading
from typing import Any

def time(): return str(datetime.now().time())[6:12]

class Pipeline:
    def __init__(self) -> None:
        self.set_lock = threading.Lock()
        self.get_lock = threading.Lock()
        print(f'{time()}: -Initilizing get_lock')
        self.get_lock.acquire()

    def set_message(self, message: Any):
        print(f'{time()}: Setter to aquire set_lock')
        self.set_lock.acquire()
        print(f'{time()}: set_lock aquired')
        self.message = message
        print(f'{time()}: Releasing get_lock')
        self.get_lock.release()

    def get_message(self) -> Any:
        print(f'{time()}: --Getter to aquire get_lock')
        self.get_lock.acquire()
        print(f'{time()}: --get_lock aquired')
        message = self.message
        print(f'{time()}: --Releasing set_lock')
        self.set_lock.release()
        return message

def producer(pipeline: Pipeline):
    for number in range(10):
        print(f'{time()}: Producing number {number}')
        pipeline.set_message(number)
    print(f'{time()}: Producer exiting')
    pipeline.set_message(None)

def consumer(pipeline: Pipeline):
    while (number := pipeline.get_message()) is not None:
        print(f'{time()}: --Consuming number {number}')
    print(f'{time()}: Consumer exiting')

pipeline = Pipeline()
with ThreadPoolExecutor() as executor:
    executor.submit(producer, pipeline)
    executor.submit(consumer, pipeline)