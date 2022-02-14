from urls_scrapper import UrlsScrapper


class ElMundoUrlsScrapper(UrlsScrapper):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @staticmethod
    def extract_urls(soup):
        urls = soup.find_all('a', class_='ue-c-cover-content__link-whole-content')
        urls = [url['href'] for url in urls]

        return urls

    @staticmethod
    def filter_urls(urls, main_url):
        # root filter
        urls = [url for url in urls if url.startswith(main_url)]

        return urls
