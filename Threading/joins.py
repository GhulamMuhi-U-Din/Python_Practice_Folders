# join

import threading
import time

def task():

    print("Task Started")

    time.sleep(3)

    print("Task Finished")


t1 = threading.Thread(target=task)

t1.start()

# Without join(), the main program would continue immediately.

t1.join()

print("Program Ended")

# another example

import threading

def print_numbers():
    for i in range(1, 6):
        print(i)

t = threading.Thread(target=print_numbers)

t.start()

t.join()

print("Done")