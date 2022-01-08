from bs4 import BeautifulSoup
import requests


class Scrapper:
    def __init__(self, urls, verbose=False):
        self.urls = urls
        self.verbose = verbose
        self.html_texts = {}
        self.news_info = {}

    def download_htmls(self):
        if self.verbose:
            print(f'-' * 50)
            print(f'Downloading HTMLs')
            print(f'-' * 50)

        n_urls = len(self.urls)
        for i, url in enumerate(self.urls):
            if self.verbose:
                print(f'Downloading {i+1}/{n_urls}: {url}')
            html_text = requests.get(url).text
            self.html_texts[url] = html_text

    def extract_info(self):
        if self.verbose:
            print(f'-' * 50)
            print(f'Extracting HTMLs information')
            print(f'-' * 50)

        n_urls = len(self.html_texts)
        for i, url in enumerate(self.html_texts):
            if self.verbose:
                print(f'Scrapping {i+1}/{n_urls}: {url}')
            html_text = self.html_texts[url]
            soup = BeautifulSoup(html_text, 'lxml')
            self.news_info[url] = {
                'title': self.extract_title(soup),
                'subtitle': self.extract_subtitle(soup),
                'date': self.extract_date(soup),
                'author': self.extract_author(soup),
                'body': self.extract_body(soup)
            }

    @staticmethod
    def extract_title(soup):
        pass

    @staticmethod
    def extract_subtitle(soup):
        pass

    @staticmethod
    def extract_author(soup):
        pass

    @staticmethod
    def extract_date(soup):
        pass

    @staticmethod
    def extract_body(soup):
        pass
