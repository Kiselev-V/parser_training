from requests import Session
from bs4 import BeautifulSoup
from time import sleep

headers = {'User-Agent':'Mozilla/4.0 (Windows NT 11.0; Win32; x32)'}

work = Session()


work.get('https://quotes.toscrape.com/', headers=headers)

response = work.get('https://quotes.toscrape.com/login', headers=headers)

soup = BeautifulSoup(response.text, 'lxml')
token = soup.find('form').find('input').get('value')

data = {'csrf_token': token, 'username': "noname", "password": "password"}

result = work.post('https://quotes.toscrape.com/login', headers=headers, data=data, allow_redirects=True)





