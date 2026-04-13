import pdfkit
import base64

def imagem_para_base64(caminho):
    with open(caminho, "rb") as img:
        return base64.b64encode(img.read()).decode("utf-8")

config = pdfkit.configuration(
    wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
)

def gerar_pdf(html_string, nome_arquivo):
    options = {
        "enable-local-file-access": "",
        "encoding": "UTF-8",
        "page-size": "A4",
        "margin-top": "0mm",
        "margin-bottom": "0mm",
        "margin-left": "0mm",
        "margin-right": "0mm",
    }

    pdfkit.from_string(
        html_string,
        nome_arquivo,
        configuration=config,
        options=options
    )


def preencher_html(html, dados):
    for chave, valor in dados.items():
        html = html.replace(f"{{{{{chave}}}}}", str(valor))
    return html