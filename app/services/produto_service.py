import time
import logging
from .omie_client import post_omie

logger = logging.getLogger("associacoes")

def listar_produtos(app_key, app_secret):
    pagina = 1
    produtos = []

    while True:
        payload = {
            "call": "ListarProdutosResumido",
            "app_key": app_key,
            "app_secret": app_secret,
            "param": [{
                "pagina": pagina,
                "registros_por_pagina": 100,
                "apenas_importado_api": "N",
                "filtrar_apenas_omiepdv": "N"
            }]
        }

        response = post_omie(payload)

        produtos.extend(response.get("produto_servico_resumido", []))

        if pagina >= response.get("total_de_paginas", 1):
            break

        pagina += 1

    return produtos

def avaliar_status(produto):
    cod = produto.get("codigo")
    cod_int = produto.get("codigo_produto_integracao", "")

    if not cod_int:
        return "Sem código integração"

    if cod == cod_int:
        return "Códigos corretos"

    return "Código divergênte"