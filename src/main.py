import flet as ft
from views.loginView import loginView
from views.homeView import homeView
from views.gerarPDFView import gerarPDFView
from views.carregamentoView import carregamentoView
from views.cadastroView import cadastroView
from database.db import conectar

def main(page: ft.Page):
    conn = conectar()
    print("Banco conectado com sucesso!")
    conn.close()

    page.title = "Requerimento de Diárias"

    page.assets_dir = "assets"

    page.window.width = 360
    page.window.height = 640

    page.padding = 0

    def route_change(e): 
        page.views.clear()
        
        if page.route == "/login":
            page.views.append(loginView(page))
        elif page.route == "/home":
            page.views.append(homeView(page))
        elif page.route == "/gerarPDF":
            page.views.append(gerarPDFView(page))
        elif page.route == "/carregamento":
            page.views.append(carregamentoView(page))
        elif page.route == "/cadastro":
            page.views.append(cadastroView(page))

        page.update()

    page.on_route_change = route_change
    
    page.go("/login")

ft.app(target=main)