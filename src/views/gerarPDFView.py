import flet as ft

def gerarPDFView(page: ft.Page):

    campos_pacientes = []
    coluna_pacientes = ft.Column()

    def adicionar_paciente(e):

        campo = ft.TextField(
            hint_text=f"Paciente {len(campos_pacientes) + 1}",
            border=ft.InputBorder.UNDERLINE,
            width=220,
        )

        def remover_paciente(e):
            coluna_pacientes.controls.remove(linha)
            campos_pacientes.remove(campo)
            page.update()

        linha = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                campo,
                ft.IconButton(
                    icon=ft.Icons.CLOSE,
                    icon_color="red",
                    tooltip="Remover",
                    on_click=remover_paciente
                )
            ]
        )

        campos_pacientes.append(campo)
        coluna_pacientes.controls.append(linha)

        page.update()

    # Função para criar campos padrão
    def campo(texto, icone=None):
        return ft.TextField(
            hint_text=texto,
            border=ft.InputBorder.UNDERLINE,
            filled=False,
            text_size=14,
            prefix_icon=icone,
            width=280,
        )

    # Campo de data (especial com calendário)
    campo_data = ft.TextField(
        hint_text="Data",
        border=ft.InputBorder.UNDERLINE,
        read_only=True,
        width=280,
        prefix_icon=ft.Icons.CALENDAR_MONTH,
    )

    # DatePicker
    date_picker = ft.DatePicker()
    page.overlay.append(date_picker)

    # Abrir calendário
    def abrir_calendario(e):
        date_picker.open = True
        page.update()

    # Quando escolher a data
    def data_selecionada(e):
        if date_picker.value:
            campo_data.value = date_picker.value.strftime("%d/%m/%Y")
            page.update()

    date_picker.on_change = data_selecionada
    campo_data.on_click = abrir_calendario

    # Tela
    return ft.View(
        route="/gerarPDF",
        scroll=ft.ScrollMode.AUTO,
        controls=[
            ft.Container(
                expand=True,
                content=ft.Column(
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[

                        ft.Container(
                            height=120,
                            width=350,
                            border_radius=ft.border_radius.only(
                                bottom_left=50, bottom_right=50
                            ),
                            gradient=ft.LinearGradient(
                                colors=["#3b6eea", "#6fa8ff"],
                                begin=ft.Alignment(-1, -1),
                                end=ft.Alignment(1, 1),
                            ),
                        ),

                        ft.Container(height=20),

                        campo("Destino"),
                        ft.Row(
                            alignment=ft.MainAxisAlignment.CENTER,
                            controls=[
                                ft.Text("Pacientes", size=14),
                                ft.IconButton(
                                    icon=ft.Icons.ADD,
                                    on_click=adicionar_paciente
                                )
                            ]
                        ),

                        coluna_pacientes,

                        campo_data,

                        campo("Hora"),

                        ft.Container(height=20),

                        ft.ElevatedButton(
                            "Criar PDF",
                            width=200,
                            height=45,
                            style=ft.ButtonStyle(
                                shape=ft.RoundedRectangleBorder(radius=30),
                                bgcolor="#6fa8ff",
                                color="white",
                            ),
                        ),
                    ],
                ),
            )
        ],
    )

#TESTAR TELA
#def main(page: ft.Page):
#   page.title = "Tela estilo PDF"
#   page.horizontal_alignment = "center"
#   page.vertical_alignment = "center"
#
#   page.views.append(loginView(page))
#   page.update()


#ft.app(target=main)