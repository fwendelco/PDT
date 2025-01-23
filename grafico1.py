import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Carregar os dados da planilha gerada
arquivo_planilha = "relatorio_escolas_2025-01-22_10-30-13.xlsx"
df = pd.read_excel(arquivo_planilha)

# Configuração do título da aplicação
st.title("Relatório Socioemocional por Escola")
st.write("Selecione uma escola para visualizar os dados.")

# Criar lista suspensa para selecionar escola
escolas = df["NOME DA ESCOLA"].unique()
escola_selecionada = st.selectbox("Escolha a escola", escolas)

# Filtrar os dados da escola selecionada
dados_escola = df[df["NOME DA ESCOLA"] == escola_selecionada]

# Preparar os dados para o gráfico
series = ["1ª Série", "2ª Série", "3ª Série"]
valores = [
    float(dados_escola[serie].values[0].replace("%", "")) if serie in dados_escola.columns and isinstance(dados_escola[serie].values[0], str) else 0
    for serie in series
]

# Criar gráfico de barras
fig, ax = plt.subplots()
ax.bar(series, valores, color=["blue", "orange", "green"])
ax.set_title(f"Porcentagens para {escola_selecionada}")
ax.set_ylabel("Porcentagem")
ax.set_ylim(0, 100)

# Adicionar rótulos acima das barras
for i, v in enumerate(valores):
    ax.text(i, v + 1, f"{v:.1f}%", ha="center")

# Mostrar o gráfico no Streamlit
st.pyplot(fig)

# Exibir tabela de dados da escola (opcional)
st.write("Dados detalhados:")
st.dataframe(dados_escola)

