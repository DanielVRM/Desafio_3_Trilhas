from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import time

def retorna_soup(html):
	return bs(html, 'lxml')

options = webdriver.ChromeOptions() 
options.add_argument('--disable-blink-features=AutomationControlled') 

driver = webdriver.Chrome(options=options)

driver.get('https://www.casasbahia.com.br/notebooks/b')
time.sleep(3)


for _ in range(10):
	driver.find_element_by_class_name('Button-sc-1o0ywp5-0').click()
	time.sleep(3)


html = driver.page_source
soup = retorna_soup(html)

produtos = soup.find_all('p', class_='ProductCard__Title-sc-2vuvzo-0 iBDOQj')
produtos = [x.text + '\n' for x in produtos]

precos = soup.find_all('span', class_='ProductPrice__PriceValue-sc-1tzw2we-6 kBYiGY')
precos = [x.text + '\n' for x in precos]

print(len(produtos))
print(len(precos))

produtos_txt = open('novos_produtos_n.txt', 'w')
precos_txt   = open('novos_precos_n.txt', 'w')

produtos_txt.writelines(produtos)
precos_txt.writelines(precos)

print('Deu certo')