# bibliotecas
import pytest
import requests

# variaveis publicas
url = 'https://petstore.swagger.io/v2/pet'
headers = {'Content-Type': 'application/json'}

# definições das funcões (defs)

def teste_incluir_pet():
    # Configura / Prepara
    # Dados de entrada provem do pet1.json

    # Resultados Esperados
    status_code_esperado = 200
    pet_id_esperado = 1732181
    pet_nome_esperado = "Snoopy"
    pet_nome_categoria_esperado = "cachorro"
    pet_nome_tag_esperado = "vacinado"

    # Executa
    resultado_obtido = requests.post(
        url=url,
        headers=headers,
        data=open('C:\\Users\\corre\\PycharmProjects\\134inicial\\vendors\\json\\pet1.json')
    )

    # Valida
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(corpo_do_resultado_obtido)

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == pet_id_esperado
    assert corpo_do_resultado_obtido['name'] == pet_nome_esperado
    assert corpo_do_resultado_obtido['category']['name'] == pet_nome_categoria_esperado
    assert corpo_do_resultado_obtido['tags'][0]['name'] == pet_nome_tag_esperado
