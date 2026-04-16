from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from PyPDF2 import PdfReader, PdfWriter
from datetime import datetime
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

CAMINHO_BASE = os.path.abspath(
    os.path.join(BASE_DIR, "..", "storage", "templates", "pdf_base.pdf")
)

CAMINHO_OVERLAY = os.path.abspath(
    os.path.join(BASE_DIR, "..", "storage", "temp", "overlay.pdf")
)

PASTA_PDFS = os.path.abspath(
    os.path.join(BASE_DIR, "..", "storage", "pdfs")
)

def criar_overlay(dados):
    os.makedirs(os.path.dirname(CAMINHO_OVERLAY), exist_ok=True)

    c = canvas.Canvas(CAMINHO_OVERLAY, pagesize=A4)

    c.setFont("Helvetica", 10)

    c.drawString(55, 615, dados["nome"])

    c.drawString(35, 575.5, dados["rg"])
    c.drawString(275, 575.5, dados["cpf"])

    c.drawString(177, 559.5, f"{dados['justificativa']} - {dados['pacientes']}")

    c.drawString(93, 502.5, dados["local_saida"])
    c.drawString(323, 502.5, dados["data_saida"])

    c.drawString(61, 473, dados["destino"])
    c.drawString(338, 473, dados["data_chegada"])

    c.drawString(112, 271, dados["nome"])
    c.drawString(162, 255, dados["rg"])
    c.drawString(64, 239, dados["lotacao"])

    c.drawString(126, 222, f"{dados['justificativa']} - {dados['pacientes']}")

    c.save()

def gerar_pdf_final():
    os.makedirs(PASTA_PDFS, exist_ok=True)

    nome_arquivo = f"relatorio_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    caminho_saida = os.path.join(PASTA_PDFS, nome_arquivo)

    base = PdfReader(CAMINHO_BASE)
    overlay = PdfReader(CAMINHO_OVERLAY)

    writer = PdfWriter()

    pagina = base.pages[0]
    pagina.merge_page(overlay.pages[0])

    writer.add_page(pagina)

    with open(caminho_saida, "wb") as f:
        writer.write(f)

    return caminho_saida