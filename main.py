import flet as ft
from flet.auth.providers import GoogleOAuthProvider
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente
load_dotenv(encoding='utf-8')

client_id = os.getenv('ID')
client_secret = os.getenv('SECRET_ID')
redirect_url = os.getenv('REDIRECT_URL')

def main(page: ft.Page):
    print('Iniciando página') ################## INICIANDO PAGINA #######################
    page.title = "Login"
    page.go("/")

    # Verifica se as secrets foram carregadas corretamente
    print(client_id)
    if not client_id or not client_secret or not redirect_url:
        print("Erro: Variáveis de ambiente não carregadas.")
        page.add(
            ft.Text(
                "Erro de configuração: ID, SECRET_ID ou REDIRECT_URL não encontrados. Configure as secrets no GitHub.",
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

    textresult = ft.Column()

    def login_google(e):
        print('INDO PARA O LOGIN GOOGLE') ################## INDO PARA O LOGIN GOOGLE #######################
        page.login(provider)

    def on_login(e):
        print('VERIFICANDO O LOGIN GOOGLE') ################## VERIFICANDO O LOGIN GOOGLE #######################
        if page.auth.user:
            textresult.controls.clear()
            print(page.auth.user)
            textresult.controls.append(ft.Text(f"nome: {page.auth.user['name']}"))
            textresult.controls.append(ft.Text(f"e-mail: {page.auth.user['email']}"))
            textresult.controls.append(ft.Text(f"sub: {page.auth.user['sub']}"))
            textresult.controls.append(ft.CircleAvatar(
                foreground_image_src=page.auth.user['picture'],
                content=ft.Text(page.auth.user['given_name']),
            ))
            textresult.controls.append(ft.CircleAvatar(
                content=ft.Text(page.auth.user['given_name']),
            ))
            # Adiciona botão de logoff
            textresult.controls.append(ft.ElevatedButton("Logoff", on_click=logoff))
            print("Login bem-sucedido!")
            page.update()
        else:
            textresult.controls.clear()
            textresult.controls.append(ft.Text("Login falhou."))
            print("Login falhou.")
            page.update()

    def on_logout(e):
        print('FAZENDO LOGOUT GOOGLE') ################## FAZENDO LOGOUT GOOGLE #######################
        page.logout()
        textresult.controls.clear()
        textresult.controls.append(ft.Text("Usuário deslogado."))
        textresult.controls.append(ft.ElevatedButton("Login", on_click=logingoogle))
        page.update()

    page.on_login = on_login
    page.on_logout = on_logout

    def mudar_tela(route):
        print(f"Rota atual: {page.route}")
        page.views.clear()
        
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
                            src='https://img.icons8.com/?size=512&id=17949&format=png'  # imagem local
                        ),
                        height=40,
                        on_click=login_google,
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
