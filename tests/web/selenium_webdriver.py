# Configura
# Biblioteca / Imports
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


# Dados de Entrada
origem = 'São Paolo'
destino = 'New York'
primeiro_nome = 'Juca'
bandeira = 'American Express'
lembrar_de_mim = True

# Resultados Esperados
titulo_passagens_esperado = 'Flights from São Paolo to New York:'
mensagem_agradecimento_esperada = 'Thank you for your purchase today!'
preco_passagem_esperado = '555 USD'

# Executa
class Testes:
    # Início
    def setup_method(self):
        # instanciar a biblioteca / motor / engine
        # informar onde esta o WebDriver (driver do Chrome)
        self.driver = webdriver.Chrome(
            'C:\\Users\\corre\\PycharmProjects\\134inicial\\vendors\\drivers\\chromedriver102.exe'
        )
        # espera ate 15 segundo por qualquer elemento
        # self.driver.implicitly_wait(15)

    # Fim
    def teardown_method(self):
        # destruir o objeto da biblioteca utilizado
        self.driver.quit()

    # Meio
    def testar_comprar_passagem(self):
        # e2e / end to end / ponta a ponta
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
        assert self.driver.find_element(By.TAG_NAME, 'h3').text == titulo_passagens_esperado

        self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) .btn").click()
        time.sleep(3)
        # Pagina de Compra

        # Executa / Valida
        # Pagina de Obrigado
        # Executa

        # Valida