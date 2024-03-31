from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager

servico = Service(ChromeDriverManager().install()) # Configurando o webdriver
driver = webdriver.Chrome(service=servico)

time.sleep(2) # Esperando a página carregar

# Cenário 1: Verificar se o login com informações válidas está funcionando corretamente.
def test_login_credenciais_validas():
    # Dado que o usuário esteja na página de login
    try:
        logout = driver.find_element(By.CLASS_NAME, 'logout')  # Garantindo que o usuário está deslogado
        logout.click()
    except:
        driver.get("http://automationpractice.pl/index.php?controller=authentication&back=myaccount")
        time.sleep(3)
    
    # Quando o usuário inserir informações válidas de login
    email_input = driver.find_element(By.ID, 'email')
    email_input.send_keys("test@outlook.com")
    password_input = driver.find_element(By.ID, 'passwd')
    password_input.send_keys("senha123")
    login_button = driver.find_element(By.XPATH,'//*[@id="SubmitLogin"]/span')
    login_button.click()
    time.sleep(2)  # Espera para garantir que a página seja carregada

    # Então o usuário deve ser redirecionado para a página da sua conta
    try:
        elemento_pagina_conta = driver.find_element(By.CLASS_NAME, 'info-account')
        if elemento_pagina_conta: # Verificando se o usuário foi redirecionado
            print('sucesso.')
    except:
        print('erro. usuário deveria ter sido redirecionado para a página de sua conta.')

# Cenário 2: Verificar login com email inválido
def test_login_email_invalido():
    # Dado que o usuário esteja na página de login
    try:
        logout = driver.find_element(By.CLASS_NAME, 'logout') # Garantindo que o usuário está deslogado
        logout.click()
    except:
        driver.get("http://automationpractice.pl/index.php?controller=authentication&back=myaccount")
        time.sleep(3)

    # Quando o usuário inserir um e-mail inválido
    email_input = driver.find_element(By.ID, 'email')
    email_input.send_keys("invalidemail")
    password_input = driver.find_element(By.ID, 'passwd')
    password_input.send_keys("examplepassword")
    login_button = driver.find_element(By.XPATH,'//*[@id="SubmitLogin"]/span')
    login_button.click()
    time.sleep(2)  # Espera para garantir que a página seja carregada
    get_source = driver.page_source
    search_text = "Invalid email address."

    # Então o usuário deve receber uma mensagem de email inválido.
    if search_text in get_source: # Verificando se a mensagem de erro está presente na página.
        print('sucesso.')
    else:
        print('erro. mensagem de email invalido esperada.')


# Cenário 3: Verificar login com senha incorreta
def test_login_senha_incorreta():
    # Dado que o usuário esteja na página de login
    try:
        logout = driver.find_element(By.CLASS_NAME, 'logout')  # Garantindo que o usuário está deslogado
        logout.click()
    except:
        driver.get("http://automationpractice.pl/index.php?controller=authentication&back=myaccount")
        time.sleep(3)

    # Quando o usuário inserir uma senha inválida
    email_input = driver.find_element(By.ID, 'email')
    email_input.send_keys("test@outlook.com")
    password_input = driver.find_element(By.ID, 'passwd')
    password_input.send_keys("123")
    login_button = driver.find_element(By.XPATH, '//*[@id="SubmitLogin"]/span')
    login_button.click()
    time.sleep(2)  # Espera para garantir que a página seja carregada

    # Então o usuário deve receber uma mensagem de senha inválida.
    get_source = driver.page_source
    search_text = "Invalid password."
    if search_text in get_source: # Verificando se a mensagem de erro está presente na página.
        print('sucesso.')
    else:
        print('erro. mensagem de senha invalida esperada.')

# Executar os testes
test_login_credenciais_validas()
test_login_email_invalido()
test_login_senha_incorreta()

# Fechar o navegador
driver.quit()

# Outras sugestões de cenário:
# Cenário 4: Verificar se o e-mail digitado para criar conta é de fato um email com domínio válido (gmail, hotmail, outlook...)
# Cenário 5: Verificar se há mensagem de erro para campos obrigatórios vazios (email ou senha)
