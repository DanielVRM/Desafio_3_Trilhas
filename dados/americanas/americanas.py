from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import time

'''
2 - MAGALU
3 - SUBMARINO - BACKLOG
4 - AMERICANAS - DOING
5 - CASAS BAHIA
'''

def retorna_soup(html):
	return bs(html, 'lxml')

driver = webdriver.Chrome()
produtos_txt = open('produtos.txt', 'w')
precos_txt = open('precos.txt', 'w')

lista_produtos = list()
lista_precos = list()

for i in range(50):
	
	driver.get(f'https://americanas.com.br/busca/computadores?limit=24&offset={24*i}')
	time.sleep(3)

	html = driver.page_source
	soup = retorna_soup(html)

	produtos = soup.find_all('h3', class_='src__Name-sc-1k0ejj6-4 isrBEm')
	produtos = [x.text + '\n' for x in produtos]

	precos = soup.find_all('span', class_='src__PromotionalPrice-sc-1k0ejj6-8')
	precos = [x.text + '\n' for x in precos]

	lista_produtos.extend(produtos)
	lista_precos.extend(precos)

	print(produtos[0])
	print(precos[0])

produtos_txt.writelines(lista_produtos)
precos_txt.writelines(lista_precos)