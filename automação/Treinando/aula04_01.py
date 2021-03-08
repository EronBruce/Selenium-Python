from selenium import webdriver

navegador = webdriver.Chrome()

navegador.get('https://selenium.dunossauro.live/aula_04_a.html')

lista_n_ordenada = navegador.find_element_by_tag_name('ul')

lis = lista_n_ordenada.find_elements_by_tag_name('li')

lis[0].find_element_by_tag_name('a').text