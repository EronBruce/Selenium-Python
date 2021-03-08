from selenium import webdriver
from time import sleep 

driver = webdriver.Chrome()

driver.get("https://www.google.com.br/")

print(driver.current_url) # url padrão
print(driver.title) #titulo
print(driver.capabilities['browserVersion']) #versão do browser

element = driver.find_element_by_name("q")
element.click() 
element.send_keys("PyJamas Conf") #escreve no browser
element.submit() #pesquisa
sleep(3)

assert driver.title == "PyJamas Conf - Pesquisa Google"

driver.close()