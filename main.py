import streamlit as st
from fpdf import FPDF
import io

# --- FUNÇÃO PARA GERAR O PDF COMPLETO (MÚLTIPLAS PÁGINAS) ---
def gerar_pdf_completo():
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    
    # Configuração de Fontes e Título
    pdf.set_font("Arial", "B", 18)
    pdf.set_text_color(0, 74, 153) # Azul Teatinas
    pdf.cell(0, 15, "Escola Ursula Benincasa - Informativo 2026", ln=True, align='C')
    pdf.ln(5)

    # Definição do conteúdo integral para o PDF
    conteudo_integral = [
        ("🏠 Institucional", [
            "Mantenedora: Associação das Irmãs Teatinas da Imaculada Conceição (Fundada em 21/07/1973).",
            "Congregação: Fundada em Nápoles, Itália, pela Madre Ursula Benincasa em 1583.",
            "Valores Humanos: Solidariedade, Respeito, Justiça e Diálogo.",
            "Regra Máxima: 'Sem outra regra além do amor' — Madre Úrsula Benincasa."
        ]),
        ("👥 Equipe", [
            "Diretora: Irmã Olinda",
            "Coordenadora Fundamental 2 e Integral Manhã: Ingrit Candido",
            "Coordenadora Ed. Infantil, Fund. 1 e Integral Tarde: Josiane Dellaqua",
            "Docentes: Ana Desirée (Inglês), Evandro (Ed. Física), Ilana (Inglês), Luci (Ed. Digital)."
        ]),
        ("📅 Orientações e Avisos", [
            "Uniforme: Uso obrigatório. Proibido chinelos ou calçados tipo 'Crocs'.",
            "Biblioteca: Multa Infantil e Fund. I: R$ 4,00 por semana. Fund. II: R$ 4,00 por dia.",
            "Medicação: Somente com receita médica e autorização assinada.",
            "Dia do Brinquedo: Sextas-feiras (proibido eletrônicos ou bolas).",
            "Aniversários: Kits individuais agendados previamente."
        ]),
        ("⏰ Horários e Pontualidade", [
            "Manhã: 07h25 às 12h10 (Fundamental I e II).",
            "Tarde Fund I: 13h00 às 17h35.",
            "Tarde Ed. Infantil: 13h00 às 17h00.",
            "Tolerância Entrada: 10 minutos. Tolerância Saída Infantil: 17h10."
        ]),
        ("📊 Sistema de Avaliação", [
            "Média Bimestral: 6.0 | Aprovação Final: 24.0 pontos.",
            "Fórmula: (P1 [Formativa] + P2 [Prova]) / 2.",
            "Notas Online: Acompanhamento via www.notasonline.com."
        ]),
        ("🚌 Projetos Pedagógicos", [
            "Aula de Campo: Experiências concretas (museus, parques, grutas).",
            "Educação Digital: Baseada na BNCC, antiga Cultura Maker (compõe nota).",
            "Eventos: Feira de Ciências e Literarte.",
            "Inovação: Sala de Recursos para Neurodivergentes (Previsão: Julho)."
        ])
    ]

    for titulo, itens in conteudo_integral:
        # Título da Secção
        pdf.set_font("Arial", "B", 14)
        pdf.set_text_color(0, 74, 153)
        pdf.cell(0, 12, titulo, ln=True)
        
        # Itens da Secção
        pdf.set_font("Arial", "", 11)
        pdf.set_text_color(0, 0, 0)
        for item in itens:
            pdf.multi_cell(0, 8, f"• {item}")
        pdf.ln(5)
    
    # Retorna o PDF em bytes de forma compatível
    return pdf.output()

# --- CONFIGURAÇÃO STREAMLIT (APRESENTAÇÃO) ---
st.set_page_config(
    page_title="Reunião Pedagógica 2026 - Escola Ursula Benincasa",
    page_icon="🏫",
    layout="wide"
)

# CSS (Original mantido)
st.markdown("""
    <style>
    .stApp { background-color: #F0F7FF; }
    h1, h2, h3 { color: #004A99; font-family: 'Helvetica', sans-serif; margin-top: 0px; }
    .img-container { text-align: center; padding: 10px; margin-top: -10px; }
    .img-circular { border-radius: 50%; border: 4px solid #004A99; object-fit: cover; width: 180px; height: 180px; margin-bottom: 10px; }
    .nome-equipe { font-weight: bold; font-size: 1.2em; margin-bottom: 2px; }
    .cargo-equipe { font-size: 0.9em; color: #555; }
    </style>
    """, unsafe_allow_html=True)

# Cabeçalho com Botão de Download
col_logo, col_titulo, col_pdf = st.columns([1, 4, 1.5])
with col_logo:
    st.image("logo.jpg", width=140)
with col_titulo:
    st.title("Reunião Pedagógica 2026")
    st.subheader("Escola Ursula Benincasa — Irmãs Teatinas")
