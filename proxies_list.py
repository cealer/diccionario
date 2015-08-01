from bs4 import BeautifulSoup
from selenium import webdriver
lista=[]
driver = webdriver.Firefox()
driver.get('http://www.cool-proxy.net/proxies/http_proxy_list/sort:score/direction:desc')
html = driver.page_source
soup = BeautifulSoup(html)
for tag in soup.find_all('td'):
	lista.append(tag.text)
#cadena = 'document.write(Base64.decode(str_rot13("ZwRmYwRmAv43BF4kZwD=")))213.136.79.124'
#data = str(lista[0])
#print(data.lstrip(")))" ))
for x in range(len(lista)):
	if not lista[x].find("document")==-1:
		a=lista[x].find(')))')
		a=a+3
		print(lista[x][a:])