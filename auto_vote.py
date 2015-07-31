from selenium import webdriver
proxy_list=["178.33.230.114","212.72.155.76"]
proxy_port=[3128,80]

for x in range(len(proxy_list)):
	profile=webdriver.FirefoxProfile()
	profile.set_preference("network.proxy.type", 1)
	profile.set_preference("network.proxy.http", proxy_list[x])
	profile.set_preference("network.proxy.http_port",proxy_port[x])
	profile.update_preferences()
	driver=webdriver.Firefox(firefox_profile=profile)
	driver.get("http://www.ferendum.com/es/PID20216PSD86783")
	driver.find_element_by_name("nombre_nuevo_votante").send_keys(str(x))
	driver.find_element_by_name("votos_array[]").click()
	driver.find_element_by_name("submit_votacion").click()
	driver.quit()