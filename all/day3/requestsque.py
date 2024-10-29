#!usr/bin/python3
import requests
import time, threading

url = "https://pastebin.com/raw/LKqWmsbk"
u = requests.get(url)
txt = u.text.split("\r\n")
head = {"User-Agent":"me-Rutuja"}

lst=[]

for j in txt:
    lst.append(j)
    #print(j)
#print(lst)


def urlfu(i):
    a = requests.get(i, headers = head, timeout = 10, allow_redirects=True)
    time.sleep(5)
    print("URL",i, a.status_code)

start = time.perf_counter()

t=0
for i in lst:
    t = threading.Thread(target=urlfu, args=[i])

    t.start()

end = time.perf_counter()

print('Execution Time: {}'.format(end-start))
print("All done")


#for i in txt:
#    try:
#        a = requests.get(i, headers = head, timeout = 10, allow_redirects=True)
#        print("URL",i, a.status_code)
#    except:
#        pass



