from bs4 import BeautifulSoup
import requests
import time
import os
from tqdm import tqdm

url = 'https://read.yagami.me/series/tokyo_ghoul/'
urls = []

r = requests.get(url)
soup = BeautifulSoup(r.text, 'lxml')
item = soup.find('div', class_ = 'list')
for i in item.findAll('a'):
    urls.append(str(i.get('href')))

urls.reverse()
for i in range(1, len(urls), 2):
    d = urls[i][40:-1].split('/')
    if len(d)==3:
        g = d[1]+'.'+d[2]
        s = d[1]+'/'+d[2]
    else:
        g = s = d[1]
        
    if not os.path.isdir(f"E:\Programming\Скрапер\Glaves\{g} глава"):
        os.mkdir(f"E:\Programming\Скрапер\Glaves\{g} глава")
    
    r = requests.get(urls[i])
    soup1 = BeautifulSoup(r.text, 'lxml')
    proc = soup1.find('div', class_ = 'tbtitle dropdown_parent dropdown_right')
    for h in proc:
        pages_c = proc.find('div', class_ = 'text')
    for o in range(int(pages_c.text[:-2])):
        url = urls[i][:40] + d[0] + '/' + s + '/page/'+ str(o+1)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        item = soup.find('img', id='miku')
        k = str(item.get('src'))
        response = requests.get(k, stream=True)

        with open(f"E:\Programming\Скрапер\Glaves\{g} глава\{o+1}.png", "wb") as handle:
            for data in tqdm(response.iter_content()):
                handle.write(data)

    
