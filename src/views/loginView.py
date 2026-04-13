import flet as ft
from database.db import verificar_login

def loginView(page: ft.Page):

    def ir_para_cadastro(e):
        page.go("/cadastro")

    def mostrar_erro(msg):
        banner = ft.Banner(
            bgcolor=ft.Colors.RED,
            leading=ft.Icon(ft.Icons.ERROR, color=ft.Colors.WHITE),
            content=ft.Text(msg),
            actions=[
                ft.TextButton(
                    "OK",
                    on_click=lambda e: fechar_banner(banner)
                )
            ],
        )

        page.overlay.append(banner) 
        banner.open = True
        page.update()


    def fechar_banner(banner):
        banner.open = False
        page.update()

    def fazer_login(e):
        user = verificar_login(
            campo_usuario.value,
            campo_senha.value
        )

        if user:
            print("Login OK")
            page.user = user 
            page.go("/home")
        else:
            mostrar_erro("Usuário ou senha incorretos")

    campo_usuario = ft.TextField(
        hint_text="Usuário",
        width=250,
        border=ft.InputBorder.UNDERLINE,
        color="white",
    )

    campo_senha = ft.TextField(
        hint_text="Senha",
        password=True,
        can_reveal_password=True,
        width=250,
        border=ft.InputBorder.UNDERLINE,
        color="white",
    )

    return ft.View(
        route="/login",
        controls=[
            ft.Container(
                expand=True,
                gradient=ft.LinearGradient(
                    colors=["#5f63f2", "#6f86ff"],
                    begin=ft.Alignment(-1, -1),
                    end=ft.Alignment(1, 1),
                ),
                content=ft.Column(
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[

                        ft.Image(
                            src="brasao.png",
                            width=220,
                            height=220,
                        ),

                        ft.Text(
                            "Seja Bem vindo!",
                            size=24,
                            weight=ft.FontWeight.BOLD,
                            color="white",
                        ),

                        ft.Container(height=20),

                        campo_usuario,
                        campo_senha,

                        ft.Container(height=20),

                        ft.ElevatedButton(
                            "Logar",
                            width=200,
                            height=45,
                            style=ft.ButtonStyle(
                                bgcolor="white",
                                color="#5f63f2",
                                shape=ft.RoundedRectangleBorder(radius=30),
                            ),
                            on_click=fazer_login,
                        ),

                        ft.TextButton(
                            "Cadastrar",
                            on_click=ir_para_cadastro,
                            style=ft.ButtonStyle(color="white"),
                        ),
                    ],
                ),
            )
        ],
    )