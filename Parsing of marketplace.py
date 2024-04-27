import requests
from bs4 import BeautifulSoup
from time import sleep

headers = {'User-Agent':'Mozilla/4.0 (Windows NT 11.0; Win32; x32)'}

def download(url):
        resp = requests.get(url, stream=True)
        r = open('D:\\Программы\\Изучение пайтона\\pythonProject\\.venv\\картинки\\' + url.split('/')[-1],'wb')
        for value in resp.iter_content(1024*1024):
                r.write(value)
        r.close()

def get_url():
    for count in range(1, 8):
            url = f"https://scrapingclub.com/exercise/list_basic/?page={count}"

            response = requests.get(url, headers=headers)

            soup = BeautifulSoup(response.text, 'lxml')

            data = soup.find_all('div', class_= 'w-full rounded border')

            for i in data:
                card_url = 'https://scrapingclub.com' + i.find('a').get('href')
                yield card_url
def array():
    for card_url in get_url():

            response = requests.get(card_url, headers=headers)
            sleep(1)
            soup = BeautifulSoup(response.text, 'lxml')

            data = soup.find('div', class_='my-8 w-full rounded border')
            name = data.find('h3', class_='card-title').text
            price = data.find('h4', class_='my-4 card-price').text
            text = data.find('p', class_='card-description').text
            url_img = 'https://scrapingclub.com' + data.find('img', class_='card-img-top').get('src')
            download(url_img)
            yield name, price, text, url_img
