from behave import given, when, then
from test.factories.user import UserFactory
from test.factories.especieDocumental import EspecieDocumentalFactory
from app.models import EspecieDocumental



#Scenario: Campos Vazios
@given('Eu sou um usuario logado')
def step_impl(context):
    #Cria um usuário de teste
    criarNovoUsuario()

    br = context.browser
    br.get(context.base_url + '/')

    # Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()

    # Fill login form and submit it (valid version)
    br.find_element_by_name('username').send_keys('foo')
    br.find_element_by_name('password').send_keys('bar')
    br.find_element_by_name('action').click()



def criarNovoUsuario():
    # Creates a dummy user for our tests (user is not authenticated at this point)
    u = UserFactory(username='foo', email='foo@example.com')
    u.set_password('bar')
    # Don't omit to call save() to insert object in database
    u.save()

def criarEspecieDocumental():
    especie = EspecieDocumental()
    especie.nome= "Teste"
    especie.save()

@given('Estou na pagina de cadastro de uma especie documental')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/especieDocumental')

    # Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()
    assert br.current_url.endswith('/especieDocumental/')

@when('Submeto o cadastro de uma nova especie documental deixando o campo em branco')
def step_impl(context):
    br = context.browser

    # Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()

    # Fill login form and submit it (valid version)
    br.find_element_by_name('submit').click()


@then('Nao conseguirei cadastrar a especie ate que eu preencha o campo nome.')
def step_impl(context):
    br = context.browser
    # br.get_screenshot_as_file('/tmp/screenshot.png')
    # Checks success status
    assert br.current_url.endswith('/especieDocumental/')
    assert br.find_element_by_id('nome').text == ""

#Scenario: Cadastrar nova EspecieDocumental
@when('Informo um nome ainda nao cadastrado no sistema')
def step_impl(context):
    br = context.browser
    especie = EspecieDocumental.objects.filter(nome='Folha de Ponto').exists()
    assert especie == False

@when('Submeto o cadastro de uma nova especie')
def step_impl(context):
    br = context.browser

    # Checks for Cross-Site Request Forgery protection input
    assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()

    # Fill login form and submit it (valid version)
    br.find_element_by_name('nome').send_keys('Folha de Ponto')
    br.find_element_by_name('submit').click()
    # br.get_screenshot_as_file('/tmp/screenshot.png')

@then('Sou redirecionado para a pagina principal de especie documental')
def step_impl(context):
    br = context.browser

    # Checks success status
    assert br.current_url.endswith('/especiesDocumentais_list/')

@then('A especie devera estar devidamente cadastrada.')
def step_impl(context):
    br = context.browser

    # Checks success status
    assert br.current_url.endswith('/especiesDocumentais_list/')
    assert br.find_element_by_id('nomeEspecie').text == "Folha de Ponto"

@when('Informo um nome ja cadastrado no sistema')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/especieDocumental')
    especie = EspecieDocumental.objects.filter(nome='Folha de Ponto').exists()
    assert  especie == True

@then('Recebo uma mensagem de erro informando que o nome ja existe.')
def step_impl(context):
    br = context.browser

    message = br.find_element_by_id('mensagem').text
    assert br.current_url.endswith('/especieDocumental/')
    assert message == "A Especie Documental ja existe. Por favor, tente novamente!"


@then('Nao conseguirei cadastrar a especie ate que eu preencha o com um nome diferente.')
def step_impl(context):
    br = context.browser
    # Checks success status
    assert br.current_url.endswith('/especieDocumental/')

#Scenario: Editar Especie documental
@given('Estou na pagina com a lista de especies documentais')
def step_impl(context):
        br = context.browser
        br.get(context.base_url + '/especiesDocumentais_list')
    # Checks success status
        assert br.current_url.endswith('/especiesDocumentais_list/')

@given('Possue uma ou mais especies documentais cadastradas')
def step_impl(context):
        especieDocumentalFactory(2)
        br = context.browser
        qtdEspecie = len(EspecieDocumental.objects.all())
        assert qtdEspecie > 0


@when('Seleciono o botao editar de uma especie documental')
def step_impl(context):
        br = context.browser
        br.get(context.base_url + '/especiesDocumentais_list')
        br.find_element_by_name('editar').click()

