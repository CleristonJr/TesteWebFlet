import flet as ft
from flet.auth.providers import GoogleOAuthProvider
from inicio import paginaInicio
from descanso import paginaDescanso
from treino import paginaTreino
from acabou import paginaAcabou
from alterar import paginaAlterarTreino
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente, que devem ser configuradas como secrets no GitHub
load_dotenv(encoding='utf-8')

client_id = os.getenv('ID')
client_secret = os.getenv('SECRET_ID')
redirect_url = os.getenv('REDIRECT_URL')

def main(page: ft.Page):
    page.title = "Treino Quest"
    page.go("/")

    # Certifica que as secrets foram carregadas.
    if not client_id or not client_secret or not redirect_url:
        print("Erro: ID, SECRET_ID e/ou REDIRECT_URL não foram carregados das variáveis de ambiente.")
        # Exibe uma mensagem de erro na tela caso as secrets não estejam configuradas.
        page.add(
            ft.Text(
                "Erro de configuração: ID, SECRET_ID ou REDIRECT_URL não encontrados. Por favor, configure as secrets no GitHub.",
                size=20,
                color=ft.colors.RED_500
            )
        )
        page.update()
        return

    provider = GoogleOAuthProvider(
        client_id=client_id,
        client_secret=client_secret,
        redirect_url=redirect_url
    )

    def logingoogle(e):
        page.login(provider)

    def on_login(e):
        if page.auth.user:
            print("Login bem-sucedido! Navegando para /inicial")
            page.go("/inicial")
        else:
            print("Login falhou.")
            page.go("/")

    def on_logout(e):
        page.go("/login")
        page.logout()

    page.on_login = on_login
    page.on_logout = on_logout

    def mudar_tela(route):
        print(f"Rota atual: {page.route}")
        page.views.clear()

        # Adiciona a view de acordo com a rota
        if page.route == "/inicial":
            print("Carregando paginaInicio...")
            page.views.append(paginaInicio(page))
        elif page.route == "/descanso":
            print("Carregando paginaDescanso...")
            page.views.append(paginaDescanso(page))
        elif page.route == "/treino":
            print("Carregando paginaTreino...")
            page.views.append(paginaTreino(page))
        elif page.route == "/acabou":
            print("Carregando paginaAcabou...")
            page.views.append(paginaAcabou(page))
        elif page.route == "/alterarTreino":
            print("Carregando alterarTreino...")
            page.views.append(paginaAlterarTreino(page))
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
                            height = 40,
                            on_click=logingoogle,
                            alignment = ft.alignment.center
                        ),
                    ],
                    vertical_alignment= ft.MainAxisAlignment.CENTER,
                    horizontal_alignment= ft.CrossAxisAlignment.CENTER
                )
            )

        page.update()

    page.on_route_change = mudar_tela
    mudar_tela(page.route)

ft.app(target=main, assets_dir="assets")
