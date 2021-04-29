import requests
from bs4 import BeautifulSoup

username = input("Trovo Account Username: ")

url = "http://www.trovo.live/" + username
try:
    connect = requests.get(url)
    soup = BeautifulSoup(connect.text, "html.parser")
    tags = soup.find(class_="tags").get_text().strip().split()
    title = soup.find(class_="title text-overflow").get_text().strip()
    category = soup.find(class_="link mr10").get_text().strip()
    name = soup.find(class_="streamer-name text-overflow").get_text().strip()
    live = soup.find(class_="status").get_text().strip()
except:
    print("Username is Invalid!")
    
try:
    adult = tags[0]
    language = tags[1]
    print("Name: " + name)
    print("Title: " + title)
    print("Category: " + category)
    print("Live: " + live)
    print("Lanugage: " + language)
    print("Adult: " + adult)
except:
    language = tags[0]
    print("Name: " + name)
    print("Title: " + title)
    print("Category: " + category)
    print("Live: " + live)
    print("Lanugage: " + language)