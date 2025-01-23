import os
os.system("pip install matplotlib")
import pandas as pd
import streamlit as st
import matplotlib
from matplotlib import pyplot as plt
#import matplotlib.pyplot as plt

# Carregar os dados da planilha gerada
arquivo_planilha = "relatorio_escolas_2025-01-22_17-45-41.xlsx"
df = pd.read_excel(arquivo_planilha)

st.image("cr.jpeg")

# Configuração do título da aplicação
st.markdown(
    """
    <div style='text-align: center; font-size: 32px; font-weight: bold;'>
        Relatório da Avaliação Socioemocional por Escola
    </div>
    """,
    unsafe_allow_html=True,
)

#st.title("Relatório Socioemocional por Escola - CREDE 01")

st.markdown(
    """
    <div style='text-align: justify; font-size: 18px; line-height: 1.6;'>
        Aqui você pode visualizar, de forma clara e interativa, as porcentagens 
        das aplicações da avaliação socioemocional por escola para cada série.
    </div>
    """,
    unsafe_allow_html=True,
)

# Criar lista suspensa para selecionar escola
escola_selecionada = st.selectbox(
    "Pesquise ou selecione uma escola:",
    options=df["NOME DA ESCOLA"],
    format_func=lambda x: f"{x}"  # O `format_func` mantém o texto original
)

#escolas = df["NOME DA ESCOLA"].unique()
#escola_selecionada = st.selectbox("Escolha a escola", escolas)

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
ax.set_ylim(0, 130)
ax.set_yticks([]) #retira os números do eixo y
# Adicionar rótulos acima das barras
for i, v in enumerate(valores):
    ax.text(i, v + 1, f"{v:.1f}%", ha="center")

# Mostrar o gráfico no Streamlit
st.pyplot(fig)

# Exibir tabela de dados da escola (opcional)
st.write("Dados detalhados:")
st.dataframe(dados_escola)

st.image("pdt1.png",  width=300)


