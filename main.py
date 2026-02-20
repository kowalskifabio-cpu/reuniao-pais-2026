import streamlit as st

# Configuração da página para um visual imersivo
st.set_page_config(
    page_title="Reunião Pedagógica 2026 - Escola Ursula Benincasa",
    page_icon="🏫",
    layout="wide"
)

# Estilização CSS Avançada
st.markdown("""
    <style>
    /* Fundo e Fonte Geral */
    .stApp { background-color: #F0F7FF; }
    
    /* Títulos e Cores */
    h1, h2, h3 { color: #004A99; font-family: 'Comic Sans MS', cursive, sans-serif; }
    
    /* Efeito Circular nas Fotos */
    .img-circular {
        border-radius: 50%;
        border: 5px solid #004A99;
        object-fit: cover;
        width: 200px;
        height: 200px;
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
    
    /* Estilização dos Cards */
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        text-align: center;
        margin-bottom: 20px;
    }
    
    /* Abas Coloridas */
    .stTabs [data-baseweb="tab-list"] { gap: 8px; }
    .stTabs [data-baseweb="tab"] {
        background-color: #D1E9FF;
        border-radius: 10px 10px 0 0;
        padding: 10px 20px;
        color: #004A99;
    }
    .stTabs [data-baseweb="tab"]:focus { color: #004A99; }
    </style>
    """, unsafe_allow_html=True)

# --- CABEÇALHO ---
col_l, col_t = st.columns([1, 4])
with col_l:
    st.image("logo.jpg", width=160)
with col_t:
    st.title("Reunião Pedagógica 2026") [cite: 1, 2]
    st.subheader("Escola Ursula Benincasa — Irmãs Teatinas") [cite: 11]

st.markdown("---")

# --- ABAS DE CONTEÚDO 100% ---
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🏠 Institucional", "👨‍👩‍👧‍👦 Equipe", "📅 Rotina & Avisos", "⏰ Horários", "📊 Avaliação", "🚌 Projetos"
])

with tab1:
    st.header("Nossa Identidade") [cite: 13]
    col_hist1, col_hist2 = st.columns(2)
    with col_hist1:
        st.write("### 🌍 Congregação")
        st.write("Fundada em Nápoles, Itália, pela Madre Ursula Benincasa no ano de 1583.") [cite: 12]
    with col_hist2:
        st.write("### 🇧🇷 Mantenedora")
        st.write("Associação das Irmãs Teatinas da Imaculada Conceição: Fundada em 21/07/1973.") [cite: 11]
    
    st.success("**Proposta Pedagógica:** Centrada no desenvolvimento dos valores humanos: Solidariedade, Respeito, Justiça e Diálogo.") [cite: 14, 15, 16, 17, 18]
    st.write("*Estes são princípios a serem seguidos por todos: Professores, Alunos, Funcionários, Diretores, Coordenadores e Pais/Responsáveis.*") [cite: 19, 20]

with tab2:
    st.header("Carômetro") [cite: 3]
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        # Como não há foto da Irmã Olinda no repositório, usamos a logo
        st.markdown('<img src="https://raw.githubusercontent.com/kowalskifabio-cpu/reuniao-pais-2026/main/logo.jpg" class="img-circular">', unsafe_allow_html=True)
        st.write("### Irmã Olinda") [cite: 6]
        st.write("**Diretora**") [cite: 7]
        st.markdown('</div>', unsafe_allow_html=True)

    with c2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<img src="https://raw.githubusercontent.com/kowalskifabio-cpu/reuniao-pais-2026/main/Ingrit.jpg" class="img-circular">', unsafe_allow_html=True)
        st.write("### Ingrit Candido") [cite: 4]
        st.write("**Coordenadora Fundamental 2 e Integral Manhã**") [cite: 5]
        st.markdown('</div>', unsafe_allow_html=True)

    with c3:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<img src="https://raw.githubusercontent.com/kowalskifabio-cpu/reuniao-pais-2026/main/Josi.jpg" class="img-circular">', unsafe_allow_html=True)
        st.write("### Josiane Dellaqua") [cite: 8]
        st.write("**Coordenadora Ed. Infantil, Fundamental 1 e Integral Tarde**") [cite: 9]
        st.markdown('</div>', unsafe_allow_html=True)

