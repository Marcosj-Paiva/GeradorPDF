import flet as ft
from database.db import buscar_requerimentos_por_motorista
from utils.sessao import limpar_usuario
import os
import webbrowser

def homeView(page: ft.Page):

    user = getattr(page, "user", None)

    if not user:
        return ft.View(
            route="/home",
            controls=[
                ft.Text("Usuário não logado"),
                ft.ElevatedButton("Voltar", on_click=lambda e: page.go("/login"))
            ]
        )

    nome = user[1]

    def sair(e):
        page.user = None
        limpar_usuario()
        page.go("/login")

    dados_db = buscar_requerimentos_por_motorista(user[0])

    pdfs = [
        {
            "id": row[0],
            "destino": row[1],
            "data": row[2],
            "arquivo": row[3],
            "pacientes": row[4],
            "justificativa": row[5],
        }
        for row in dados_db
    ]

    def abrir_pdf(caminho):
        if caminho and os.path.exists(caminho):
            webbrowser.open(caminho)
        else:
            print("Arquivo não encontrado")
    
    def criar_card(pdf):

        lista_controles = [
            ft.Text(pdf["destino"], size=16, weight="bold", color=ft.Colors.BLACK),
            ft.Text(f'Data: {pdf["data"]}', size=12, color=ft.Colors.BLACK),
            ft.Text(f'Justificativa: {pdf["justificativa"]}', size=12, color=ft.Colors.BLACK),
        ]

        if pdf.get("pacientes") and str(pdf["pacientes"]).strip():
            lista_controles.append(
                ft.Text(f'Pacientes: {pdf["pacientes"]}', size=12, color=ft.Colors.BLACK)
            )

        return ft.Container(
            width=300,
            padding=10,
            border_radius=15,
            bgcolor="white",
            content=ft.Stack([
                ft.Column(
                    spacing=5,
                    controls=lista_controles,
                    width=250 
                ),
         
                ft.IconButton(
                    icon=ft.Icons.PICTURE_AS_PDF,
                    icon_color=ft.Colors.RED_700,
                    tooltip="Abrir PDF",
                    top=-5,    
                    right=-5,  
                    on_click=lambda e, caminho=pdf["arquivo"]: abrir_pdf(caminho)
                )
            ])
        )
    
    return ft.View(
        route="/home",
        scroll=ft.ScrollMode.AUTO,
        controls=[
            ft.Container(
                expand=True,
                gradient=ft.LinearGradient(
                    colors=["#5f63f2", "#6f86ff"],
                    begin=ft.Alignment(-1, -1),
                    end=ft.Alignment(1, 1),
                ),
                content=ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Container(height=40),

                        ft.Text(
                            f"Bem-vindo, {nome} 👋",
                            size=24,
                            weight=ft.FontWeight.BOLD,
                            color="white",
                        ),

                        ft.Container(height=10),

                        ft.Text(
                            "Seus PDFs",
                            size=18,
                            color="white"
                        ),

                        ft.Container(height=10),

                        ft.Container(
                            height=300,  
                            width=320,
                            bgcolor=ft.Colors.WHITE24,  
                            border_radius=15,
                            padding=10,
                            content=ft.Column(
                                scroll=ft.ScrollMode.AUTO,  
                                spacing=10,
                                controls=[criar_card(pdf) for pdf in pdfs]
                            )
                        ),

                        ft.Container(height=20),

                        ft.ElevatedButton(
                            "Gerar PDF",
                            on_click=lambda e: page.go("/gerarPDF")
                        ),

                        ft.TextButton(
                            "Sair",
                            on_click=sair,
                            style=ft.ButtonStyle(color="white")
                        )
                    ],
                ),
            )
        ],
    )