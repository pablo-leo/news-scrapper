import json
import os.path
import requests
from bs4 import BeautifulSoup


class UrlsScrapper:
    def __init__(self, main_url, verbose=False):
        self.main_url = main_url
        self.verbose = verbose
        self.urls = None

    def download_news_urls(self):
        if self.verbose:
            print(f'-' * 50)
            print(f'Downloading main site')
            print(f'-' * 50)

        main_html = requests.get(self.main_url).text
        soup = BeautifulSoup(main_html, 'lxml')
        urls = self.extract_urls(soup)
        self.urls = self.filter_urls(urls, self.main_url)
        return self.urls

    def save_urls(self, filename):
        with open(filename, 'w') as fp:
            json.dump(self.urls, fp, indent=4)

    def load_urls(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as fp:
                self.urls = json.load(fp)
        elif self.verbose:
            print(f'-' * 50)
            print(f'{filename} doesn\'t exist!')
            print(f'Nothing loaded')
            print(f'-' * 50)

    @staticmethod
    def extract_urls(soup, n_urls):
        pass

    @staticmethod
    def filter_urls(urls, main_url):
        pass
