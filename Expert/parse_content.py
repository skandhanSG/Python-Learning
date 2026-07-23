from bs4 import BeautifulSoup
import requests

url =input("enter the url: ")

response = requests.get(url)

parse = BeautifulSoup(response.content, 'html.parser')

if parse.title:
    print(parse.title.text.strip())
else:
    print("No title found.")