import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Reunião de Pais 2026 - Escola Ursula Benincasa",
    page_icon="📚",
    layout="wide"
)

# Estilização Personalizada (CSS)
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    h1, h2 { color: #004a99; font-family: 'Helvetica', sans-serif; }
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] {
        background-color: #e1f0ff;
        border-radius: 5px;
        padding: 8px 16px;
    }
    </style>
    """, unsafe_allow_html=True)

# Cabeçalho com Logo
col_logo, col_titulo = st.columns([1, 4])
with col_logo:
    st.image("logo.jpg", width=150)
with col_titulo:
    st.title("Reunião Pedagógica 2026")
    st.subheader("Escola Ursula Benincasa — Irmãs Teatinas")

st.info("**Regra de Ouro:** 'Sem outra regra além do amor' — Madre Úrsula Benincasa")

# Abas de Navegação
tab_inst, tab_rotina, tab_aval, tab_campo = st.tabs([
    "🏛️ Institucional", "⏰ Rotina Escolar", "📊 Sistema de Avaliação", "🚌 Saídas Pedagógicas"
])

with tab_inst:
    st.header("Nossa Identidade")
    st.write("A Congregação foi fundada em Nápoles, Itália, pela Madre Ursula Benincasa no ano de 1583. A Associação das Irmãs Teatinas da Imaculada Conceição foi fundada em 21/07/1973.")
    
    st.markdown("---")
    st.subheader("Equipe Diretiva e Coordenação")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.image("logo.jpg", width=200)
        st.write("**Irmã Olinda**")
        st.caption("Diretora")
    with c2:
        st.image("Ingrit.jpg", width=200)
        st.write("**Ingrit Candido**")
        st.caption("Coordenadora Fundamental 2 e Integral Manhã")
    with c3:
        st.image("Josi.jpg", width=200)
        st.write("**Josiane Dellaqua**")
        st.caption("Coordenadora Educação Infantil, Fundamental 1 e Integral Tarde")

with tab_rotina:
    st.header("Horários e Organização")
    
    col_h1, col_h2 = st.columns(2)
    with col_h1:
        st.markdown("### ☀️ Período da Manhã")
        st.write("**Fundamental I e II:** 07h25 às 12h10")
    with col_h2:
        st.markdown("### 🌤️ Período da Tarde")
        st.write("**Fundamental I:** 13h às 17h35")
        st.write("**Educação Infantil:** 13h às 17h15")
    
    st.warning("⚠️ Há tolerância de 10 minutos para atrasos. Após esse período, o aluno poderá ingressar apenas na 2ª aula.")
    
    st.markdown("---")
    st.subheader("Avisos Gerais")
    st.markdown("""
    * **Uniforme:** Deve estar devidamente uniformizado e colocar nome em todas as peças.
    * **Medicação:** A escola administrará somente mediante receita médica e autorização assinada.
    * **Dia do Brinquedo:** Sexta-feira (Ed. Infantil e Fund. I). Proibido eletrônicos ou bolas.
    * **Lanche:** Tempo de 15 minutos; orientamos o envio de lanche saudável.
    * **Biblioteca:** Empréstimos semanais; devolução quinzenal.
    """)

with tab_aval:
    st.header("Sistema de Avaliação")
    st.write("Ensino Fundamental (1º ao 9º ano)")
    
    col_n1, col_n2 = st.columns(2)
    with col_n1:
        st.metric("Média do Bimestre", "6.0")
    with col_n2:
        st.metric("Média Final (Aprovação)", "24.0")
    
    st.markdown("#### Composição da Nota Bimestral:")
    st.latex(r'''\text{Média} = \frac{P1 + P2}{2}''')
    
    st.info("O descumprimento de regras (atrasos, material incompleto, desrespeito) é registrado no sistema.")
    st.link_button("Acessar Notas Online", "http://www.notasonline.com")

with tab_campo:
    st.header("Aulas de Campo")
    st.write("As saídas visam ampliar a aprendizagem por meio de experiências concretas.")
    
    st.markdown("""
    * **Segurança:** Acompanhadas por professores e funcionários.
    * **Autorização:** É obrigatória a autorização prévia dos pais ou responsáveis.
    * **Custos:** Valores de transporte ou ingressos serão informados previamente.
    """)
