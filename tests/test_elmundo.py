from datetime import date
from newspapers.elmundo.urls import ElMundoUrlsScrapper
from newspapers.elmundo.news import ElMundoNewsScrapper


main_url = 'https://www.elmundo.es/'
sc = ElMundoUrlsScrapper(main_url=main_url)
urls = sc.download_news_urls()

sc = ElMundoNewsScrapper(urls=urls, verbose=True)
sc.download_htmls()
sc.extract_info()

today = date.today().strftime('%Y-%m-%d')
filepath_test = f'/home/pablo/Documents/news-scrapper/newspapers/elmundo/news_{today}.json'
sc.save_news(filepath_test)
sc.load_news(filepath_test)