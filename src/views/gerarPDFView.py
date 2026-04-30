import flet as ft
import os
from datetime import datetime
import webbrowser
from utils.sobreEscreverPDF import criar_overlay
from utils.sobreEscreverPDF import gerar_pdf_final
from database.db import salvar_requerimento

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
html_path = os.path.join(BASE_DIR, "pdf.html")


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
pasta_pdfs = os.path.join(BASE_DIR, "..", "pdfs")

def gerarPDFView(page: ft.Page):

    campos_pacientes = []
    coluna_pacientes = ft.Column()

    def adicionar_paciente(e):
        campo = ft.TextField(
            hint_text=f"Paciente {len(campos_pacientes) + 1}",
            border=ft.InputBorder.UNDERLINE,
            color=ft.Colors.BLACK,  
            width=220,
        )

        def remover_paciente(e):
            coluna_pacientes.controls.remove(linha)
            campos_pacientes.remove(campo)
            page.update()

        linha = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                campo,
                ft.IconButton(
                    icon=ft.Icons.CLOSE,
                    icon_color="red",
                    on_click=remover_paciente
                )
            ]
        )

        campos_pacientes.append(campo)
        coluna_pacientes.controls.append(linha)
        page.update()

    def campo(texto, icone=None):
        return ft.TextField(
            hint_text=texto,
            border=ft.InputBorder.UNDERLINE,
            prefix_icon=icone,
            width=280,
            color=ft.Colors.BLACK,            
            border_color=ft.Colors.BLACK,    
            focused_border_color=ft.Colors.CYAN,
            hint_style=ft.TextStyle(color=ft.Colors.GREY_400),
        )

    campo_destino = campo("Destino")

    campo_local_saida = campo("Local de Saída")

    dropdown_justificativa = ft.Dropdown(
        width=280,
        hint_text="Justificativa",
        options=[
            ft.dropdown.Option("Transporte de Paciente"),
            ft.dropdown.Option("Busca de Medicamento"),
            ft.dropdown.Option("Outros"),
        ],
        color = ft.Colors.BLACK,
    )

    seta = ft.Container(
        padding=10,
        alignment=ft.Alignment.TOP_LEFT,
        content=ft.IconButton(
            icon=ft.Icons.ARROW_BACK,
            icon_color="white",
            on_click=lambda e: page.go("/home")
        )
    )

    campo_data_saida = ft.TextField(
        hint_text="Data de Saída",
        border=ft.InputBorder.UNDERLINE,
        read_only=True,
        width=280,
        prefix_icon=ft.Icons.CALENDAR_MONTH,
        color= ft.Colors.BLACK,
    )

    campo_data_chegada = ft.TextField(
        hint_text="Data de Chegada",
        border=ft.InputBorder.UNDERLINE,
        read_only=True,
        width=280,
        prefix_icon=ft.Icons.CALENDAR_MONTH,
        color= ft.Colors.BLACK,
    )

    date_picker = ft.DatePicker()
    page.overlay.append(date_picker)

    campo_ativo = {"campo": None}

    def abrir_calendario(e):
        campo_ativo["campo"] = e.control
        date_picker.open = True
        page.update()

    def data_selecionada(e):
        if date_picker.value and campo_ativo["campo"]:
            campo_ativo["campo"].value = date_picker.value.strftime("%d/%m/%Y")
            page.update()

    date_picker.on_change = data_selecionada
    campo_data_saida.on_click = abrir_calendario
    campo_data_chegada.on_click = abrir_calendario

    botao_pacientes = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.Text("Pacientes", color=ft.Colors.BLACK),
            ft.IconButton(
                icon=ft.Icons.ADD,
                icon_color=ft.Colors.BLACK,
                on_click=adicionar_paciente
            )
        ]
    )

    def criar_pdf(e):

        user = getattr(page, "user", None)

        lista_pacientes = [c.value for c in campos_pacientes if c.value]

        dados = {
            "nome": user[1] if user else "",
            "rg": user[2] if user else "",
            "cpf": user[3] if user else "",
            "lotacao": user[4] if user else "",
            "destino": campo_destino.value,
            "local_saida": campo_local_saida.value,
            "data_saida": campo_data_saida.value,
            "data_chegada": campo_data_chegada.value,
            "justificativa": dropdown_justificativa.value,
            "pacientes": ", ".join(lista_pacientes),
        }

        criar_overlay(dados)

        caminho_pdf = gerar_pdf_final() 

        salvar_requerimento({
            "motorista_id": user[0],
            "destino": campo_destino.value,
            "local_saida": campo_local_saida.value,
            "data_saida": campo_data_saida.value,
            "data_chegada": campo_data_chegada.value,
            "justificativa": dropdown_justificativa.value,
            "pacientes": ", ".join(lista_pacientes),
            "arquivo_pdf": caminho_pdf
        })

        webbrowser.open(caminho_pdf)

        print("PDF final gerado com sucesso!")

        page.go("/home")

    return ft.View(
        route="/gerarPDF",
        controls=[
            ft.Container(
                expand=True,
                bgcolor= ft.Colors.WHITE,
                content=ft.Column(
                    scroll=ft.ScrollMode.AUTO,
                    spacing=12,
                    alignment=ft.MainAxisAlignment.START,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[

                        ft.Container(
                            seta,
                            height=120,
                            width=350,
                            border_radius=ft.border_radius.only(
                                bottom_left=50, bottom_right=50
                            ),
                            gradient=ft.LinearGradient(
                                colors=["#3b6eea", "#6fa8ff"],
                                begin=ft.Alignment(-1, -1),
                                end=ft.Alignment(1, 1),
                            ),
                        ),

                        campo_local_saida,
                        campo_destino,
                        dropdown_justificativa,

                        botao_pacientes,
                        coluna_pacientes,

                        campo_data_saida,
                        campo_data_chegada,

                        ft.Container(height=20),

                        ft.ElevatedButton(
                            "Criar PDF",
                            width=200,
                            height=45,
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=30),
                                bgcolor="#6fa8ff",
                                color="white",
                            ),
                            on_click=criar_pdf
                        ),
                    ],
                ),
            )
        ],
    )