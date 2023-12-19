import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from datetime import date
from news_scrapper.elpais.news import ElPaisNewsScrapper
from news_scrapper.elpais.urls import ElPaisUrlsScrapper

main_url = 'https://elpais.com/'
sc = ElPaisUrlsScrapper(main_url=main_url)
urls = sc.download_news_urls()

sc = ElPaisNewsScrapper(urls=urls, verbose=True)
sc.download_htmls()
sc.extract_info()

folder_path = './news/elpais/'
if not os.path.exists(folder_path):
   os.makedirs(folder_path)
today = date.today().strftime('%Y-%m-%d')
filepath = os.path.join(folder_path, f'news_{today}.json')

sc.save_news(filepath)
sc.load_news(filepath)
