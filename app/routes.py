from flask import Blueprint, render_template, request, redirect, url_for
import logging
from .config.mapeamento import LOCAIS
from .services.produto_service import (
    listar_produtos,
    avaliar_status,
    associar_codigo
)

main = Blueprint("main", __name__)

logging.basicConfig(
    filename="app/logs/associacoes.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)

@main.route("/", methods=["GET", "POST"])
def index():
    local_selecionado = request.form.get("local")
    produtos = []

    if local_selecionado:
        cred = LOCAIS[local_selecionado]
        produtos_raw = listar_produtos(
            cred["app_key"],
            cred["app_secret"]
        )

        for p in produtos_raw:
            p["status"] = avaliar_status(p)

        produtos = produtos_raw

    return render_template(
        "index.html",
        locais=LOCAIS.keys(),
        local_selecionado=local_selecionado,
        produtos=produtos
    )

@main.route("/associar", method=["POST"])
def associar():
    local = request.form["local"]
    codigo_produto = request.form["codigo_produto"]
    codigo_integracao = request.form["codigo_integracao"]

    cred = LOCAIS[local]

    associar_codigo(
        cred["app_key"],
        cred["app_secret"],
        int(codigo_produto),
        codigo_integracao
    )

    return redirect(url_for("main.index", local=local))