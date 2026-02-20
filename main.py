import streamlit as st

# Configuração da página para um visual mais profissional
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
    [cite_start]st.image("logo.jpg", width=150) [cite: 1, 3]
with col_titulo:
    [cite_start]st.title("Reunião Pedagógica 2026") [cite: 1, 2]
    [cite_start]st.subheader("Escola Ursula Benincasa — Irmãs Teatinas") [cite: 1]

[cite_start]st.info("**Regra de Ouro:** 'Sem outra regra além do amor' — Madre Úrsula Benincasa") [cite: 12, 89, 90]

# Abas de Navegação
tab_inst, tab_rotina, tab_aval, tab_campo = st.tabs([
    "🏛️ Institucional", "⏰ Rotina Escolar", "📊 Sistema de Avaliação", "🚌 Saídas Pedagógicas"
])

with tab_inst:
    st.header("Nossa Identidade")
    [cite_start]st.write("A Congregação foi fundada em Nápoles, Itália, pela Madre Ursula Benincasa no ano de 1583[cite: 12]. [cite_start]A Associação das Irmãs Teatinas da Imaculada Conceição foi fundada em 21/07/1973[cite: 11].")
    
    st.markdown("---")
    st.subheader("Equipe Diretiva e Coordenação")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.image("logo.jpg", width=200) # Representando a Direção
        [cite_start]st.write("**Irmã Olinda**") [cite: 6]
        [cite_start]st.caption("Diretora") [cite: 7]
    with c2:
        st.image("Ingrit.jpg", width=200)
        [cite_start]st.write("**Ingrit Candido**") [cite: 4]
        [cite_start]st.caption("Coordenadora Fundamental 2 e Integral Manhã") [cite: 5]
    with c3:
        st.image("Josi.jpg", width=200)
        [cite_start]st.write("**Josiane Dellaqua**") [cite: 8]
        [cite_start]st.caption("Coordenadora Educação Infantil, Fundamental 1 e Integral Tarde") [cite: 9]

with tab_rotina:
    st.header("Horários e Organização")
    
    col_h1, col_h2 = st.columns(2)
    with col_h1:
        st.markdown("### ☀️ Período da Manhã")
        [cite_start]st.write("**Fundamental I e II:** 07h25 às 12h10") [cite: 61]
    with col_h2:
        st.markdown("### 🌤️ Período da Tarde")
        [cite_start]st.write("**Fundamental I:** 13h às 17h35") [cite: 62]
        [cite_start]st.write("**Educação Infantil:** 13h às 17h15") [cite: 62]
    
    [cite_start]st.warning("⚠️ Há tolerância de 10 minutos para atrasos. Após esse período, o aluno poderá ingressar apenas na 2ª aula[cite: 63].")
    
    st.markdown("---")
    st.subheader("Avisos Gerais")
    st.markdown(f"""
    * [cite_start]**Uniforme:** Deve estar devidamente uniformizado e colocar nome em todas as peças[cite: 22].
    * [cite_start]**Medicação:** A escola administrará somente mediante receita médica e autorização assinada[cite: 42].
    * **Dia do Brinquedo:** Sexta-feira (Ed. Infantil e Fund. I). [cite_start]Proibido eletrônicos ou bolas[cite: 43, 44, 45].
    * [cite_start]**Lanche:** Tempo de 15 minutos; orientamos o envio de lanche saudável[cite: 49, 50].
    * [cite_start]**Biblioteca:** Empréstimos semanais; devolução quinzenal[cite: 24, 25].
    """)

with tab_aval:
    st.header("Sistema de Avaliação")
    [cite_start]st.write("Ensino Fundamental (1º ao 9º ano)") [cite: 66]
    
    col_n1, col_n2 = st.columns(2)
    with col_n1:
        [cite_start]st.metric("Média do Bimestre", "6.0") [cite: 67]
    with col_n2:
        [cite_start]st.metric("Média Final (Aprovação)", "24.0") [cite: 68]
    
    st.markdown("#### Composição da Nota Bimestral:")
    [cite_start]st.latex(r'''\text{Média} = \frac{P1 (\text{Atividades Formativas}) + P2 (\text{Prova Bimestral})}{2}''') [cite: 75, 76, 77, 78, 79]
    
    [cite_start]st.info("O descumprimento de regras (atrasos, material incompleto, desrespeito) é registrado no sistema[cite: 73].")
    [cite_start]st.link_button("Acessar Notas Online", "http://www.notasonline.com") [cite: 71]

with tab_campo:
    st.header("Aulas de Campo e Saídas Pedagógicas")
    [cite_start]st.write("As saídas visam ampliar a aprendizagem por meio de experiências concretas em teatros, museus, parques e outros[cite: 81, 82].")
    
    st.markdown("""
    * [cite_start]**Segurança:** Acompanhadas por professores e funcionários[cite: 83].
    * [cite_start]**Autorização:** É obrigatória a autorização prévia dos pais ou responsáveis[cite: 84].
    * [cite_start]**Custos:** Valores de transporte ou ingressos serão informados previamente[cite: 85].
    """)
    
    if st.button("Verificar Sala de Recursos (Neurodivergentes)"):
        [cite_start]st.write("Previsão para Julho[cite: 86, 87].")
