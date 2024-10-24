#!/usr/bin/python3
import time, threading

def func1(name1):
    print(f"Thread {name1}: running for next 5 secs")
    time.sleep(5)
    print(f"Thread {name1}: finishing")
    print("---------------------------")

def func2(name2):
    print(f"Thread {name2}: running for next 4 secs")
    time.sleep(4)
    print(f"Thread {name2}: finishing")
    print("---------------------------")

def func3(name3):
    print(f"Thread {name3}: running for next 3 secs")
    time.sleep(3)
    print(f"Thread {name3}: finishing")
    print("---------------------------")

start = time.perf_counter()

t1 = threading.Thread(target=func1, args=[1])
t2 = threading.Thread(target=func2, args=[2])
t3 = threading.Thread(target=func3, args=[3])

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

end = time.perf_counter()
print('Execution Time: {}'.format(end-start))
print("All done")
