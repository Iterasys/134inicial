# Configura
# Biblioteca / Imports
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

# Dados de Entrada
# origem = 'São Paolo'
# destino = 'New York'
primeiro_nome = 'Juca'
bandeira = 'American Express'
lembrar_de_mim = True

# Resultados Esperados
# titulo_passagens_esperado = 'Flights from São Paolo to New York:'
mensagem_agradecimento_esperada = 'Thank you for your purchase today!'
preco_passagem_esperado = '555 USD'


# Executa
class Testes:
    # Início
    # def setup_method(self):
    # instanciar a biblioteca / motor / engine
    # informar onde esta o WebDriver (driver do Chrome)
    # self.driver = webdriver.Chrome(
    #     'C:\\Users\\corre\\PycharmProjects\\134inicial\\vendors\\drivers\\chromedriver102.exe'
    # )
    # espera ate 15 segundo por qualquer elemento
    # self.driver.implicitly_wait(15)

    # Fim
    def teardown_method(self):
        # destruir o objeto da biblioteca utilizado
        self.driver.quit()

    # Meio
    # lista para uso como massa de teste
    lista_de_valores = [
        ('São Paolo', 'New York', 'chrome'),
        ('Boston', 'New York', 'chrome'),
        ('San Diego', 'New York', 'chrome')
    ]

    @pytest.mark.parametrize('origem,destino,browser', lista_de_valores)
    def testar_comprar_passagem(self, origem, destino, browser):
        # e2e / end to end / ponta a ponta

        # Trouxe o setup_method / Iniciação para cá
        match browser:
            case 'chrome':
                self.driver = webdriver.Chrome(
                    'C:\\Users\\corre\\PycharmProjects\\134inicial\\vendors\\drivers\\chromedriver102.exe'

                )
            case 'firefox':
                # --| Setup
                options = Options()
                # options.add_argument("--headless")
                caps = webdriver.DesiredCapabilities().FIREFOX
                caps["marionette"] = True
                # browser = webdriver.Firefox(options=options, capabilities=caps,
                #                            executable_path=r"geckodriver.exe")
                # --| Parse
                self.driver = webdriver.Firefox(
                    executable_path='C:\\Users\\corre\\PycharmProjects\\134inicial\\vendors\\drivers\\geckodriver.exe'
                )

        # Pagina Inicial (Home)
        # Executa / Valida
        # abrir o browser no endereco
        self.driver.get('https://www.blazedemo.com')
        # clicar na lista de cidades de origem
        lista = self.driver.find_element(By.NAME, "fromPort")
        lista.click()
        # selecionar a cidade de origem desejada
        lista.find_element(By.XPATH, f'//option[ .= "{origem}"]').click()

        # clicar na lista de cidades de destino
        lista = self.driver.find_element(By.NAME, 'toPort')
        lista.click()

        # selecionar a cidade de destino desejada
        lista.find_element(By.XPATH, f'//option[ .= "{destino}"]').click()

        # clicar no botão de procurar voos
        self.driver.find_element(By.CSS_SELECTOR, 'input.btn.btn-primary').click()

        # Pagina Lista de Passagens
        # Executa / Valida
        assert self.driver.find_element(By.TAG_NAME, 'h3').text == f'Flights from {origem} to {destino}:'

        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) .btn").click()
        time.sleep(3)
        # Pagina de Compra
        # Executa / Valida
        # Limpar o campo do nome para evitar problemas ao digitar
        self.driver.find_element(By.ID, 'inputName').clear()
        # Prenche o nome do comprador
        self.driver.find_element(By.ID, 'inputName').send_keys(primeiro_nome)

        # Seleciona a bandeira do cartao
        lista = self.driver.find_element(By.ID, 'cardType')
        lista.click()
        lista.find_element(By.XPATH, f'//option[ .= "{bandeira}"]').click()

        # Marca o checkbox para ser lembrado
        self.driver.find_element(By.ID, 'rememberMe').click()
        time.sleep(3)
        # Aperta o botao Purchase Flight
        self.driver.find_element(By.CSS_SELECTOR, 'input.btn.btn-primary').click()

        # Pagina de Obrigado
        # Valida
        assert self.driver.find_element(By.TAG_NAME, 'h1').text == mensagem_agradecimento_esperada
        assert self.driver.find_element(By.CSS_SELECTOR, 'tr:nth-child(3) > td:nth-child(2)').text == \
               preco_passagem_esperado
        time.sleep(3)