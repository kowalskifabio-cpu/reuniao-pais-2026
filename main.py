import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Reunião Pedagógica 2026 - Escola Ursula Benincasa",
    page_icon="🏫",
    layout="wide"
)

# Estilização CSS para fotos circulares e layout limpo
st.markdown("""
    <style>
    .stApp { background-color: #F0F7FF; }
    h1, h2, h3 { color: #004A99; font-family: 'Helvetica', sans-serif; margin-top: 0px; }
    
    .img-container {
        text-align: center;
        padding: 10px;
        margin-top: -10px;
    }
    
    .img-circular {
        border-radius: 50%;
        border: 4px solid #004A99;
        object-fit: cover;
        width: 180px;
        height: 180px;
        margin-bottom: 10px;
    }

    .nome-equipe { font-weight: bold; font-size: 1.2em; margin-bottom: 2px; }
    .cargo-equipe { font-size: 0.9em; color: #555; }
    </style>
    """, unsafe_allow_html=True)

# Cabeçalho
col_logo, col_titulo = st.columns([1, 4])
with col_logo:
    st.image("logo.jpg", width=140)
with col_titulo:
    st.title("Reunião Pedagógica 2026")
    st.subheader("Escola Ursula Benincasa — Irmãs Teatinas")

st.info("**Regra Máxima:** 'Sem outra regra além do amor' — Madre Úrsula Benincasa")

# Abas de Conteúdo
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🏠 Institucional", "👥 Equipe", "📅 Rotina Escolar", "📊 Avaliação", "🚌 Projetos"
])

with tab1:
    st.header("Identidade e Proposta")
    st.write("### 🌍 Origens")
    st.write("- **Congregação:** Fundada em Nápoles, Itália, pela Madre Ursula Benincasa em 1583.")
    st.write("- **Mantenedora:** Associação das Irmãs Teatinas da Imaculada Conceição, fundada em 21/07/1973.")
    
    st.write("### 💡 Proposta Pedagógica")
    st.write("Fundamentada no desenvolvimento dos valores humanos: **Solidariedade, Respeito, Justiça e Diálogo**.")
    st.write("Princípios seguidos por todos: Professores, Alunos, Funcionários, Diretores, Coordenadores e Pais/Responsáveis.")

with tab2:
    st.header("Equipe Diretiva")
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown(f'''<div class="img-container">
            <img src="https://raw.githubusercontent.com/kowalskifabio-cpu/reuniao-pais-2026/main/logo.jpg" class="img-circular">
            <div class="nome-equipe">Irmã Olinda</div>
            <div class="cargo-equipe">Diretora</div>
        </div>''', unsafe_allow_html=True)

    with c2:
        st.markdown(f'''<div class="img-container">
            <img src="https://raw.githubusercontent.com/kowalskifabio-cpu/reuniao-pais-2026/main/Ingrit.jpg" class="img-circular">
            <div class="nome-equipe">Ingrit Candido</div>
            <div class="cargo-equipe">Coordenadora Fundamental 2 e Integral Manhã</div>
        </div>''', unsafe_allow_html=True)

    with c3:
        st.markdown(f'''<div class="img-container">
            <img src="https://raw.githubusercontent.com/kowalskifabio-cpu/reuniao-pais-2026/main/Josi.jpg" class="img-circular">
            <div class="nome-equipe">Josiane Dellaqua</div>
            <div class="cargo-equipe">Coordenadora Ed. Infantil, Fundamental 1 e Integral Tarde</div>
        </div>''', unsafe_allow_html=True)

with tab3:
    st.header("Rotina e Avisos Gerais")
    col_a, col_b = st.columns(2)
    with col_a:
        st.write("### ⏰ Horários")
        st.write("- **Manhã (07h25 às 12h10):** Fundamental I e II.")
        st.write("- **Tarde (13h às 17h35):** Fundamental I.")
        st.write("- **Tarde (13h às 17h15):** Educação Infantil.")
        st.warning("Tolerância de 10 min. para atrasos. Após isso, entrada apenas na 2ª aula.")
        
        st.write("### 👕 Uniforme")
        st.write("Uso obrigatório e com nome em todas as peças. Proibido outras cores.")
        
    with col_b:
        st.write("### 💊 Medicação")
        st.write("Somente com receita médica e autorização assinada.")
        st.write("### 🧸 Brinquedos (Sexta)")
        st.write("Proibido eletrônicos ou bolas. Foco no compartilhar.")
        st.write("### 🍎 Lanche")
        st.write("- Tempo de lanche: 15 min. Sugerimos opções saudáveis.")

with tab4:
    st.header("Sistema de Avaliação")
    st.write("A média bimestral é composta por: P1 (Formativa) e P2 (Prova).")
    st.latex(r'''\text{Média Bimestral} = \frac{P1 + P2}{2}''')
    
    c_m1, c_m2 = st.columns(2)
    with c_m1:
        st.metric("Média do Bimestre", "6.0")
    with c_m2:
        st.metric("Aprovação Final", "24.0 pontos")
    
    st.write("Acompanhe em: **www.notasonline.com**")

with tab5:
    st.header("Saídas e Projetos")
    st.write("### 🚌 Aula de Campo")
    st.write("Visitas a museus e parques para aprendizagem concreta.")
    st.write("Exige autorização prévia obrigatória dos pais.")
    
    st.write("### 🧠 Sala de Recursos")
    st.write("Atendimento para alunos Neurodivergentes. Previsão: **Julho**.")
