# Configura
# Biblioteca / Imports


# Dados de Entrada
from selenium import webdriver

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

    # Fim
    def teardown_method(self):
        # destruir o objeto da biblioteca utilizado
        self.driver.quit()

    # Meio
    def testar_comprar_passagem(self):
        # e2e / end to end / ponta a ponta
        # Pagina Inicial (Home)
        # Executa / Valida

        # Pagina Lista de Passagens
        # Executa / Valida

        # Pagina de Compra

        # Executa / Valida
        # Pagina de Obrigado
        # Executa

        # Valida