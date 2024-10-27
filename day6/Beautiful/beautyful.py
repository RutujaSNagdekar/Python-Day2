from bs4 import BeautifulSoup as bb


with open("index.html","r") as f1:
    data=bb(f1,"html.parser")
print(type(data))

print(data.title) # Print <title> tage
print(data.title.string) # Print <title> STRING only without tag




