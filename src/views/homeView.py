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
        }
        for row in dados_db
    ]

    def abrir_pdf(caminho):
        if caminho and os.path.exists(caminho):
            webbrowser.open(caminho)
        else:
            print("Arquivo não encontrado")

    def criar_card(pdf):
        return ft.Container(
            width=300,
            padding=10,
            border_radius=15,
            bgcolor="white",
            content=ft.Column(
                spacing=5,
                controls=[
                    ft.Text(pdf["destino"], size=16, weight="bold"),
                    ft.Text(f'Data: {pdf["data"]}', size=12),
                    ft.Row(
                        alignment=ft.MainAxisAlignment.END,
                        controls=[
                            ft.IconButton(
                                icon=ft.Icons.PICTURE_AS_PDF,
                                tooltip="Abrir PDF",
                                on_click=lambda e, caminho=pdf["arquivo"]: abrir_pdf(caminho)
                            )
                        ]
                    )
                ]
            )
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