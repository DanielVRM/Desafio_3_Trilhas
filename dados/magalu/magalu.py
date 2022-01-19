import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

def get_html(dados_request):
  if dados_request.status_code == 200:
    return bs(dados_request.content,'lxml')
  else:
    return f'{dados_request.status_code}, : erro'

headers = { 
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36', 
  'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 
  'Accept-Language' : 'en-US,en;q=0.5',
  'Accept-Encoding' : 'gzip', 
  'DNT' : '1',
  'Connection' : 'close'
}

lista_de_produtos = list()

def retorna_soup(pagina):
  url_busca = f'https://www.magazineluiza.com.br/busca/computadores/?page={pagina}'
  dados_request = requests.get(url_busca, headers=headers)
  soup = get_html(dados_request)
  return soup

def retorna_produtos(soup):
  produtos = [x.text for x in soup.find_all('h2', class_='sc-bHXGc hsFKpx')]
  precos = [x.text.split("\xa0")[1].replace('.','').replace(',','.') for x in soup.find_all('p', class_='sc-hKgJUU kegCEa sc-bxnjHY cTpdOW')]
  return zip(produtos, precos)

for pagina in range(25):
  soup = retorna_soup(pagina)
  produtos = retorna_produtos(soup)
  lista_de_produtos.extend(produtos)

df = pd.DataFrame(lista_de_produtos, columns=['Produto', 'Preco'])
df['Preco'] = df['Preco'].apply(lambda x: float(x))

filtro = df.query('Preco > 1200')
x = filtro.sample(800)
x.to_csv('magalu.csv')
