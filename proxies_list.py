from bs4 import BeautifulSoup
from selenium import webdriver
driver = webdriver.Firefox()
driver.get('http://www.cool-proxy.net/proxies/http_proxy_list/sort:score/direction:desc')
html = driver.page_source
soup = BeautifulSoup(html)
for tag in soup.find_all('td'):
 	print (tag.text)