import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "requerimentoBD.db")

def conectar():
    return sqlite3.connect(db_path)

def inserir_motorista(nome, rg, cpf, lotacao, usuario, senha):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO motorista (nome, rg, cpf, lotacao, usuario, senha)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (nome, rg, cpf, lotacao, usuario, senha))

    conn.commit()
    conn.close()

    
def verificar_login(usuario, senha):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM motorista
        WHERE usuario = ? AND senha = ?
    """, (usuario, senha))

    user = cursor.fetchone()

    conn.close()

    return user