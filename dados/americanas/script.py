precos = open('precos_sem_c.txt', 'r').readlines()

novos_precos = [x.replace('.',"").replace(',','.').strip() for x in precos]

for preco in novos_precos:
	print(preco)
