import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from datetime import date
from news_scrapper.elmundo.urls import ElMundoUrlsScrapper
from news_scrapper.elmundo.news import ElMundoNewsScrapper

main_url = 'https://www.elmundo.es/'
sc = ElMundoUrlsScrapper(main_url=main_url)
urls = sc.download_news_urls()

sc = ElMundoNewsScrapper(urls=urls, verbose=True)
sc.download_htmls()
sc.extract_info()

folder_path = './news/elmundo/'
if not os.path.exists(folder_path):
   os.makedirs(folder_path)
today = date.today().strftime('%Y-%m-%d')
filepath = os.path.join(folder_path, f'news_{today}.json')

sc.save_news(filepath)
sc.load_news(filepath)