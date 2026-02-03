## Estrutura de pastas e arquivos do Projeto

```text
omie-console/
├── run.py
└── app/
    ├── __init__.py
    ├── routes.py # Fluxo simples, refresh de página após ações.
    ├── config/
    │   └── mapeamento.py
    ├── services/
    │   ├── omie_client.py # Cliente HTTP isolado (facilita testes e expansão).
    │   └── produto_service.py # Aqui fica toda a regra de negócio.
    ├── templates/
    │   └── index.html # HTML simples, responsivo e funcional.
    ├── static/
    │   └── style.css
    └── logs/
        └── associacoes.log
├── requirements.txt
└── README.md