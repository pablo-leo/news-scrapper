from datetime import date
from newspapers.marketwatch.news import MarketWatchNewsScrapper
from newspapers.marketwatch.urls import MarketWatchUrlsScrapper


main_url = 'https://www.marketwatch.com/'
sc = MarketWatchUrlsScrapper(main_url=main_url)
urls = sc.download_news_urls()

sc = MarketWatchNewsScrapper(urls=urls, verbose=True)
sc.download_htmls()
sc.extract_info()

today = date.today().strftime('%Y-%m-%d')
filepath_test = f'/home/pablo/Documents/news-scrapper/newspapers/marketwatch/news_{today}.json'
sc.save_news(filepath_test)
sc.load_news(filepath_test)