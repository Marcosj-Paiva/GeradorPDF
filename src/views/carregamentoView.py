import flet as ft

def carregamentoView(page: ft.Page):

    return ft.View(
        route = "/carregamento",
        controls=[
            ft.Container(
                expand= True,
                gradient= ft.LinearGradient(
                    colors=["#5f63f2", "#6f86ff"],
                    begin=ft.Alignment(-1, -1),
                    end=ft.Alignment(1, 1),
                ),
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment= ft.CrossAxisAlignment.CENTER,
                    controls=[
                        ft.Image(
                            src="brasao.png",
                            width=220,
                            height=220,
                        ),

                        ft.Container(height=20),

                        ft.ProgressRing(color='white'),

                    ],
                ),
            )
        ],
    )