import flet as ft
import re

def cadastroView(page: ft.Page):

    campo_nome = ft.TextField(
        hint_text='Nome Completo',
        width=250, 
        border=ft.InputBorder.UNDERLINE, 
        color="white",
        hint_style=ft.TextStyle(color="white70"),
        error_style=ft.TextStyle(color="red"),
    )

    campo_rg = ft.TextField(
        hint_text='RG', 
        width=250, 
        border=ft.InputBorder.UNDERLINE, 
        color="white",
        hint_style=ft.TextStyle(color="white70"),
        error_style=ft.TextStyle(color="red"),    
    )
    
    campo_cpf = ft.TextField(
        hint_text='CPF', 
        width=250, 
        border=ft.InputBorder.UNDERLINE, 
        color="white",
        hint_style=ft.TextStyle(color="white70"),
        error_style=ft.TextStyle(color="red"),    
    )
    
    campo_usuario = ft.TextField(
        hint_text='Usuário', 
        width=250, 
        border=ft.InputBorder.UNDERLINE, 
        color="white",
        hint_style=ft.TextStyle(color="white70"),
        error_style=ft.TextStyle(color="red"),
    )

    campo_senha = ft.TextField(
        hint_text='Senha',
        password=True,
        can_reveal_password=True,
        width=250,
        border=ft.InputBorder.UNDERLINE,
        color="white",
        hint_style=ft.TextStyle(color="white70"),
        error_style=ft.TextStyle(color="red"),
    )

    dropdown_area = ft.Dropdown(
        width=250,
        hint_text="Área de Atuação",
        options=[
            ft.dropdown.Option("Saúde"),
            ft.dropdown.Option("Educação"),
            ft.dropdown.Option("Assistência Social"),
        ],
    )

    erro_nome = ft.Text("", color="red", size=12)
    erro_rg = ft.Text("", color="red", size=12)
    erro_cpf = ft.Text("", color="red", size=12)
    erro_usuario = ft.Text("", color="red", size=12)
    erro_senha = ft.Text("", color="red", size=12)
    erro_area = ft.Text("", color="red", size=12)
    erro_senha = ft.Text("", color="red", size=12)

    def validar_nome(nome):
        return re.fullmatch(r"[A-Za-zÀ-ÿ ]+", nome)
    
    def validar_cpf(cpf):
        return re.fullmatch(r"\d{3}\.\d{3}\.\d{3}-\d{2}", cpf)

    def validar_senha(senha):
        return re.fullmatch(r"(?=.*[A-Z])(?=.*\d).{6,}", senha)

    def validar_rg(rg):
        return bool(re.fullmatch(r"(?=(?:\D*\d){8,})[0-9\.\-]+", rg))

    def validar(e):
        erro = False

        if not campo_nome.value or not campo_nome.value.strip():
            erro_nome.value = "Informe o nome"
            campo_nome.border_color = "red"
            campo_nome.focused_border_color = "red"
            erro = True
        elif not validar_nome(campo_nome.value):  
            erro_nome.value = "Nome inválido"
            campo_nome.border_color = "red"
            campo_nome.focused_border_color = "red"
            erro = True
        else:
            erro_nome.value = ""
            campo_nome.border_color = "white"
            campo_nome.focused_border_color = "white"

        if not campo_rg.value or not campo_rg.value.strip():
            erro_rg.value = "Informe o rg"
            campo_rg.border_color = "red"
            campo_rg.focused_border_color = "red"
            erro = True
        elif not validar_rg(campo_rg.value):  
            erro_rg.value = "RG inválido"
            campo_rg.border_color = "red"
            campo_rg.focused_border_color = "red"
            erro = True        
        else:
            erro_rg.value = ""
            campo_rg.border_color = "white"
            campo_rg.focused_border_color = "white"

        if not campo_cpf.value or not campo_cpf.value.strip():
            erro_cpf.value = "Informe o CPF"
            campo_cpf.border_color = "red"
            campo_cpf.focused_border_color = "red"
            erro = True
        elif not validar_cpf(campo_cpf.value):  
            erro_cpf.value = "CPF inválido"
            campo_cpf.border_color = "red"
            campo_cpf.focused_border_color = "red"
            erro = True        
        else:
            erro_cpf.value = ""
            campo_cpf.border_color = "white"
            campo_cpf.focused_border_color = "white"

        if not campo_usuario.value or not campo_usuario.value.strip():
            erro_usuario.value = "Informe um nome para Usuário"
            campo_usuario.border_color = "red"
            campo_usuario.focused_border_color = "red"
            erro = True
        else:
            erro_usuario.value = ""
            campo_usuario.border_color = "white"
            campo_usuario.focused_border_color = "white"

        if not campo_senha.value or not campo_senha.value.strip():
            erro_senha.value = "Informe a senha"
            campo_senha.border_color = "red"
            campo_senha.focused_border_color = "red"
            erro = True
        elif not validar_senha(campo_senha.value):  
            erro_senha.value = "Senha inválida"
            campo_senha.border_color = "red"
            campo_senha.focused_border_color = "red"
            erro = True
        else:
            erro_senha.value = ""
            campo_senha.border_color = "white"
            campo_senha.focused_border_color = "white"

        if not dropdown_area.value or not dropdown_area.value.strip():
            erro_area.value = "Selecione ua área de atuação"
            dropdown_area.border_color = "red"
            dropdown_area.focused_border_color = "red"
            erro = True
        else:
            erro_area.value = ""
            dropdown_area.border_color = "white"
            dropdown_area.focused_border_color = "white"

        page.update()

        if not erro:
            print("Nome validado com sucesso!")
            page.go("/login")

    return ft.View(
        route="/cadastro",
        controls=[
            ft.Container(
                expand=True,
                gradient=ft.LinearGradient(
                    colors=["#5f63f2", "#6f86ff"],
                    begin=ft.Alignment(-1, -1),
                    end=ft.Alignment(1, 1),
                ),
                content=ft.Column(
                    scroll= ft.ScrollMode.AUTO,
                    spacing=10,
                    alignment=ft.MainAxisAlignment.CENTER,  
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[
                        campo_nome,
                        erro_nome,
                        campo_rg,
                        erro_rg,
                        campo_cpf,
                        erro_cpf,
                        dropdown_area,
                        erro_area,
                        campo_usuario,
                        erro_usuario,
                        campo_senha,
                        erro_senha,

                        ft.Container(height=20),

                        ft.ElevatedButton(
                            "Cadastrar",
                            width=200,
                            height=45,
                            style=ft.ButtonStyle(
                                bgcolor="white",
                                color="#5f63f2",
                                shape=ft.RoundedRectangleBorder(radius=30),
                            ),
                            on_click=validar,
                        ),
                    ],
                ),
            )
        ],
    )