@when('Sou redirecionado para a pagina com seus dados ja preenchidos')
def step_impl(context):
        br = context.browser
        especies = EspecieDocumental.objects.all()
        br.get(context.base_url + '/especieDocumental/%d/edit' % especies[0].id)
        assert br.current_url.endswith('/especieDocumental/%d/edit/' % especies[0].id)

@when('Nao altero a especie documental deixando com o nome ja preenchido')
def step_impl(context):
        br = context.browser
        especies = EspecieDocumental.objects.all()
        assert br.find_element_by_id('nome').get_attribute('value') == especies[0].nome

@when ('Preencho o campo especie documental com um novo nome')
def step_impl(context):
        br = context.browser
        novo_nome = 'novo nome'
        especie = EspecieDocumental.objects.filter(nome=novo_nome).exists()
        assert especie == False
        br.find_element_by_id('nome').clear()
        nome = br.find_element_by_id('nome').send_keys(novo_nome)
        assert br.find_element_by_id('nome').get_attribute('value') == novo_nome

@when ('Edito o campo especie documental e o deixo em branco')
def step_impl(context):
        br = context.browser
        br.find_element_by_id('nome').clear()
        assert br.find_element_by_id('nome').get_attribute('value') == ""


@when('Clico no botao salvar')
def step_impl(context):
        br = context.browser
        assert br.find_element_by_name('csrfmiddlewaretoken').is_enabled()
        br.find_element_by_name('submit').click()


@then('Nao conseguirei editar a especie ate que preencha o campo nome')
def step_impl(context):
        br = context.browser
    # br.get_screenshot_as_file('/tmp/screenshot.png')
    # Checks success status
        especies = EspecieDocumental.objects.all()
        assert br.current_url.endswith('/especieDocumental/%d/edit/' % especies[0].id)
        assert br.find_element_by_id('nome').text == ""


@when('Edito o nome e coloco um nome que ja esta cadastrado')
def step_impl(context):
        br = context.browser
        especie = EspecieDocumental.objects.filter(nome='especie1').exists()
        assert  especie == True
        br.find_element_by_id('nome').clear()
        br.find_element_by_id('nome').send_keys('especie1')
        assert br.find_element_by_id('nome').get_attribute('value') == 'especie1'


@then('Nao conseguirei salvar a especie ate que eu a preencha com um nome diferente.')
def step_impl(context):
        br = context.browser

#Scenario: Visualizar Especie Documental
@given('Uma especie documental foi cadastrada')
def step_impl(context):
    br = context.browser
    criarEspecieDocumental()
    especie = EspecieDocumental.objects.filter(nome='Teste').exists()
    assert especie == True

@when('Sou redirecionado para a pagina principal de especie documental')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/especiesDocumentais_list/')
    # Checks success status
    assert br.current_url.endswith('/especiesDocumentais_list/')

@then('A especie documental devera aparecer na lista.')
def step_impl(context):
    br = context.browser

    # Checks success status
    assert br.current_url.endswith('/especiesDocumentais_list/')
    assert br.find_element_by_id('nomeEspecie').text == "Teste"


@given('Estou na pagina principal do sistema')
def step_impl(context):
    br = context.browser
    br.get(context.base_url + '/home')
    # Checks success status
    assert br.current_url.endswith('/home/')

@when('clico no botao visualizar especie documental')
def step_impl(context):
    br = context.browser
    br.find_element_by_name('visualizarEspecie').click()
    assert br.current_url.endswith('/especiesDocumentais_list/')

#Scenario: Excluir Especie documental
@given('que existem especies documentais cadastradas')
def step_impl(context):
        br = context.browser
        especieDocumentalFactory(3)
        br.refresh()
        assert EspecieDocumental.objects.count()==3
        assert EspecieDocumental.objects.filter(nome='especie0').exists()
        assert EspecieDocumental.objects.filter(nome='especie1').exists()
        assert EspecieDocumental.objects.filter(nome='especie2').exists()
        assert br.current_url.endswith('/especiesDocumentais_list/')

def especieDocumentalFactory(quantidade):
    for index in range(quantidade):
        nomeEspecie = 'especie' + str(index)
        especie = EspecieDocumentalFactory(nome=nomeEspecie)
        especie.save()


@when('clico no botao excluir')
def step_impl(context):
    br = context.browser
    br.find_element_by_name('excluir').click()
    assert br.current_url.endswith('/especiesDocumentais_list/')

@then('a especie documental deixara de existir.')
def step_impl(context):
        br = context.browser

        br.refresh()
        assert EspecieDocumental.objects.count() == 2