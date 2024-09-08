# Análise da Carga Tributária no Brasil (1994 - 2022)

Este repositório contém um código em Python para análise da evolução da carga tributária no Brasil, expressa como porcentagem do PIB, desde a implementação do Plano Real em 1994 até 2022. A análise utiliza dados disponibilizados em uma planilha Excel que acompanha o projeto.

## Objetivo

O objetivo deste projeto é visualizar a evolução da carga tributária no Brasil e identificar os principais momentos de alta e baixa arrecadação ao longo das últimas três décadas. Isso é feito por meio de um gráfico que mostra a carga tributária como percentual do PIB, a partir de dados coletados anualmente.

## Fonte de Dados

Os dados utilizados neste projeto foram obtidos da série histórica de carga tributária no Brasil, disponível no [Observatório de Política Fiscal](https://observatorio-politica-fiscal.ibre.fgv.br/series-historicas/carga-tributaria/carga-tributaria-no-brasil-1990-2022), mantido pelo Instituto Brasileiro de Economia da Fundação Getulio Vargas (FGV IBRE).

## Requisitos

Para executar o código, você precisará dos seguintes pacotes Python:

- `pandas`
- `matplotlib`

Para instalar as dependências, execute:

```bash
pip install pandas matplotlib
````

## Estrutura do Repositório
`ctb_1990-2022.xlsx:` Arquivo de dados em Excel contendo as receitas tributárias do Brasil, em R$ milhões e como porcentagem do PIB.
`main.py:` Script Python que carrega, processa e plota a evolução da carga tributária em % do PIB.

## Como Executar
Clone este repositório ou baixe os arquivos.
Certifique-se de que o arquivo ctb_1990-2022.xlsx esteja no mesmo diretório do script main.py.
Execute o script:
```bash
python main.py
```
O script irá gerar um gráfico da evolução da carga tributária (% do PIB) no Brasil de 1994 a 2022.

## Explicação do Código
O código realiza as seguintes etapas:

- Leitura do arquivo Excel: A planilha contendo os dados de carga tributária é carregada usando pandas.
- Filtragem dos dados: O código filtra os dados para analisar o período entre 1994 (início do Plano Real) até 2022.
- Plotagem do gráfico: Utilizando matplotlib, o gráfico da carga tributária como % do PIB é gerado, mostrando a evolução anual.
