from bs4 import BeautifulSoup
import requests
import wget
import os


url = 'https://embracedata.inpe.br/imager/CP/2022/CP_2022_0303/'
# by month
exts = ['O6', 'O5']

data_dir = os.getcwd() + '/data/imager/'
os.makedirs(data_dir, exist_ok=True)

def listFD(url, ext=''):
  page = requests.get(url).text
  soup = BeautifulSoup(page, 'html.parser')
  return [url + node.get('href') for node in soup.find_all('a') if node.get('href').endswith(ext, 0, 2)]

for ext in exts:
  for file in listFD(url, ext):
    print(file)
    wget.download(file, data_dir)