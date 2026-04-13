import flet as ft

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
        page.go("/login")

    # 🔥 LISTA MOCK (depois vem do banco)
    pdfs = [
        {"destino": "Vitória", "data": "10/04/2026"},
        {"destino": "Belo Horizonte", "data": "08/04/2026"},
        {"destino": "São Paulo", "data": "05/04/2026"},
    ]

    # 🔥 função pra criar card
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
                                on_click=lambda e: print("abrir pdf")
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
                            bgcolor=ft.Colors.WHITE24,  # branco transparente
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