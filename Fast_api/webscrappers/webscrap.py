import requests
from bs4 import BeautifulSoup

resopnse = requests.get('https://discord.com')
soup = BeautifulSoup(resopnse.text,'html.parser')
print(soup)