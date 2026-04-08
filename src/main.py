import flet as ft
from views.loginView import loginView
from views.homeView import homeView

def main(page: ft.Page):
    page.title = "Requerimento de Diárias"

    def route_change(e): 
        page.views.clear()
        
        if page.route == "/login":
            page.views.append(loginView(page))
        if page.route == "/home":
            page.views.append(homeView(page))
        page.update()

    page.on_route_change = route_change
    
    page.go("/login")

ft.app(target=main)