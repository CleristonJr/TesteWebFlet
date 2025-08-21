import flet as ft
import pandas as pd
import os

def manipular_excel(e, page: ft.Page, content_column: ft.Column):
    
    try:

        caminho_arquivo_original = 'https://raw.githubusercontent.com/CleristonJr/TesteWebFlet/main/Sheet2WPSOffice.xlsx'

        # Limpa o conteúdo anterior
        content_column.controls.clear()
        content_column.controls.append(ft.Text("Iniciando a leitura do Excel...", size=16))
        page.update()

        #url_raw = 'https://raw.githubusercontent.com/CleristonJr/TesteWebFlet/main/Sheet2WPSOffice.xlsx'
        df = pd.DataFrame(dados)

        content_column.controls.append(ft.Text("\nConteúdo original do arquivo:"))
        content_column.controls.append(ft.Text(df.to_string()))
        page.update()
      
   
    except Exception as e:
        content_column.controls.append(ft.Text(f"Ocorreu um erro ao processar o arquivo: {e}"))
        page.update()


def paginaInicio(page: ft.Page):
    page.title = "Treino Quest"
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'
    page.theme_mode = ft.ThemeMode.LIGHT

    # Coluna para exibir o conteúdo principal e os resultados do Excel
    content_column = ft.Column(
        controls=[
            ft.Text("Bem-vindo ao Treino Quest!", size=24, weight=ft.FontWeight.BOLD),
            ft.Text("Escolha uma opção no menu ou inicie seu treino."),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True
    )

    def check_item_clicked(e):
        
        page.theme_mode = (
            ft.ThemeMode.LIGHT if page.theme_mode != ft.ThemeMode.LIGHT else ft.ThemeMode.DARK
        )
        page.update()

    def tela_Treino(e):
        
        print("Navegando para Treino")
        # page.go("/treino")

    def destino_selecionado(e):
        
        if rail.selected_index == 1:
            print("Alterar Treino selecionado!")
            # page.go("/alterarTreino")
            # page.update()
        
    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=70,
        min_extended_width=200,
        leading=ft.Text("Menu"),
        group_alignment=-0.9,
        destinations=[
            ft.NavigationRailDestination(
                icon=ft.Icon(ft.Icons.FITNESS_CENTER),
                label="Treino",
            ),
            ft.NavigationRailDestination(
                icon=ft.Icon(ft.Icons.EDIT_NOTE),
                label="Alterar Treino",
            ),
        ],
        on_change=destino_selecionado
    )
    
    appbar_inicio = ft.CupertinoAppBar(
        leading=ft.IconButton(icon=ft.Icons.WB_SUNNY_OUTLINED, on_click=check_item_clicked, icon_size=20),
        middle=ft.Text("Treino Quest"),
        bgcolor=ft.Colors.SURFACE_CONTAINER_HIGHEST,
    )

    return ft.View(
        "/inicial",
        [
            ft.Row([
                rail,
                ft.VerticalDivider(width=1),
                ft.Column(
                    [
                        ft.ElevatedButton(
                            "Treino de Hoje",
                            style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=60),
                            elevation=2,
                            on_click=tela_Treino
                        ),
                        ft.ElevatedButton(
                            "Manipular Excel",
                            on_click=lambda e: manipular_excel(e, page, content_column),
                            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=10)),
                            elevation=2
                        ),
                        content_column
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    expand=True
                )
            ], expand=True)
        ],
        appbar=appbar_inicio,
    )
