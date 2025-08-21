# Para rodar este código, primeiro instale as bibliotecas necessárias.
# Abra o terminal e execute:
# pip install pandas openpyxl

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

