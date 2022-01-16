from newspapers.elmundo import ElMundoScrapper

urls = [
    'https://www.elmundo.es/pais-vasco/2022/01/08/61d8a848e4d4d80a3a8b4592.html',
    'https://www.elmundo.es/andalucia/2022/01/07/61d8860821efa0aa688b45b9.html'
]

sc = ElMundoScrapper(urls=urls, verbose=True)
sc.download_htmls()
sc.extract_info()

filepath_test = '/home/pablo/Documents/news-scrapper/news/test_elmundo.json'
sc.save_news(filepath_test)
sc.load_news(filepath_test)