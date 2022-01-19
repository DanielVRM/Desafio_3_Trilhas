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

options = webdriver.ChromeOptions() 
options.add_argument('--disable-blink-features=AutomationControlled') 

driver = webdriver.Chrome(options=options)

produtos_txt = open('novos_produtos.txt', 'w')
precos_txt = open('novos_precos.txt', 'w')

lista_produtos = list()
lista_precos = list()

for i in range(25):
	
	driver.get(f'https://submarino.com.br/busca/computadores?limit=24&offset={(600) + 24*i}')
	time.sleep(3)

	html = driver.page_source
	soup = retorna_soup(html)

	produtos = soup.find_all('h3', class_='src__Name-r60f4z-1 dBpyfL')
	produtos = [x.text + '\n' for x in produtos]

	precos = soup.find_all('span', class_='src__PromotionalPrice-r60f4z-6')
	precos = [x.text + '\n' for x in precos]

	lista_produtos.extend(produtos)
	lista_precos.extend(precos)

	try:
		print(produtos[0])
		print(precos[0])
	except:
		break

produtos_txt.writelines(lista_produtos)
precos_txt.writelines(lista_precos)
