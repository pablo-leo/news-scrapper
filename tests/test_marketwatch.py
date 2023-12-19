import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from datetime import date
from news_scrapper.marketwatch.news import MarketWatchNewsScrapper
from news_scrapper.marketwatch.urls import MarketWatchUrlsScrapper


main_url = 'https://www.marketwatch.com/'
sc = MarketWatchUrlsScrapper(main_url=main_url)
urls = sc.download_news_urls()

sc = MarketWatchNewsScrapper(urls=urls, verbose=True)
sc.download_htmls()
sc.extract_info()

folder_path = './news/marketwatch/'
if not os.path.exists(folder_path):
   os.makedirs(folder_path)
today = date.today().strftime('%Y-%m-%d')
filepath = os.path.join(folder_path, f'news_{today}.json')

sc.save_news(filepath)
sc.load_news(filepath)