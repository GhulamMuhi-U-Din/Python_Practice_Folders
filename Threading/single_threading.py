# single threading

import threading

def task():
    print("Task Started")

t1 = threading.Thread(target=task)

t1.start()