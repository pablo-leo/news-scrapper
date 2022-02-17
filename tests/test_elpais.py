from newspapers.elpais.news import ElPaisNewsScrapper
from newspapers.elpais.urls import ElPaisUrlsScrapper


main_url = 'https://elpais.com/'
sc = ElPaisUrlsScrapper(main_url=main_url)
urls = sc.download_news_urls()

sc = ElPaisNewsScrapper(urls=urls, verbose=True)
sc.download_htmls()
sc.extract_info()

filepath_test = '/home/pablo/Documents/news-scrapper/newspapers/elpais/news.json'
sc.save_news(filepath_test)
sc.load_news(filepath_test)
