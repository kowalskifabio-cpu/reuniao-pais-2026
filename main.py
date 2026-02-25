import streamlit as st
from fpdf import FPDF
import io

# --- FUNÇÃO PARA GERAR O PDF DE SEGURANÇA ---
def gerar_pdf_seguranca():
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # Título do PDF
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Escola Ursula Benincasa - Planejamento 2026", ln=True, align='C')
    pdf.ln(10)

    # Conteúdo estruturado para o PDF baseado no seu script
    secoes = [
        ("Institucional", "Mantenedora: Associação das Irmãs Teatinas (1973). Congregação: Fundada em 1583 por Madre Ursula Benincasa. Valores: Solidariedade, Respeito, Justiça e Diálogo."),
        ("Equipe", "Diretora: Irmã Olinda. Coordenadoras: Ingrit Candido e Josiane Dellaqua. Professores: Ana Desirée, Evandro, Ilana e Luci."),
        ("Avisos e Rotina", "Uniforme: Uso obrigatório (proibido chinelo/Crocs). Biblioteca: Multa Inf/Fund1 R$4,00/semana; Fund2 R$4,00/dia. Medicação: Apenas com receita."),
        ("Horários", "Manhã: 07h25-12h10. Tarde Fund1: 17h35. Ed. Infantil: 17h00 (Tolerância até 17h10)."),
        ("Avaliação", "Média Bimestral: 6.0. Aprovação Final: 24.0. Sistema: (P1+P2)/2. Acompanhamento: www.notasonline.com"),
        ("Projetos", "Aula de Campo, Educação Digital (Antiga Maker), Feira de Ciências, Literarte e Sala de Recursos (Julho).")
    ]

    for titulo, texto in secoes:
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 10, titulo, ln=True)
        pdf.set_font("Arial", "", 10)
        pdf.multi_cell(0, 7, texto)
        pdf.ln(4)
    
    # Retorna o PDF como bytes
    return pdf.output(dest='S').encode('latin-1', 'replace')

# --- CONFIGURAÇÃO DA PÁGINA (ORIGINAL) ---
st.set_page_config(
    page_title="Reunião Pedagógica 2026 - Escola Ursula Benincasa",
    page_icon="🏫",
    layout="wide"
)

# Estilização CSS (ORIGINAL)
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

# Cabeçalho com Inclusão do Botão de PDF
col_logo, col_titulo, col_btn = st.columns([1, 4, 1.2])
with col_logo:
    st.image("logo.jpg", width=140)
with col_titulo:
    st.title("Reunião Pedagógica 2026")
    st.subheader("Escola Ursula Benincasa — Irmãs Teatinas")
with col_btn:
    # Gerador de PDF integrado
    try:
        pdf_bytes = gerar_pdf_seguranca()
        st.download_button(
            label="📄 Baixar PDF de Segurança",
            data=pdf_bytes,
            file_name="Resumo_Reuniao_2026.pdf",
            mime="application/pdf",
        )
    except Exception as e:
        st.error("Erro ao gerar PDF. Verifique o fpdf2.")

st.info("**Regra Máxima:** 'Sem outra regra além do amor' — Madre Úrsula Benincasa")

# Abas com 100% do conteúdo (ORIGINAL)
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "🏠 Institucional", "👥 Equipe", "📅 Avisos & Rotina", "⏰ Horários", "📊 Avaliação", "🚌 Projetos"
])

with tab1:
    st.header("Institucional e Proposta")
    st.write("### 🌍 Mantenedora e Congregação")
    st.write("- **Associação das Irmãs Teatinas da Imaculada Conceição:** Fundada em 21/07/1973.")
    st.write("- **Congregação:** Fundada em Nápoles, Itália, pela Madre Ursula Benincasa em 1583.")
    
    st.write("### 💡 Proposta Pedagógica")
    st.write("Fundamentada no desenvolvimento dos valores humanos: **Solidariedade, Respeito, Justiça e Diálogo**.")
    st.write("Princípios seguidos por todos: Professores, Alunos, Funcionários, Diretores, Coordenadores e Pais/Responsáveis.")

with tab2:
    st.header("Equipe Diretiva (Carômetro)")
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

    st.markdown("---")
    st.header("Corpo Docente")
    
    p1, p2, p3, p4 = st.columns(4)
    
    with p1:
        st.markdown(f'''<div class="img-container">
            <img src="https://raw.githubusercontent.com/kowalskifabio-cpu/reuniao-pais-2026/main/Ana%20Desir%C3%A9e.jpg" class="img-circular">
            <div class="nome-equipe">Ana Desirée</div>
            <div class="cargo-equipe">Professora de Inglês (3º, 4º e 5º anos)</div>
        </div>''', unsafe_allow_html=True)

    with p2:
        st.markdown(f'''<div class="img-container">
            <img src="https://raw.githubusercontent.com/kowalskifabio-cpu/reuniao-pais-2026/main/Evandro.jpg" class="img-circular">
            <div class="nome-equipe">Evandro</div>
            <div class="cargo-equipe">Educação Física (Infantil ao Fund. 2)</div>
        </div>''', unsafe_allow_html=True)

    with p3:
        st.markdown(f'''<div class="img-container">
            <img src="https://raw.githubusercontent.com/kowalskifabio-cpu/reuniao-pais-2026/main/Ilana.jpg" class="img-circular">
            <div class="nome-equipe">Ilana</div>
            <div class="cargo-equipe">Professora de Inglês (Ed. Infantil, 1º e 2º anos)</div>
        </div>''', unsafe_allow_html=True)

    with p4:
        st.markdown(f'''<div class="img-container">
            <img src="https://raw.githubusercontent.com/kowalskifabio-cpu/reuniao-pais-2026/main/Luci.jpg" class="img-circular">
            <div class="nome-equipe">Luci</div>
            <div class="cargo-equipe">Educação Digital (Infantil e Fund. 1)</div>
        </div>''', unsafe_allow_html=True)

