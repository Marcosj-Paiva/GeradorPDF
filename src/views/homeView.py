import flet as ft

def homeView(page: ft.Page):

    lista_pdfs = [
        {"titulo": "Viagem BH", "data": "01/04/2026"},
        {"titulo": "Viagem SP", "data": "05/04/2026"},
        {"titulo": "Reunião RJ", "data": "10/04/2026"},
    ]

    def abrir_pdf(e):
        print("Abrir PDF")

    def criar_card(pdf):
        return ft.Container(
            width=320,
            padding=15,
            border_radius=15,
            bgcolor="white",
            shadow=ft.BoxShadow(
                blur_radius=10,
                color="black12"
            ),
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.Column(
                        spacing=5,
                        controls=[
                            ft.Text(pdf["titulo"], weight="bold"),
                            ft.Text(pdf["data"], size=12, color="grey"),
                        ],
                    ),
                    ft.IconButton(
                        icon=ft.Icons.PICTURE_AS_PDF,
                        icon_color="red",
                        on_click=abrir_pdf
                    )
                ],
            ),
        )

    return ft.View(
        route="/home",
        controls=[
            ft.Container(
                expand=True,
                bgcolor="#f5f7fb",
                padding=20,
                content=ft.Column(
                    scroll=ft.ScrollMode.AUTO,
                    controls=[

                        ft.Text(
                            "Meus PDFs",
                            size=22,
                            weight="bold"
                        ),

                        ft.Container(height=10),

                        *[criar_card(pdf) for pdf in lista_pdfs],

                        ft.Container(height=20),

                        ft.ElevatedButton(
                            "Novo PDF",
                            icon=ft.Icons.ADD,
                            on_click=lambda e: page.go("/gerarPDF")
                        )
                    ],
                ),
            )
        ],
    )