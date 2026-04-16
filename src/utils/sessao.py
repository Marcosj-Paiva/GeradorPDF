import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

CAMINHO = os.path.abspath(
    os.path.join(BASE_DIR, "..", "storage", "sessao.json")
)

def salvar_usuario(user_id):
    os.makedirs(os.path.dirname(CAMINHO), exist_ok=True)

    with open(CAMINHO, "w") as f:
        json.dump({"user_id": user_id}, f)

def carregar_usuario():
    if not os.path.exists(CAMINHO):
        return None

    with open(CAMINHO, "r") as f:
        dados = json.load(f)
        return dados.get("user_id")

def limpar_usuario():
    if os.path.exists(CAMINHO):
        os.remove(CAMINHO)