with tab3:
    st.header("Orientações Educacionais e Avisos")
    col_a, col_b = st.columns(2)
    with col_a:
        st.write("### 👕 Uniforme")
        st.write("Uso obrigatório e com nome em todas as peças. Não serão permitidas outras cores.")
        st.warning("É proibido o uso de chinelos ou calçados tipo 'Crocs' por questões de segurança e padronização.")
        
        st.write("### 📚 Biblioteca e Literatura (Infantil e Fund 1)")
        st.write("- Dia fixo na semana para empréstimo; devolução quinzenal.")
        st.write("- **Atrasos:** Infantil e Fundamental I (multa de R$ 4,00 por semana); Fundamental II (multa de R$ 4,00 por dia).")
        st.write("- Aulas de Literatura acontecem quinzenalmente na biblioteca.")
        
        st.write("### 👩‍🏫 Atendimentos Individualizados")
        st.write("- Duração média de 20 minutos, organizados a partir de março.")
        st.write("- **Infantil/Fund I:** Agendar via agenda com horários informados pela escola.")
        st.write("- **Fund II:** Solicitar na Secretaria conforme disponibilidade.")

    with col_b:
        st.write("### 💊 Medicação e Saúde")
        st.write("Administração somente com receita médica e autorização assinada.")
        
        st.write("### 🧸 Dia do Brinquedo (Sexta-feira)")
        st.write("Educação Infantil e Fundamental I. Proibido eletrônicos ou bolas.")
        st.write("Objetivo: incentivar o compartilhar e a convivência coletiva.")
        
        st.write("### 🍎 Lanche e Aniversários")
        st.write("- Lanche: 15 minutos; orientamos opções saudáveis.")
        st.write("- Aniversários: Kits individuais com agendamento via agenda e Secretaria.")
        
        st.write("### 📝 Lição de Casa e Cadastro")
        st.write("- Acompanhar diariamente para incentivar autonomia e responsabilidade.")
        st.write("- Alterações de telefone/e-mail devem ser comunicadas via agenda.")

with tab4:
    st.header("Horários e Pontualidade")
    col_h1, col_h2 = st.columns(2)
    with col_h1:
        st.info("### ☀️ Período Manhã\n**07h25 às 12h10**\nFundamental I e II")
    with col_h2:
        st.info("### 🌤️ Período Tarde\n**13h às 17h35** (Fund I)\n**13h às 17h00** (Ed. Infantil)")
    
    st.warning("⚠️ **Tolerância:** 10 minutos (Entrada). Na saída da Educação Infantil, tolerância até 17h10.")
    st.write("Atrasos superiores na entrada exigem atestado médico ou justificativa dos responsáveis.")

with tab5:
    st.header("Sistema de Avaliação e Controle")
    st.write("### 📊 Ensino Fundamental (1º ao 9º ano)")
    st.write("- **Média Bimestral:** 6.0")
    st.write("- **Aprovação Final:** Média Final (MF) ≥ 24.0")
    
    st.latex(r'''\text{Média} = \frac{P1 (\text{Formativa}) + P2 (\text{Prova})}{2}''')
    st.write("- **P1 (10,0):** Trabalhos, pesquisas, testes e atividades formativas.")
    st.write("- **P2 (10,0):** Prova bimestral.")
    
    st.write("---")
    st.write("### 💻 Sistema Notas Online (www.notasonline.com)")
    st.write("Acesso a: Calendários, boletim, lição de casa e registro de ocorrências.")
    st.error("Registros incluem: desentendimento, desrespeito, dano material, atrasos e uniforme incompleto.")

with tab6:
    st.header("Projetos Pedagógicos")
    st.write("### 🚌 Aula de Campo")
    st.write("Objetivo: experiências concretas em teatros, museus, parques e grutas.")
    st.write("- Acompanhamento total por professores e funcionários.")
    st.write("- **Obrigatória autorização prévia dos pais.**")
    st.write("- Custos de transporte/ingressos informados previamente.")
    
    st.write("---")
    st.write("### 💻 Educação Digital (Antiga Cultura Maker)")
    st.write("- **Nomenclatura:** Disciplina alterada em 2026, mantendo material de Cultura Maker e alinhamento à BNCC.")
    st.write("- **Avaliação:** Compõe nota para Fundamental 1 e 2 (participação coletiva e individual).")

    st.write("---")
    st.write("### 🧪 Feira de Ciências e 🎨 Literarte")
    st.write("Projetos voltados à investigação científica, literatura e artes.")

    st.write("---")
    st.write("### 🧠 Sala de Recursos (Neurodivergentes)")
    st.write("Previsão de inauguração: **Julho**.")