with col_pdf:
    try:
        pdf_data = gerar_pdf_completo()
        st.download_button(
            label="📄 Baixar Informativo Completo (PDF)",
            data=pdf_data,
            file_name="Escola_Ursula_Benincasa_2026.pdf",
            mime="application/pdf"
        )
    except Exception as e:
        st.error(f"Erro no PDF: {e}")

st.info("**Regra Máxima:** 'Sem outra regra além do amor' — Madre Úrsula Benincasa")

# Navegação por Abas (Para a apresentação)
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

with tab2:
    st.header("Equipe Diretiva (Carômetro)")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(f'''<div class="img-container"><img src="https://raw.githubusercontent.com/kowalskifabio-cpu/reuniao-pais-2026/main/logo.jpg" class="img-circular"><div class="nome-equipe">Irmã Olinda</div><div class="cargo-equipe">Diretora</div></div>''', unsafe_allow_html=True)
    with c2:
        st.markdown(f'''<div class="img-container"><img src="https://raw.githubusercontent.com/kowalskifabio-cpu/reuniao-pais-2026/main/Ingrit.jpg" class="img-circular"><div class="nome-equipe">Ingrit Candido</div><div class="cargo-equipe">Coordenadora Fundamental 2 e Integral Manhã</div></div>''', unsafe_allow_html=True)
    with c3:
        st.markdown(f'''<div class="img-container"><img src="https://raw.githubusercontent.com/kowalskifabio-cpu/reuniao-pais-2026/main/Josi.jpg" class="img-circular"><div class="nome-equipe">Josiane Dellaqua</div><div class="cargo-equipe">Coordenadora Ed. Infantil, Fundamental 1 e Integral Tarde</div></div>''', unsafe_allow_html=True)
    
    st.markdown("---")
    st.header("Corpo Docente")
    p1, p2, p3, p4 = st.columns(4)
    with p1: st.markdown(f'''<div class="img-container"><img src="https://raw.githubusercontent.com/kowalskifabio-cpu/reuniao-pais-2026/main/Ana%20Desir%C3%A9e.jpg" class="img-circular"><div class="nome-equipe">Ana Desirée</div><div class="cargo-equipe">Inglês (3º ao 5º)</div></div>''', unsafe_allow_html=True)
    with p2: st.markdown(f'''<div class="img-container"><img src="https://raw.githubusercontent.com/kowalskifabio-cpu/reuniao-pais-2026/main/Evandro.jpg" class="img-circular"><div class="nome-equipe">Evandro</div><div class="cargo-equipe">Ed. Física</div></div>''', unsafe_allow_html=True)
    with p3: st.markdown(f'''<div class="img-container"><img src="https://raw.githubusercontent.com/kowalskifabio-cpu/reuniao-pais-2026/main/Ilana.jpg" class="img-circular"><div class="nome-equipe">Ilana</div><div class="cargo-equipe">Inglês (Infantil/1º/2º)</div></div>''', unsafe_allow_html=True)
    with p4: st.markdown(f'''<div class="img-container"><img src="https://raw.githubusercontent.com/kowalskifabio-cpu/reuniao-pais-2026/main/Luci.jpg" class="img-circular"><div class="nome-equipe">Luci</div><div class="cargo-equipe">Educação Digital</div></div>''', unsafe_allow_html=True)

with tab3:
    st.header("Orientações Educacionais e Avisos")
    col_a, col_b = st.columns(2)
    with col_a:
        st.write("### 👕 Uniforme")
        st.warning("Proibido o uso de chinelos ou 'Crocs'.")
        st.write("### 📚 Biblioteca")
        st.write("- Multa Inf./Fund 1: R$ 4,00 por semana.")
        st.write("- Multa Fund 2: R$ 4,00 por dia.")
    with col_b:
        st.write("### 💊 Medicação")
        st.write("Somente com receita médica e autorização assinada.")
        st.write("### 🧸 Dia do Brinquedo")
        st.write("Sexta-feira. Proibido eletrônicos.")

with tab4:
    st.header("Horários e Pontualidade")
    col_h1, col_h2 = st.columns(2)
    with col_h1: st.info("### ☀️ Manhã: 07h25 às 12h10")
    with col_h2: st.info("### 🌤️ Tarde Fund 1: 17h35 | Infantil: 17h00")
    st.warning("⚠️ Saída Infantil: Tolerância até 17h10.")

with tab5:
    st.header("Sistema de Avaliação")
    st.latex(r'''\text{Média} = \frac{P1 + P2}{2}''')
    st.write("- Média Bimestral: 6.0 | Aprovação Final: 24.0")

with tab6:
    st.header("Projetos Pedagógicos")
    st.write("### 🚌 Aula de Campo | 🧪 Feira de Ciências | 🎨 Literarte")
    st.write("### 💻 Educação Digital (Antiga Maker)")
    st.write("### 🧠 Sala de Recursos (Neurodivergentes): Previsão Julho.")
