# multiprocessing

import multiprocessing

def task1():
    print("Process 1")

def task2():
    print("Process 2")

p1 = multiprocessing.Process(target=task1)

p2 = multiprocessing.Process(target=task2)

p1.start()

p2.start()

p1.join()

p2.join()

print("Finished")