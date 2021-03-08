from behave import given, when, then

@given(u'que acesso a página do Google')
def step_impl(context):
    context.web.get("https://www.google.com.br/")


@when(u'realizo uma pesquisa')
def step_impl(context):
    context.element = context.web.find_element_by_name("q")
    context.element.click() 
    context.element.send_keys("PyJamas Conf") #escreve no browser
    context.element.submit() #pesquisa


@when(u'pesquisa é realizada')
def step_impl(context):
    assert context.web.title == "PyJamas Conf - Pesquisa Google"


@then(u'o titulo da página deve ser validado')
def step_impl(context):
    pass 