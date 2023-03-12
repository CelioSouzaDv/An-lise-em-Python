# -*- coding: utf-8 -*-
"""Projeto1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uHZujYDDVImoXZCyHg-anlYeuXNIX20n
"""

# Primeiro projeto prático utilizando a linguagem Python para análise de dados;

# Utilizando as tabelas com dados relacionados a VENDAS, irei compilar e estrair os dados necessários para a análise;

# As informações serão: Protudos mais vendidos, Produto que mais faturou e a loja/cidade que mais vendeu;

# Com base nas informações/dados extraidos das tabelas foi criado um Dashboard informativo com os resultados.

import os
import pandas as pd
import plotly.express as px

list_itens = os.listdir('/content/drive/MyDrive/Estudos Programação/Vendas')
display(list_itens)

new_table = pd.DataFrame()
for itens in list_itens:
    if 'Vendas' in itens:
        table = pd.read_csv(f'/content/drive/MyDrive/Estudos Programação/Vendas/{itens}')
        new_table = new_table.append(table)
        
display(new_table)

product_table = new_table.groupby('Produto').sum()
product_table = product_table[['Quantidade Vendida', 'Faturamento']].sort_values(by='Quantidade Vendida', ascending=False)
display(product_table)

new_table['Faturamento'] = new_table['Quantidade Vendida']* new_table['Preco Unitario']
invoicing_table = new_table.groupby('Produto').sum()
invoicing_table = invoicing_table [['Faturamento']].sort_values(by='Faturamento', ascending=False)
display(invoicing_table)

store_table = new_table.groupby('Loja').sum()
store_table = store_table[['Faturamento']].sort_values(by='Faturamento', ascending=False)
display(store_table)

graph = px.bar(store_table, x=store_table.index, y='Faturamento')
graph.show()