import flet as ft
import pandas as pd
import os


# --- Parte 1: Criar um arquivo Excel de exemplo ---
print("Criando um arquivo Excel de exemplo...")

# Dicionário de dados para criar a tabela
dados = {
    'Nome': ['João', 'Maria', 'Pedro', 'Ana'],
    'Idade': [25, 30, 35, 28],
    'Pontuacao': [85, 92, 78, 95]
}

# Criar um DataFrame (tabela) com os dados
df = pd.DataFrame(dados)

# Salvar o DataFrame em um arquivo Excel (.xlsx)
caminho_arquivo_original = 'dados_originais.xlsx'
df.to_excel(caminho_arquivo_original, index=False) # index=False para não salvar o índice do DataFrame
print(f"Arquivo '{caminho_arquivo_original}' criado com sucesso.\n")

# --- Parte 2: Ler e Alterar o arquivo Excel ---
print(f"Lendo o arquivo '{caminho_arquivo_original}'...")

# Ler o arquivo Excel usando pandas
try:
    df_lido = pd.read_excel(caminho_arquivo_original)
    print("Conteúdo original do arquivo:")
    print(df_lido)

    # Exemplo de alteração: Adicionar uma nova coluna 'Bonus'
    # Baseado na pontuação, vamos calcular um bônus de 10%
    df_lido['Bonus'] = df_lido['Pontuacao'] * 0.10
    print("\nConteúdo após a alteração (adicionando coluna 'Bonus'):")
    print(df_lido)
    
    # Exemplo de alteração de um valor específico:
    # Mudar a idade de 'João' para 26
    df_lido.loc[df_lido['Nome'] == 'João', 'Idade'] = 26
    print("\nConteúdo após alteração da idade de 'João':")
    print(df_lido)

    # --- Parte 3: Salvar as alterações em um novo arquivo ---
    caminho_arquivo_alterado = 'dados_alterados.xlsx'
    df_lido.to_excel(caminho_arquivo_alterado, index=False)
    print(f"\nAlterações salvas com sucesso em '{caminho_arquivo_alterado}'.")

except FileNotFoundError:
    print(f"Erro: O arquivo '{caminho_arquivo_original}' não foi encontrado.")
except Exception as e:
    print(f"Ocorreu um erro ao processar o arquivo: {e}")

def paginaInicio(page: ft.Page):
    page.title = "Treino Quest"
    page.horizontal_alignment = 'center'
    page.vertical_alignment = 'center'

    ft.ThemeMode.LIGHT

    def check_item_clicked(e):
        page.theme_mode = (
            ft.ThemeMode.LIGHT if page.theme_mode != ft.ThemeMode.LIGHT else ft.ThemeMode.DARK
        )
        page.update()


    def tela_Treino(e):
        print("Navegando para Treino")
        #page.go("/treino")

    leading_content = ft.Text("Login")


    def destino_selecionado(e):
        if rail.selected_index == 1:
            print("Alterar Treino selecionado!")
            # Aqui, execute a função relacionada ao treino
            #page.go("/alterarTreino")
            #page.update()


    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=10,
        min_extended_width=40,
        leading=leading_content,
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
        width=70,
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
                ft.VerticalDivider(width=5),
                ft.Column(
                    [
                        ft.ElevatedButton(
                            "Treino de Hoje",
                            style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=60),
                            elevation=2,
                            on_click = tela_Treino
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    expand=True
                )
            ],expand=True)
        ],
        appbar=appbar_inicio,
    )
