# multiple threading

import threading

def task1():
    print("Task 1")

def task2():
    print("Task 2")

t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)

t1.start()
t2.start()