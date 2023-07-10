"""Example of class extending the thread class
"""
from threading import Thread
import time


class SampleThread(Thread):
    def run(self) -> None:
        """Method that runs when the thread is started
        """
        print("Running the sample thread")
        time.sleep(2)
        print("Thread execution completed")


if __name__=="__main__":
    sample_thread = SampleThread()
    sample_thread.start()
    sample_thread.join()
