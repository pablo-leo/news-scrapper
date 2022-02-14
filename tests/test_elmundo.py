from newspapers.elmundo.urls import ElMundoUrlsScrapper
from newspapers.elmundo.news import ElMundoNewsScrapper

main_url = 'https://www.elmundo.es/'
sc = ElMundoUrlsScrapper(main_url=main_url)
urls = sc.download_news_urls()

# urls = [
#     'https://www.elmundo.es/pais-vasco/2022/01/08/61d8a848e4d4d80a3a8b4592.html',
#     'https://www.elmundo.es/andalucia/2022/01/07/61d8860821efa0aa688b45b9.html'
# ]

sc = ElMundoNewsScrapper(urls=urls, verbose=True)
sc.download_htmls()
sc.extract_info()

filepath_test = '/newspapers/test_elmundo.json'
sc.save_news(filepath_test)
sc.load_news(filepath_test)