"""Single Producer Singler consumer example
"""
from queue import Queue
import time
from threading import Thread
import random


def consumer(que: Queue) -> None:
    """Consumer to consume objects from queue
    """
    while True:
        item = que.get()
        if item is None:
            print("Exiting as sentinal value extracted from queue buffer")
            break
        time.sleep(item)
        print(f"Consumer got the following from que {item}")


def producer(que: Queue) -> None:
    """Method to produce values and put them on the
    shared buffer
    """
    for _ in range(10):
        item = random.randint(1, 3)
        time.sleep(item)
        print(f"Putting item {item} on queue")
        que.put(item)
    que.append(None)  # Sentinal signal

if __name__ == "__main__":
    queue = Queue()
    prod, con = Thread(target=producer, args=(queue,)), Thread(target=consumer, args=(queue,))
    prod.start()
    con.start()
    prod.join()
    con.join()
