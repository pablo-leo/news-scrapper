from newspapers.elmundo.urls import ElMundoUrlsScrapper
from newspapers.elmundo.news import ElMundoNewsScrapper


main_url = 'https://www.elmundo.es/'
sc = ElMundoUrlsScrapper(main_url=main_url)
urls = sc.download_news_urls()

sc = ElMundoNewsScrapper(urls=urls, verbose=True)
sc.download_htmls()
sc.extract_info()

filepath_test = '/home/pablo/Documents/news-scrapper/newspapers/elmundo/news.json'
sc.save_news(filepath_test)
sc.load_news(filepath_test)