with tab3:
    st.header("Orientações e Avisos Gerais") [cite: 21]
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.write("### 👕 Uniforme")
        st.write("Estar devidamente uniformizado e colocar nome em todas as peças. Não serão permitidas outras cores.") [cite: 22]
        
        st.write("### 📚 Biblioteca e Literatura") [cite: 23]
        st.write("- Dia fixo na semana para empréstimo.") [cite: 24]
        st.write("- Devolução quinzenal.") [cite: 25]
        st.write("- **Multas:** Infantil/Fund I (por semana); Fund II (R$ 4,00 por dia).") [cite: 27, 28]
        
        st.write("### 🍎 Alimentação")
        st.write("- Tempo de lanche: 15 minutos.") [cite: 49]
        st.write("- Orientamos o envio de lanche adequado e saudável.") [cite: 50]
    
    with col_b:
        st.write("### 💊 Medicação")
        st.write("Somente mediante receita médica e autorização assinada.") [cite: 42]
        
        st.write("### 🧸 Dia do Brinquedo (Sexta-feira)") [cite: 43, 44]
        st.write("- Proibido eletrônicos ou bolas.") [cite: 45]
        st.write("- Incentivar o compartilhar e a convivência coletiva.") [cite: 47]
        
        st.write("### 🎂 Aniversários (Infantil e Fund I)") [cite: 53]
        st.write("Kits individuais com agendamento via agenda e secretaria.") [cite: 54, 55, 56]

with tab4:
    st.header("Horários e Pontualidade") [cite: 39, 59]
    st.write("Pedimos a colaboração quanto ao cumprimento dos horários para organização da rotina.") [cite: 60]
    
    col_h1, col_h2 = st.columns(2)
    with col_h1:
        st.info("### ☀️ Manhã\n**07h25 às 12h10**\nFundamental I e II") [cite: 61]
    with col_h2:
        st.info("### 🌤️ Tarde\n**13h às 17h35** (Fund I)\n**13h às 17h15** (Ed. Infantil)") [cite: 62]
    
    st.warning("⚠️ **Tolerância:** 10 minutos. Após isso, o aluno ingressa apenas na 2ª aula. Atrasos maiores exigem atestado médico.") [cite: 63, 64]

with tab5:
    st.header("Sistema de Avaliação") [cite: 65, 74]
    st.write("### Ensino Fundamental (1º ao 9º ano)") [cite: 66]
    
    col_m1, col_m2 = st.columns(2)
    with col_m1:
        st.metric("Média Bimestral", "6.0") [cite: 67]
    with col_m2:
        st.metric("Média Final para Aprovação", "24.0") [cite: 68, 69]

    st.write("#### Composição da Média:") [cite: 75]
    st.latex(r'''\text{Média} = \frac{P1 (\text{Atividades Formativas}) + P2 (\text{Prova Bimestral})}{2}''') [cite: 76, 77, 78, 79]
    
    st.write("---")
    st.write("### 💻 Sistema Notas Online") [cite: 70]
    st.write("**Acesse:** [www.notasonline.com](http://www.notasonline.com)") [cite: 71]
    st.write("Registros de: Notas, Calendário, Ocorrências, Lição de Casa e Uniforme.") [cite: 72, 73]

with tab6:
    st.header("Projetos e Inovações")
    
    st.write("### 🚌 Aula de Campo") [cite: 80]
    st.write("Visitas a teatros, museus e parques para ampliar a aprendizagem concreta.") [cite: 81, 82]
    st.write("- Acompanhamento de professores e segurança garantida.") [cite: 83]
    st.write("- **Autorização prévia obrigatória.**") [cite: 84]
    
    st.write("---")
    st.write("### 🧠 Sala de Recursos (Neurodivergentes)") [cite: 86]
    st.write("**Previsão de Inauguração:** Julho de 2026.") [cite: 87]

# --- RODAPÉ ---
st.markdown("---")
st.markdown(
    "<h2 style='text-align: center;'>“SEM OUTRA REGRA ALÉM DO AMOR”</h2>", 
    unsafe_allow_html=True
) [cite: 88, 89]
st.markdown("<p style='text-align: center;'>Madre Úrsula Benincasa</p>", unsafe_allow_html=True) [cite: 90]
