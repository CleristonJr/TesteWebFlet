import flet as ft
from inicio import paginaInicio
from treino import paginaTreino


def main(page: ft.Page):
    print('Iniciando página')
    page.title = "Treino Quest"
    page.go("/")

    
    def logingoogle(e):
        print('INDO PARA O LOGIN GOOGLE')
        page.go("/inicial")
        


    def mudar_tela(route):
        print(f"Rota atual: {page.route}")
        page.views.clear()

        # Adiciona a view de acordo com a rota
        if page.route == "/inicial":
            print("Carregando paginaInicio...")
            try:
                page.views.append(paginaInicio(page))
            except Exception as e:
                print(f"Erro ao carregar paginaInicio: {e}")
                page.views.append(ft.Text(f"Erro ao carregar paginaInicio: {e}"))
        elif page.route == "/treino":
            print("Carregando paginaTreino...")
            page.views.append(paginaTreino(page))
        else:
            # Rota padrão: tela de login
            print("Carregando tela de login...")
            page.views.append(
                ft.View(
                    "/",
                    [
                        ft.Container(
                            alignment=ft.alignment.center,
                            content=ft.Text('Logar com o Google')
                        ),
                        ft.Container(
                            content=ft.Image(
                                src='https://img.icons8.com/?size=512&id=17949&format=png'
                            ),
                            height=40,
                            on_click=logingoogle,
                            alignment=ft.alignment.center
                        ),
                    ],
                    vertical_alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER
                )
            )

        page.update()

    page.on_route_change = mudar_tela
    mudar_tela(page.route)

ft.app(target=main, assets_dir="assets")
