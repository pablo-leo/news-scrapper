from newspapers.marketwatch import MarketWatchScrapper

urls = [
    'https://www.marketwatch.com/story/why-new-years-chaos-may-signal-a-more-balanced-but-volatile-stock-market-in-2022-as-investors-grapple-with-a-hawkish-fed-11641653191?mod=home-page',
    'https://www.marketwatch.com/story/3-key-takeaways-from-the-supreme-court-showdown-over-the-vaccine-or-test-rule-for-businesses-11641591945?mod=home-page',
    'https://www.marketwatch.com/story/2022-could-be-the-year-of-financial-reckoning-bankruptcy-cases-fell-dramatically-in-2021-but-new-challenges-await-11641296556?mod=home-page'
]

sc = MarketWatchScrapper(urls=urls, verbose=True)
sc.download_htmls()
sc.extract_info()

filepath_test = '/home/pablo/Documents/news-scrapper/news/test_marketwatch.json'
sc.save_news(filepath_test)
sc.load_news(filepath_test)