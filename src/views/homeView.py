import flet as ft

def homeView(page: ft.Page):
    return ft.View(
        route="/home",
        appbar=ft.AppBar(title=ft.Text("Home")), 
        controls=[
            ft.TextField(label="Requerimento"),
        ],
    )