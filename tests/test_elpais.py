from datetime import date
from newspapers.elpais.news import ElPaisNewsScrapper
from newspapers.elpais.urls import ElPaisUrlsScrapper

main_url = 'https://elpais.com/'
sc = ElPaisUrlsScrapper(main_url=main_url)
urls = sc.download_news_urls()

sc = ElPaisNewsScrapper(urls=urls, verbose=True)
sc.download_htmls()
sc.extract_info()

today = date.today().strftime('%Y-%m-%d')
filepath_test = f'/home/pablo/Documents/news-scrapper/newspapers/elpais/news_{today}.json'
sc.save_news(filepath_test)
sc.load_news(filepath_test)
