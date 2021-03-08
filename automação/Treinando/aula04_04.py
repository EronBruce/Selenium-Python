from selenium import webdriver

from urllib.parse import urlparse 

browser = webdriver.Chrome()

browser.get('http://selenium.dunossauro.live/aula_04_b.html')

url_parseada = urlparse(browser.current_url) 