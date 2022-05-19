# bibliotecas
import json

import pytest
import requests

from tests.utils.file_manager import ler_csv

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


def teste_consultar_pet():
    # Configura
    # Entrada
    pet_id = '1732181'

    # Resultados Esperados
    status_code_esperado = 200
    pet_id_esperado = 1732181
    pet_nome_esperado = "Snoopy"
    pet_nome_categoria_esperado = "cachorro"
    pet_nome_tag_esperado = "vacinado"

    # Executa
    resultado_obtido = requests.get(
        url=url + '/' + pet_id,
        headers=headers
    )

    # Valida
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))


    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == pet_id_esperado
    assert corpo_do_resultado_obtido['name'] == pet_nome_esperado
    assert corpo_do_resultado_obtido['category']['name'] == pet_nome_categoria_esperado
    assert corpo_do_resultado_obtido['tags'][0]['name'] == pet_nome_tag_esperado

def teste_alterar_pet():
    # Configura
    # Dados de Entrada virão do pet2.json

    # Resultados Esperados
    status_code_esperado = 200
    pet_id_esperado = 1732181
    pet_nome_esperado = "Snoopy"
    pet_nome_categoria_esperado = "cachorro"
    pet_nome_tag_esperado = "vacinado"
    pet_status_esperado = 'pending'

    # Executa
    resultado_obtido = requests.put(
        url=url,
        headers=headers,
        data=open('C:\\Users\\corre\\PycharmProjects\\134inicial\\vendors\\json\\pet2.json')
    )

    # Valida
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == pet_id_esperado
    assert corpo_do_resultado_obtido['name'] == pet_nome_esperado
    assert corpo_do_resultado_obtido['category']['name'] == pet_nome_categoria_esperado
    assert corpo_do_resultado_obtido['tags'][0]['name'] == pet_nome_tag_esperado
    assert corpo_do_resultado_obtido['status'] == pet_status_esperado


def teste_excluir_pet():
    # Configura
    # Dados de Entrada
    pet_id = '1732181'

    # Resultados Esperado
    status_code_esperado = 200
    tipo_esperado = 'unknown'
    mensagem_esperada = '1732181'

    # Executa
    resultado_obtido = requests.delete(
        url=url + '/' + pet_id,
        headers=headers
    )

    # Valida
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['code'] == status_code_esperado
    assert corpo_do_resultado_obtido['type'] == tipo_esperado
    assert corpo_do_resultado_obtido['message'] == mensagem_esperada

@pytest.mark.parametrize(
    'pet_id,category_id,category_name,pet_name,tags_id,tags_name,status',
    ler_csv('C:\\Users\\corre\\PycharmProjects\\134inicial\\vendors\\csv\\massa_incluir_pet.csv')
)
def teste_incluir_pet_em_massa(pet_id,category_id,category_name,pet_name,tags_id,tags_name,status):
    # 1. Configura
    # 1.1 Dados de Entrada
    # Os dados de entrada proveem do arquivo massa_incluir_pet.csv
    # 1.1.1 Montagem do JSON dinâmico
    corpo_json =  '{'
    corpo_json += f'  "id": {pet_id},'
    corpo_json += '  "category": {'
    corpo_json += f'    "id": {category_id},'
    corpo_json += f'    "name": "{category_name}"'
    corpo_json += '  },'
    corpo_json += f'  "name": "{pet_name}",'
    corpo_json += '  "photoUrls": ['
    corpo_json += '    "string"'
    corpo_json += '  ],'
    corpo_json += '  "tags": ['
    corpo_json += '    {'
    corpo_json += f'      "id": {tags_id},'
    corpo_json += f'      "name": "{tags_name}"'
    corpo_json += '    }'
    corpo_json += '  ],'
    corpo_json += f'  "status": "{status}"'
    corpo_json += '}'

    # 1.2 Resultados Esperados
    # Os dados de entrada também servirão como resultados
    # esperados, visto que o retorno é um eco
    status_code_esperado = 200

    # 2. Executa
    resultado_obtido = requests.post(
        url=url,
        headers=headers,
        data=corpo_json
    )

    # 3. Valida
    print(resultado_obtido)
    corpo_do_resultado_obtido = resultado_obtido.json()
    print(json.dumps(corpo_do_resultado_obtido, indent=4))

    assert resultado_obtido.status_code == status_code_esperado
    assert corpo_do_resultado_obtido['id'] == int(pet_id)
    assert corpo_do_resultado_obtido['name'] == pet_name
    assert corpo_do_resultado_obtido['category']['name'] == category_name
    assert corpo_do_resultado_obtido['tags'][0]['name'] == tags_name
