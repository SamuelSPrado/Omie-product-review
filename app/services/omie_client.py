import requests

OMIE_BASE_URL_API_PRODUTOS = "https://app.omie.com.br/api/v1/geral/produtos/"

def post_omie(payload):
    response = requests.post(
        OMIE_BASE_URL_API_PRODUTOS,
        json=payload,
        timeout=30
    )
    response.raise_for_status()
    return response.json()