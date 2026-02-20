import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Reunião Pedagógica 2026 - Escola Ursula Benincasa",
    page_icon="🏫",
    layout="wide"
)

# Estilização CSS para remover os quadrados e ajustar o layout
st.markdown("""
    <style>
    .stApp { background-color: #F0F7FF; }
    h1, h2, h3 { color: #004A99; font-family: 'Helvetica', sans-serif; margin-top: 0px; }
    
    /* Estilo para fotos circulares sem os quadrados brancos */
    .img-container {
        text-align: center;
        padding: 10px;
        margin-top: -20px; /* Sobe o conteúdo */
    }
    
    .img-circular {
        border-radius: 50%;
        border: 4px solid #004A99;
        object-fit: cover;
        width: 180px;
        height: 180px;
        margin-bottom: 10px;
    }

    .nome-equipe {
        font-weight: bold;
        font-size: 1.2em;
        margin-bottom: 2px;
    }
    
    .cargo-equipe {
        font-size: 0.9em;
        color: #555;
    }
    </style>
    """, unsafe_allow_html=True)

# Cabeçalho Principal
col_logo, col_titulo = st.columns([1, 4])
with col_logo:
    st.image("logo.jpg", width=140)
with col_titulo:
    st.title("Reunião Pedagógica 2026")
    st.subheader("Escola Ursula Benincasa — Irmãs Teatinas")

st.info("**Regra Máxima:** 'Sem outra regra além do amor' — Madre Úrsula Benincasa [cite: 88, 89, 90]")

# Abas de Conteúdo 100% fiel ao documento
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🏠 Institucional", "👥 Equipe", "📅 Rotina Escolar", "📊 Avaliação", "🚌 Projetos"
])

with tab1:
    st.header("Identidade e Proposta") [cite: 13]
    st.write("### 🌍 Origens")
    st.write("- **Congregação:** Fundada em Nápoles, Itália, pela Madre Ursula Benincasa em 1583. [cite: 12]")
    st.write("- **Mantenedora:** Associação das Irmãs Teatinas da Imaculada Conceição, fundada em 21/07/1973. [cite: 10, 11]")
    
    st.write("### 💡 Proposta Pedagógica") [cite: 13]
    st.write("Fundamentada no desenvolvimento dos valores humanos: **Solidariedade, Respeito, Justiça e Diálogo**. [cite: 14, 15, 16, 17, 18]")
    st.write("Princípios seguidos por todos: Professores, Alunos, Funcionários, Diretores, Coordenadores e Pais/Responsáveis. [cite: 19, 20]")

with tab2:
    st.header("Equipe Diretiva") [cite: 3]
    # Layout limpo para a equipe
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown(f'''<div class="img-container">
            <img src="https://raw.githubusercontent.com/kowalskifabio-cpu/reuniao-pais-2026/main/logo.jpg" class="img-circular">
            <div class="nome-equipe">Irmã Olinda</div>
            <div class="cargo-equipe">Diretora</div>
        </div>''', unsafe_allow_html=True) [cite: 6, 7]

    with c2:
        st.markdown(f'''<div class="img-container">
            <img src="https://raw.githubusercontent.com/kowalskifabio-cpu/reuniao-pais-2026/main/Ingrit.jpg" class="img-circular">
            <div class="nome-equipe">Ingrit Candido</div>
            <div class="cargo-equipe">Coordenadora Fundamental 2 e Integral Manhã</div>
        </div>''', unsafe_allow_html=True) [cite: 4, 5]

    with c3:
        st.markdown(f'''<div class="img-container">
            <img src="https://raw.githubusercontent.com/kowalskifabio-cpu/reuniao-pais-2026/main/Josi.jpg" class="img-circular">
            <div class="nome-equipe">Josiane Dellaqua</div>
            <div class="cargo-equipe">Coordenadora Ed. Infantil, Fundamental 1 e Integral Tarde</div>
        </div>''', unsafe_allow_html=True) [cite: 8, 9]

with tab3:
    st.header("Rotina e Avisos Gerais") [cite: 21]
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.write("### ⏰ Horários") [cite: 59]
        st.write("- **Manhã (07h25 às 12h10):** Fundamental I e II. [cite: 61]")
        st.write("- **Tarde (13h às 17h35):** Fundamental I. [cite: 62]")
        st.write("- **Tarde (13h às 17h15):** Educação Infantil. [cite: 62]")
        st.warning("Tolerância de 10 min. para atrasos. Após isso, entrada apenas na 2ª aula. [cite: 63]")
        
        st.write("### 👕 Uniforme")
        st.write("Uso obrigatório e com nome em todas as peças. Proibido outras cores. [cite: 22]")
        
        st.write("### 📚 Biblioteca (Inf. e Fund. 1)") [cite: 23]
        st.write("- Dia fixo para empréstimo; devolução quinzenal. [cite: 24, 25]")
        st.write("- **Multas por atraso:** Fund. II cobra R$ 4,00 por dia. [cite: 28]")

    with col_b:
        st.write("### 💊 Medicação")
        st.write("Somente com receita médica e autorização assinada. [cite: 41, 42]")
        
        st.write("### 🧸 Brinquedos (Sexta)") [cite: 43, 44]
        st.write("Proibido eletrônicos ou bolas. Foco no compartilhar. [cite: 45, 47]")
        
        st.write("### 🍎 Lanche e Aniversários")
        st.write("- Lanche: 15 min. [cite: 49] Sugerimos opções saudáveis. [cite: 50]")
        st.write("- Aniversários: Kits individuais com agendamento prévio. [cite: 53, 54, 55]")

with tab4:
    st.header("Sistema de Avaliação (1º ao 9º ano)") [cite: 65, 66]
    st.write("A média bimestral é composta por duas notas: P1 (Formativa) e P2 (Prova). [cite: 74, 75, 76, 77]")
    
    st.latex(r'''\text{Média Bimestral} = \frac{P1 + P2}{2}''') [cite: 78, 79]
    
    c_m1, c_m2 = st.columns(2)
    with c_m1:
        st.metric("Média do Bimestre", "6.0") [cite: 67]
    with c_m2:
        st.metric("Aprovação Final", "24.0 pontos") [cite: 68, 69]
    
    st.write("Acompanhe ocorrências e notas em: **www.notasonline.com** [cite: 70, 71, 72, 73]")

with tab5:
    st.header("Saídas e Projetos")
    st.write("### 🚌 Aula de Campo") [cite: 80]
    st.write("Visitas a museus, parques e teatros para aprendizagem concreta. [cite: 81, 82]")
    st.write("Exige autorização prévia obrigatória dos pais. [cite: 84]")
    
    st.write("### 🧠 Sala de Recursos") [cite: 86]
    st.write("Atendimento para alunos Neurodivergentes. Previsão: **Julho**. [cite: 87]")
