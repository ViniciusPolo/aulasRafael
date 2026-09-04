import pandas as pd
import numpy as np

# Configuração só para exibir mais colunas/linhas no notebook, sem cortar com "..."
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 120)

print("Versão do pandas:", pd.__version__)

import os
print(os.getcwd())

# Exemplo simples só para fixar o conceito, sem depender de arquivo nenhum
serie = pd.Series([10, 20, 30], name="idade")
print(serie)
print("------")
print(type(serie))

df_exemplo = pd.DataFrame({
    "nome": ["Ana", "Bruno", "Carla"],
    "idade": [23, 35, 29],
    "peso": [55, 98, 75]
})
print(df_exemplo)  # em notebook, retornar o DataFrame na última linha já exibe como tabela

caminho = "~/Documents/superProf/aulaPandas/vendas_exemplo.xlsx"  # ajuste o caminho se o arquivo estiver em outra pasta

df = pd.read_excel(caminho, sheet_name="Vendas")  # sheet_name é opcional se só tiver uma aba
print(df)

print(df.shape)  # (número de linhas, número de colunas)
print(df.head())  # primeiras 5 linhas (pode passar um número, ex: df.head(10))
print(df.info()) 
print(df.describe()) 
print(df.dtypes )

# Uma coluna -> vira uma Series
print(df["Cliente"])    

print(df[["Cliente", "Produto", "Preco_Unitario"]])

print(df.loc[4:9, ["Cliente", "Produto"]])  # linhas de índice 0 a 4, só essas colunas

print(df[df["Produto"] == "Notebook"])

# Combinando condições: & é "e", | é "ou" -- SEMPRE use parênteses em cada condição
print(df[(df["Produto"] == "Monitor") & (df["Estado"] == "MG")])