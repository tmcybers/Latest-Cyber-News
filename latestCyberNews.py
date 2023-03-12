import requests
from bs4 import BeautifulSoup

print("\n"+"\033[1;33;100m")
print("**************************************************************************************************************************")
print("*                                       ☭ Latest↘Cyber↘News ☭ | ☬ C0D3D ßÿ тм¢увєя ☬                                     *")
print("*                                                                                                                        *")
print("*                                                                                                                        *")
print("*                                                                                                                        *")
print("*                               ♛ Stay informed about the latest moves of cybercriminals ♛                               *")
print("*                                                                                                                        *")
print("*                            ☠ The best Sources of Spanish News on cybersecurity and hacking ☠                           *")
print("*                                                                                                                        *")
print("*                                                                                                                        *")
print("*                                                                                                                        *")
print("**************************************************************************************************************************")
print("\n"+"\033[1;33;33m")

urls = ['https://www.escudodigital.com/ciberseguridad',
        'https://noticiasseguridad.com/category/seguridad-informatica/',
        'https://www.europapress.es/temas/ciberseguridad/',
        'https://www.bleepingcomputer.com/',
        'https://cybersecuritynews.es/soluciones-seguridad/',
        'https://www.eleconomista.es/tags/ciberseguridad',
        'https://www.elespanol.com/temas/ciberseguridad/',
        'https://elcomercio.pe/noticias/ciberseguridad/',
        'https://revistabyte.es/ciberseguridad/',
        'https://www.xataka.com/tag/ciberseguridad']

for url in urls:
    print(f'Latest cybersecurity news from {url}:')
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    if url == 'https://www.bleepingcomputer.com/':
        articles = soup.find_all(
            'article', class_='news-listing news-listing-1')
    elif url == 'https://cybersecuritynews.es/soluciones-seguridad/':
        articles = soup.find_all('div', class_='blog-list-wrap')
    elif url == 'https://www.eleconomista.es/tags/ciberseguridad':
        articles = soup.find_all('article', class_='card')
    elif url == 'https://www.elespanol.com/temas/ciberseguridad/':
        articles = soup.find_all('div', class_='articulo-row')
    elif url == 'https://elcomercio.pe/noticias/ciberseguridad/':
        articles = soup.find_all('article', class_='news-item')
    elif url == 'https://revistabyte.es/ciberseguridad/':
        articles = soup.find_all('article', class_='post')
    elif url == 'https://www.xataka.com/tag/ciberseguridad':
        articles = soup.find_all('article')
    else:
        articles = soup.find_all('article')

    for article in articles:
        title_element = article.find('h2')
        if title_element:
            title = title_element.text.strip()
        else:
            title = 'No title found'
        link_element = article.find('a')
        if link_element:
            link = link_element['href']
        else:
            link = 'No link found'
        summary_element = article.find('p')
        if summary_element:
            summary = summary_element.text.strip()
        else:
            summary = 'No summary found'
        print(f'Title: {title}\nLink: {link}\nSummary: {summary}\n')
