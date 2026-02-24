import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Reunião Pedagógica 2026 - Escola Ursula Benincasa",
    page_icon="🏫",
    layout="wide"
)

# Estilização CSS para fotos circulares e design limpo
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

# Abas com 100% do conteúdo
tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "🏠 Institucional", "👥 Equipe", "📅 Avisos & Rotina", "⏰ Horários", "📊 Avaliação", "🚌 Projetos", "☀️ Período Integral"
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
    
    # Primeira linha de professores
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
        st.write("- **Atrasos:** Multa de R$ 4,00 por dia para todos os segmentos (Infantil, Fund. 1 e Fund. 2).")
        st.write("- Aulas de Literatura acontecem quinzenalmente na biblioteca.")
        
        st.write("### 👩‍🏫 Atendimentos Individualizados")
        st.write("- Duração média de 20 minutos, organizados a partir de março.")
        st.write("- **Infantil/Fund I:** Agendar via agenda com horários informados pela escola.")
        st.write("- **Fund II:** Solicitar na Secretaria conforme disponibilidade.")
        st.write("- *Não haverá agendamentos em semanas de avaliação.*")

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
        st.info("### 🌤️ Período Tarde\n**13h às 17h35** (Fund I)\n**13h às 17h15** (Ed. Infantil)")
    
    st.warning("⚠️ **Tolerância:** 10 minutos. Após isso, o aluno ingressa apenas na 2ª aula.")
    st.write("Atrasos superiores exigem atestado médico ou justificativa dos responsáveis.")

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
    st.write("- **Nomenclatura:** A disciplina passou por alteração de nome para 2026, mas mantém o uso do material de Cultura Maker.")
    st.write("- **Alinhamento:** Desenvolvida em total conformidade com a BNCC.")
    st.write("- **Avaliação:** Passará a compor nota para Fundamental 1 e 2.")
    st.write("- **Critérios:** A nota considerará tanto a participação coletiva quanto a individual dos alunos em sala.")

    st.write("---")
    st.write("### 🧪 Feira de Ciências")
    st.write("Projeto voltado à investigação científica e apresentação de experimentos práticos desenvolvidos pelos alunos.")

    st.write("### 🎨 Literarte")
    st.write("Evento que integra literatura e artes, celebrando a produção criativa e cultural de nossos estudantes.")

    st.write("---")
    st.write("### 🧠 Sala de Recursos (Neurodivergentes)")
    st.write("Previsão de inauguração: **Julho**.")

with tab7:
    st.header("Informativo do Integral - manhã")
    st.write("Curitiba, 23 de fevereiro de 2026")
    st.write("Prezadas famílias e queridos alunos,")
    st.write("Pensando sempre no aprendizado, no desenvolvimento integral e na qualidade de ensino, reformulamos as aulas do Integral para tornar a rotina ainda mais rica, dinâmica e significativa para nossos estudantes.")
    st.write("A partir deste período, nossa grade de horários foi reorganizada, contemplando atividades diversificadas que estimulam o desenvolvimento cognitivo, social, emocional e criativo dos alunos.")
    st.write("Convidamos todos a conferirem as novas grades de horário e as aulas disponíveis em cada ciclo.")
    
    st.subheader("Confira as novidades do Integral:")
    
    st.write("#### 🧪 Experiência / Pequenos Cientistas")
    st.write("No laboratório de Ciências, as crianças vivenciam experiências práticas e seguras, explorando fenômenos como misturas, reações simples, estados físicos da matéria, plantio e observação da natureza. De forma lúdica, aprendem a observar, levantar hipóteses e registrar descobertas, despertando a curiosidade científica desde cedo.")
    
    st.write("#### ✍️ Produção Textual (4º e 5º ano)")
    st.write("Espaço dedicado ao desenvolvimento da escrita criativa e formal, trabalhando diferentes gêneros textuais, ampliação de vocabulário, organização de ideias e aprimoramento da expressão escrita.")
    
    st.write("#### 📖 Contação de Histórias")
    st.write("Momento de imaginação e encantamento, estimulando a escuta atenta, a interpretação e o gosto pela leitura.")
    
    st.write("#### 🎭 Iniciação Teatral")
    st.write("Atividades que desenvolvem expressão corporal, oralidade, criatividade, autoconfiança e trabalho em grupo por meio de jogos e práticas teatrais.")
    
    st.write("#### 🎨 Oficina Criativa")
    st.write("Exploração artística com diferentes materiais e técnicas, incentivando a criatividade, coordenação motora e expressão individual.")
    
    st.write("#### ♟️ Xadrez")
    st.write("Desenvolvimento da concentração, planejamento, paciência e tomada de decisões estratégicas.")
    
    st.write("#### 📂 Projeto")
    st.write("Momento destinado a pesquisas, desenvolvimento de trabalhos interdisciplinares e aprofundamento de conteúdos.")
    
    st.write("#### 🍳 Culinária (quinzenal)")
    st.write("Atividade prática que trabalha medidas, organização, autonomia, alimentação saudável e cooperação, além de proporcionar experiências sensoriais.")
    
    st.write("#### 🎵 Musicalização")
    st.write("Vivências com ritmo, canto, percepção sonora e expressão musical, contribuindo para o desenvolvimento cognitivo e sensível.")
    
    st.write("#### 🧩 Raciocínio Lógico e Estratégia (2º ao 5º ano)")
    st.write("Desafios, jogos e situações-problema que estimulam o pensamento lógico, a resolução de problemas e a tomada de decisões.")
    
    st.write("#### 🥬 Horta")
    st.write("Contato direto com a natureza, plantio, cuidados com a terra e aprendizagem sobre sustentabilidade e alimentação saudável.")
    
    st.write("#### ⚽ Esportes")
    st.write("Atividades que promovem coordenação motora, trabalho em equipe, respeito às regras e hábitos saudáveis.")
    
    st.write("---")
    st.write("Além das aulas, os alunos continuam contando com momentos de descontração, café, descanso e almoço, garantindo equilíbrio entre aprendizagem e bem-estar.")
    st.write("Estamos muito animados com essa nova organização e confiantes de que ela proporcionará experiências ainda mais significativas para nossos alunos.")
    st.write("Contamos com a parceria de sempre!")
    st.write("Com carinho, **Equipe do Integral**")
