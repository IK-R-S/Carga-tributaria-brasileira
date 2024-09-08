# Importando as bibliotecas necessárias
import pandas as pd
import matplotlib.pyplot as plt

# Carregar a planilha de dados
# FONTE DE DADOS: https://observatorio-politica-fiscal.ibre.fgv.br/series-historicas/carga-tributaria/carga-tributaria-no-brasil-1990-2022
file_path = './ctb_1990-2022.xlsx'
xls = pd.ExcelFile(file_path)

# Carregar as planilhas de interesse
ctb_pib_percentage = pd.read_excel(xls, sheet_name='CTB (% do PIB)')

# Limpar e organizar os dados para análise a partir de 1994
ctb_pib_filtered = ctb_pib_percentage.iloc[2:, 1:].set_index(ctb_pib_percentage.iloc[2:, 0])
ctb_pib_filtered.columns = [str(int(float(year))) for year in ctb_pib_percentage.iloc[1, 1:]]
ctb_pib_filtered = ctb_pib_filtered.loc[:, "1994":"2022"].apply(pd.to_numeric, errors='coerce')

# Plotar a evolução da carga tributária (Total da Receita Tributária) em % do PIB de 1994 a 2022
plt.figure(figsize=(10, 6))
plt.plot(ctb_pib_filtered.columns, ctb_pib_filtered.loc['Total da Receita Tributária'], marker='o', label="Total da Receita Tributária (% do PIB)")

# Configurar os títulos e rótulos do gráfico
plt.title("Evolução da Carga Tributária no Brasil (% do PIB) de 1994 a 2022", fontsize=14)
plt.xlabel("Ano", fontsize=12)
plt.ylabel("Carga Tributária (% do PIB)", fontsize=12)
plt.grid(True)
plt.xticks(rotation=45)
plt.legend()

# Exibir o gráfico
plt.tight_layout()
plt.show()
