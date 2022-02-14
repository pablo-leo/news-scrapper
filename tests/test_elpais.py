from newspapers.elpais.news import ElPaisNewsScrapper

urls = [
    'https://elpais.com/economia/2022-01-08/espana-pide-a-la-ue-blindar-la-inversion-de-los-recortes-de-deuda.html',
    'https://elpais.com/espana/catalunya/2022-01-08/contagiados-de-covid-tres-veces-un-caso-excepcional-que-cada-vez-lo-sera-menos.html',
    'https://elpais.com/sociedad/2022-01-08/los-expertos-cuestionan-la-utilidad-de-la-dosis-de-refuerzo-a-cuatro-semanas-de-la-infeccion-no-tiene-sentido.html',
    'https://elpais.com/economia/2022-01-18/microsoft-revoluciona-el-mercado-al-comprar-por-70000-millones-de-dolares-la-desarrolladora-de-videojuegos-activision.html'
]

sc = ElPaisNewsScrapper(urls=urls, verbose=True)
sc.download_htmls()
sc.extract_info()

filepath_test = '/newspapers/test_elpais.json'
sc.save_news(filepath_test)
sc.load_news(filepath_test)
