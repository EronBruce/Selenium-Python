from selenium import webdriver
from time import sleep

def find_by_text(browser, tag, text):
    """
    Encontrar o elemento com o texto 'text'.

    Argumentos:
        - browser = Instancia do browser [firefox, chrome, ...]
        - texto = conteúdo que deve estar na tag
        - tag = tag onde o texto será procurado
    """

    elementos = browser.find_elements_by_tag_name(tag) #lista

    for elemento in elementos:
        if elemento.text == text:
            return elemento

browser = webdriver.Chrome()

browser.get('https://selenium.dunossauro.live/aula_04_b.html')

#programa principal
nomes_das_caixas = ['um', 'dois', 'tres', 'quatro']

for nome in nomes_das_caixas:
    sleep(1)
    find_by_text(browser, 'div', nome).click()

for nome in nomes_das_caixas:
    sleep(1)
    browser.back()

for nome in nomes_das_caixas:
    sleep(1)
    browser.forward()


