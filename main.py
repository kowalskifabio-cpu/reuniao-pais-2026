import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Reunião Pedagógica 2026 - Escola Ursula Benincasa",
    page_icon="🏫",
    layout="wide"
)

# Estilização CSS para fotos circulares e visual limpo
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

# Abas com Conteúdo Integral de todos os slides
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🏠 Institucional", "👥 Equipe", "📅 Avisos & Rotina", "⏰ Horários", "📊 Avaliação", "🚌 Saídas & Projetos"
])

with tab1:
    st.header("Institucional e Proposta")
    st.write("### 🌍 Nossa História")
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
    st.header("Orientações e Avisos Gerais")
    col_a, col_b = st.columns(2)
    with col_a:
        st.write("### 👕 Uniforme")
        st.write("Uso obrigatório e com nome em todas as peças. Proibido outras cores.")
        
        st.write("### 📚 Biblioteca e Literatura (Infantil e Fund 1)")
        st.write("- Dia fixo na semana para empréstimo; devolução quinzenal.")
        st.write("- Aulas de Literatura acontecem quinzenalmente na biblioteca.")
        st.write("- **Multas por atraso:** Infantil e Fund I (por semana); Fund II (R$ 4,00 por dia).")
        
        st.write("### 👩‍🏫 Atendimento e Agendamentos")
        st.write("- Agendar via agenda com antecedência de 24h a 48h.")
        st.write("- Início dos atendimentos em Março; duração média de 20 minutos.")

    with col_b:
        st.write("### 💊 Medicação")
        st.write("Somente com receita médica e autorização assinada.")
        
        st.write("### 🧸 Brinquedos (Sexta-feira)")
        st.write("Proibido eletrônicos ou bolas. Incentivar o compartilhar e a convivência.")
        
        st.write("### 🍎 Lanche e Aniversários")
        st.write("- Tempo de lanche: 15 minutos; orientamos opções saudáveis.")
        st.write("- Aniversários (Infantil e Fund I): Kits individuais agendados via secretaria.")

with tab4:
    st.header("Horários e Pontualidade")
    col_h1, col_h2 = st.columns(2)
    with col_h1:
        st.info("### ☀️ Período Manhã\n**07h25 às 12h10**\nFundamental I e II")
    with col_h2:
        st.info("### 🌤️ Período Tarde\n**13h às 17h35** (Fund I)\n**13h às 17h15** (Ed. Infantil)")
    
    st.warning("⚠️ **Tolerância:** 10 minutos para atrasos. Após isso, o aluno ingressa apenas na 2ª aula.")
    st.write("Atrasos maiores exigem atestado médico ou justificativa dos responsáveis.")

with tab5:
    st.header("Sistema de Avaliação (1º ao 9º ano)")
    st.write("Média do bimestre: 6.0.")
    st.write("Aprovação anual: Média Final igual ou superior a 24.0.")
    
    st.write("#### Composição da Nota:")
    st.latex(r'''\text{Média Bimestral} = \frac{P1 (\text{Formativa}) + P2 (\text{Prova})}{2}''')
    st.write("- **P1 (10,0):** Trabalhos, pesquisas e testes.")
    st.write("- **P2 (10,0):** Prova bimestral.")
    
    st.write("---")
    st.write("### 💻 Notas Online")
    st.write("Acompanhe em: **www.notasonline.com**.")
    st.write("Registros de: Notas, lição de casa, calendário e ocorrências disciplinares.")

with tab6:
    st.header("Projetos Pedagógicos")
    st.write("### 🚌 Aula de Campo")
    st.write("Saídas para teatros, museus e parques visando aprendizagem concreta.")
    st.write("- Acompanhamento garantido por professores e segurança total.")
    st.write("- **Autorização prévia obrigatória**; custos informados com antecedência.")
    
    st.write("---")
    st.write("### 🧠 Sala de Recursos")
    st.write("Atendimento focado em alunos Neurodivergentes. Previsão de inauguração: **Julho**.")
