import time

def students(name:str) -> None:
    print(f"{name} is so cool, please wait for 2 seconds")
    time.sleep(5)
    print("Thanks for waiting")

if __name__=='__main__':
    students("CDAC")
