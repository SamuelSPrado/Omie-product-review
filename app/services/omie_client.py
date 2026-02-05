import requests
from app.config.settings import OMIE_BASE_URL

OMIE_BASE_URL_API_PRODUTOS = OMIE_BASE_URL

def post_omie(payload):
    response = requests.post(
        OMIE_BASE_URL_API_PRODUTOS,
        json=payload,
        timeout=30
    )

    try:
        return response.json()
    except ValueError:
        return {
            "codigo_status": "HTTP_ERROR",
            "descricao_status": response.text
        }