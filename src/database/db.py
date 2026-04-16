import sqlite3
import os
from datetime import datetime

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

def salvar_requerimento(dados):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO requerimento (
            motorista_id,
            destino,
            local_saida,
            data_saida,
            data_chegada,
            justificativa,
            pacientes,
            arquivo_pdf,
            data_criacao
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        dados["motorista_id"],
        dados["destino"],
        dados["local_saida"],
        dados["data_saida"],
        dados["data_chegada"],
        dados["justificativa"],
        dados["pacientes"],
        dados["arquivo_pdf"],
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()
    conn.close()

def buscar_requerimentos_por_motorista(motorista_id):
    conn = conectar() 
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, destino, data_saida, arquivo_pdf
        FROM requerimento
        WHERE motorista_id = ?
        ORDER BY id DESC
    """, (motorista_id,))

    resultados = cursor.fetchall()
    conn.close()

    return resultados

def buscar_usuario_por_id(user_id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM motorista WHERE id = ?", (user_id,))
    user = cursor.fetchone()

    conn.close()
    return user