import streamlit as st

# Configurações iniciais
st.set_page_config(page_title="Escola Ursula Benincasa 2026", layout="centered")

# Estilo para as cores do colégio
st.markdown("""
    <style>
    .stApp { background-color: #f0f8ff; }
    h1, h2, h3 { color: #003366; }
    </style>
    """, unsafe_allow_html=True)

st.title("Reunião Pedagógica 2026")
st.write("### Escola Ursula Benincasa - Irmãs Teatinas")
st.write("*'Sem outra regra além do amor'* — Madre Úrsula Benincasa") [cite: 89, 90]

tab1, tab2, tab3, tab4 = st.tabs(["Institucional", "Rotina", "Avaliação", "Eventos"])

with tab1:
    st.header("Nossa História")
    st.write("Fundada em Nápoles, Itália, por Madre Ursula Benincasa em 1583.") [cite: 12]
    st.write("Mantida pela Associação das Irmãs Teatinas (desde 1973).") [cite: 10, 11]
    
    st.subheader("Equipe")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.write("**Irmã Olinda**")
        st.caption("Diretora") [cite: 6, 7]
    with col2:
        st.write("**Ingrit Candido**")
        st.caption("Coord. Fund 2 e Integral") [cite: 4, 5]
    with col3:
        st.write("**Josiane Dellaqua**")
        st.caption("Coord. Ed. Infantil e Fund 1") [cite: 8, 9]

with tab2:
    st.header("Horários e Regras")
    st.info("Tolerância de 10 minutos para atrasos.") [cite: 63]
    
    # Tabela de horários
    horarios = {
        "Segmento": ["Fund. I e II (Manhã)", "Fund. I (Tarde)", "Ed. Infantil (Tarde)"],
        "Horário": ["07h25 às 12h10", "13h às 17h35", "13h às 17h15"]
    }
    st.table(horarios) [cite: 61, 62]

    st.subheader("Avisos Gerais")
    st.markdown("""
    * **Uniforme:** Obrigatório e com nome em todas as peças. [cite: 22]
    * **Medicação:** Apenas com receita médica e autorização. [cite: 42]
    * **Brinquedo:** Sextas-feiras (Infantil/Fund 1). Proibido eletrônicos. [cite: 43, 44, 45]
    """)

with tab3:
    st.header("Sistema de Avaliação")
    st.write("Média do Bimestre: **6.0**") [cite: 67]
    st.write("Média Final para Aprovação: **24.0**") [cite: 68, 69]
    
    st.latex(r'''\text{Média} = \frac{P1 (\text{Formativa}) + P2 (\text{Prova})}{2}''') [cite: 75, 78, 79]
    
    st.write("Consulte notas em: [notasonline.com](http://www.notasonline.com)") [cite: 71]

with tab4:
    st.header("Aulas de Campo")
    st.write("Experiências em museus, teatros e parques.") [cite: 82]
    st.warning("Autorização prévia dos pais é obrigatória.") [cite: 84]
