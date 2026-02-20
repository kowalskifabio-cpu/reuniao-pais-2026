import streamlit as st

# Configuração da página para um visual imersivo e acolhedor
st.set_page_config(
    page_title="Reunião Pedagógica 2026 - Escola Ursula Benincasa",
    page_icon="🏫",
    layout="wide"
)

# Estilização CSS para fotos circulares e design lúdico
st.markdown("""
    <style>
    .stApp { background-color: #F0F7FF; }
    h1, h2, h3 { color: #004A99; font-family: 'Helvetica', sans-serif; }
    
    /* Efeito Circular nas Fotos */
    .img-circular {
        border-radius: 50%;
        border: 5px solid #004A99;
        object-fit: cover;
        width: 180px;
        height: 180px;
        display: block;
        margin-left: auto;
        margin-right: auto;
    }
    
    /* Cards para Equipe */
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        text-align: center;
        min-height: 350px;
    }
    </style>
    """, unsafe_allow_html=True)

# Cabeçalho
col_logo, col_titulo = st.columns([1, 4])
with col_logo:
    st.image("logo.jpg", width=150)
with col_titulo:
    st.title("Reunião Pedagógica 2026")
    st.subheader("Escola Ursula Benincasa — Irmãs Teatinas")

st.info("**Regra Máxima:** 'Sem outra regra além do amor' — Madre Úrsula Benincasa")

# Abas de Conteúdo (Sem resumos)
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🏠 Institucional", "👥 Equipe", "📅 Rotina Escolar", "📊 Avaliação", "🚌 Projetos"
])

with tab1:
    st.header("Nossa Identidade e Proposta")
    st.write("### 🌍 Origens")
    st.write("- **Congregação:** Fundada em Nápoles, Itália, pela Madre Ursula Benincasa no ano de 1583.")
    st.write("- **Mantenedora:** Associação das Irmãs Teatinas da Imaculada Conceição, fundada em 21/07/1973.")
    
    st.write("### 💡 Proposta Pedagógica")
    st.write("Centrada no desenvolvimento dos valores humanos: **Solidariedade, Respeito, Justiça e Diálogo**.")
    st.write("Estes princípios devem ser seguidos por todos: Professores, Alunos, Funcionários, Diretores, Coordenadores e Pais/Responsáveis.")

with tab2:
    st.header("Carômetro - Equipe Diretiva")
    c1, c2, c3 = st.columns(3)
    
    with c1:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<img src="https://raw.githubusercontent.com/kowalskifabio-cpu/reuniao-pais-2026/main/logo.jpg" class="img-circular">', unsafe_allow_html=True)
        st.write("### Irmã Olinda")
        st.write("**Diretora**")
        st.markdown('</div>', unsafe_allow_html=True)

    with c2:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<img src="https://raw.githubusercontent.com/kowalskifabio-cpu/reuniao-pais-2026/main/Ingrit.jpg" class="img-circular">', unsafe_allow_html=True)
        st.write("### Ingrit Candido")
        st.write("**Coordenadora Fundamental 2 e Integral Manhã**")
        st.markdown('</div>', unsafe_allow_html=True)

    with c3:
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.markdown('<img src="https://raw.githubusercontent.com/kowalskifabio-cpu/reuniao-pais-2026/main/Josi.jpg" class="img-circular">', unsafe_allow_html=True)
        st.write("### Josiane Dellaqua")
        st.write("**Coordenadora Ed. Infantil, Fundamental 1 e Integral Tarde**")
        st.markdown('</div>', unsafe_allow_html=True)

with tab3:
    st.header("Orientações, Avisos e Horários")
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.write("### ⏰ Horários de Entrada e Saída")
        st.write("- **Manhã (07h25 às 12h10):** Fundamental I e II.")
        st.write("- **Tarde (13h às 17h35):** Fundamental I.")
        st.write("- **Tarde (13h às 17h15):** Educação Infantil.")
        st.warning("Tolerância de 10 minutos para atrasos. Após isso, entrada apenas na 2ª aula (atrasos maiores apenas com atestado).")
        
        st.write("### 👕 Uniforme e Materiais")
        st.write("- Uso obrigatório e com nome em todas as peças.")
        st.write("- **Biblioteca:** Empréstimos semanais; devolução quinzenal. Multa Fund II: R$ 4,00/dia.")
        st.write("- **Lição de Casa:** Acompanhar diariamente para incentivar autonomia.")
    
    with col_b:
        st.write("### 💊 Saúde e Convivência")
        st.write("- **Medicação:** Apenas com receita médica e autorização assinada.")
        st.write("- **Lanche:** 15 minutos (orientamos opções saudáveis).")
        st.write("- **Dia do Brinquedo (Sexta):** Proibido eletrônicos ou bolas.")
        st.write("- **Aniversários:** Kits individuais com agendamento prévio via agenda.")

with tab4:
    st.header("Sistema de Avaliação (1º ao 9º ano)")
    st.write("### 📊 Composição da Nota")
    st.latex(r'''\text{Média Bimestral} = \frac{P1 (\text{Formativa}) + P2 (\text{Prova})}{2}''')
    
    c_m1, c_m2 = st.columns(2)
    with c_m1:
        st.metric("Média do Bimestre", "6.0")
    with c_m2:
        st.metric("Média Final (Aprovação)", "24.0")
    
    st.info("Acompanhe o desempenho, ocorrências e calendário em: **www.notasonline.com**")

with tab5:
    st.header("Projetos Especiais")
    st.write("### 🚌 Aula de Campo")
    st.write("Vivências em teatros, museus e parques. Acompanhadas por professores e segurança garantida. Exige autorização prévia.")
    
    st.write("### 🧠 Sala de Recursos")
    st.write("Foco em Neurodivergentes. Previsão de inauguração para **Julho**.")

st.markdown("---")
st.caption("Qualquer alteração cadastral (telefone/e-mail) deve ser comunicada via agenda ou Secretaria.")
