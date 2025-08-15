import flet as ft
from inicio import paginaInicio
import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente
load_dotenv(encoding='utf-8')


def main(page: ft.Page):
    print('Iniciando página') ################## INICIANDO PAGINA #######################
    page.title = "Login"
    page.go("/")

    # Verifica se as secrets foram carregadas corretamente
  
    textresult = ft.Column()

    def login_google(e):
        print('INDO PARA O LOGIN GOOGLE') ################## INDO PARA O LOGIN GOOGLE #######################
        page.go("/inicial")
        print("Navagando para inicio")
      

    def on_login(e):
        print('VERIFICANDO O LOGIN GOOGLE') ################## VERIFICANDO O LOGIN GOOGLE #######################
       

    def on_logout(e):
        print('FAZENDO LOGOUT GOOGLE') ################## FAZENDO LOGOUT GOOGLE #######################
        textresult.controls.clear()
        textresult.controls.append(ft.Text("Usuário deslogado."))
        page.update()

    page.on_login = on_login
    page.on_logout = on_logout

    def mudar_tela(route):
        print(f"Rota atual: {page.route}")
        page.views.clear()
        
        if page.route == "/inicial":
            print("Carregando paginaInicio...")
            try:
                page.views.append(paginaInicio(page))
            except Exception as e:
                print(f"Erro ao carregar paginaInicio: {e}")
                page.views.append(ft.Text(f"Erro ao carregar paginaInicio: {e}"))
        else:
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
