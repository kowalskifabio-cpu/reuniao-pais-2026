import streamlit as st

# Configuração da página
st.set_page_config(page_title="Escola Ursula Benincasa 2026", layout="wide")

# Estilo para cores do colégio
st.markdown("""
    <style>
    .stApp { background-color: #fdfdfd; }
    h1, h2, h3 { color: #0056b3; }
    .stTabs [data-baseweb="tab-list"] { gap: 24px; }
    </style>
    """, unsafe_allow_html=True)

# Título Principal
st.title("Reunião Pedagógica 2026")
st.write("### Escola Ursula Benincasa — Irmãs Teatinas")
st.info("'Sem outra regra além do amor' — Madre Úrsula Benincasa")

# Organização por Abas
tab1, tab2, tab3, tab4 = st.tabs(["🏛️ Institucional", "📅 Rotina e Horários", "📊 Avaliação", "🚌 Eventos"])

with tab1:
    st.header("Nossa Identidade")
    [cite_start]st.write("Fundada em Nápoles (1583) pela Madre Ursula Benincasa[cite: 12].")
    [cite_start]st.write("Mantida pela Associação das Irmãs Teatinas da Imaculada Conceição desde 1973[cite: 10, 11].")
    
    st.subheader("Equipe Diretiva")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("Irmã Olinda")
        [cite_start]st.caption("Diretora [cite: 6, 7]")
    with col2:
        st.subheader("Ingrit Candido")
        [cite_start]st.caption("Coordenadora Fundamental 2 e Integral Manhã [cite: 4, 5]")
    with col3:
        st.subheader("Josiane Dellaqua")
        [cite_start]st.caption("Coordenadora Educação Infantil, Fundamental 1 e Integral Tarde [cite: 8, 9]")

with tab2:
    st.header("Horários e Regras")
    col_h1, col_h2 = st.columns(2)
    with col_h1:
        st.markdown("**Período da Manhã**")
        [cite_start]st.write("07h25 às 12h10 (Fundamental I e II) [cite: 61]")
    with col_h2:
        st.markdown("**Período da Tarde**")
        [cite_start]st.write("13h às 17h15 (Educação Infantil) [cite: 62]")
        [cite_start]st.write("13h às 17h35 (Fundamental I) [cite: 62]")
    
    [cite_start]st.warning("Tolerância de 10 minutos para atrasos. Após isso, entrada apenas na 2ª aula[cite: 63].")

with tab3:
    st.header("Sistema de Avaliação")
    [cite_start]st.write("Média do Bimestre: **6.0** [cite: 67]")
    [cite_start]st.write("Aprovação Final: **24.0 pontos** [cite: 68, 69]")
    st.markdown("""
    * [cite_start]**P1 (10,0 pts):** Atividades formativas, trabalhos e pesquisas[cite: 76].
    * [cite_start]**P2 (10,0 pts):** Prova bimestral[cite: 77].
    """)
    [cite_start]st.link_button("Acessar Notas Online", "http://www.notasonline.com") [cite: 71]

with tab4:
    st.header("Saídas Pedagógicas")
    [cite_start]st.write("Objetivo: Ampliar a aprendizagem com experiências concretas (museus, teatros, parques)[cite: 81, 82].")
    [cite_start]st.error("Obrigatória a autorização prévia dos pais para participação[cite: 84].")
