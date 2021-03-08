"" "
Crie um programa com selênio que
* Jogue o jogo
* Quando você ganhar o script deve parar de ser desenvolvido
"" "
from  selenium  import  webdriver
do  tempo  importar  dormir

#Google Chrome
options  =  webdriver . ChromeOptions ()
opções . add_experimental_option ( "excludeSwitches" , [ "enable-logging" ])
navegador  =  webdriver . Chrome ( options = options , executable_path = r'C: \ Program Files \ chromedriver_v88.0.4324.96 \ chromedriver.exe ' )
navegador . get ( "https://curso-python-selenium.netlify.app/exercicio_02.html" )

dormir ( 1,5 )

a  =  navegador . find_element_by_tag_name ( 'a' )
p  =  navegador . find_elements_by_tag_name ( 'p' )

numero_esperado  =  int (( p [ 1 ]. text ). split ( '' ) [ - 1 ])

enquanto  verdadeiro :
    a . clique ()
    p  =  navegador . find_elements_by_tag_name ( 'p' )
    se  p [ - 1 ]. text  ==  f "Você ganhou: { numero_esperado } " :
        intervalo