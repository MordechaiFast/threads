from concurrent.futures import ThreadPoolExecutor
from datetime import datetime
from queue import Queue
import threading
from time import sleep
from typing import Any

time = lambda: str(datetime.now().time())[6:12]

class Pipeline(Queue):
    def __init__(self, maxsize: int=10) -> None:
        super().__init__(maxsize)

    def set_message(self, message: Any):
        #print(f'{time()}: Setter to add to the queue')
        self.put(message)
        #print(f'{time()}: Setter added to the queue')

    def get_message(self) -> Any:
        #print(f'{time()}: --Getter to take from the queue')
        message = self.get()
        #print(f'{time()}: --Getter took from the queue')
        return message

def producer(pipeline: Pipeline, signal: threading.Event):
    number = 0
    while not signal.is_set():
        number += 1
        print(f'{time()}: Producing number {number}')
        pipeline.set_message(number)
    print(f'{time()}: Producer received exit signal')

def consumer(pipeline: Pipeline, signal: threading.Event):
    while not signal.is_set():
        number = pipeline.get_message()
        print(f'{time()}: --Consuming number {number}')
    print(f'{time()}: --Consumer received exit signal')
    while not pipeline.empty():
        number = pipeline.get_message()
        print(f'{time()}: --Consuming number {number}')

pipeline = Pipeline()
exit_signal = threading.Event()
with ThreadPoolExecutor() as executor:
    executor.submit(producer, pipeline, exit_signal)
    executor.submit(consumer, pipeline, exit_signal)
    sleep(.003)
    print(f'{time()}: -Exit request')
    exit_signal.set()