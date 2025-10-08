# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="https://raw.githubusercontent.com/lfusca/templateFiap/main/assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

## 👨‍🎓 Integrantes do Grupo

- RM559800 - [Jonas Felipe dos Santos Lima](https://www.linkedin.com/in/jonas-felipe-dos-santos-lima-b2346811b/)
- RM560173 - [Gabriel Ribeiro](https://www.linkedin.com/in/ribeirogab/)
- RM559926 - [Marcos Trazzini](https://www.linkedin.com/in/mstrazzini/)
- RM559645 - [Edimilson Ribeiro](https://www.linkedin.com/in/edimilson-ribeiro/)

## 👩‍🏫 Professores

### Coordenador(a)

- [André Godoi](https://www.linkedin.com/in/profandregodoi/)



## 📖 Sobre o Projeto

Este projeto faz parte do **Desafio Integrador** da FIAP, focado em aplicações de Inteligência Artificial na área médica. O objetivo é desenvolver sistemas inteligentes capazes de auxiliar no diagnóstico médico através da análise de sintomas e classificação de frases médicas.

Na fase do, o projeto está dividido em **duas fases**:
- **Parte 1**: Sistema de diagnóstico baseado em sintomas cardiovasculares
- **Parte 2**: Classificação de frases médicas utilizando técnicas de Machine Learning

---

## 🎯 Objetivos

### Objetivos Gerais
- Aplicar técnicas de Inteligência Artificial em contextos médicos reais
- Desenvolver sistemas de apoio ao diagnóstico clínico
- Explorar processamento de linguagem natural (NLP) aplicado à saúde
- Demonstrar competências em análise de dados e machine learning

1. **Parte 1**: Criar um sistema de mapeamento sintoma-diagnóstico para doenças cardiovasculares
2. **Parte 2**: Implementar algoritmos de classificação para frases médicas rotuladas
3. Comparar diferentes abordagens de IA aplicadas à medicina
4. Avaliar métricas de desempenho e acurácia dos modelos

---

## 🚀 Desenvolvimento

### Parte 1: Sistema de Diagnóstico por Sintomas

#### 📝 Descrição
Sistema de diagnóstico médico focado em **doenças cardiovasculares**, utilizando correspondência de padrões entre sintomas relatados por pacientes e um mapa de conhecimento médico.

#### 🔑 Características Principais
- ✅ **Simplicidade**: Código limpo com ~100 linhas, sem dependências externas complexas
- ✅ **Base de Conhecimento**: 30 regras de correlação sintoma-doença
- ✅ **15 Doenças Cardiovasculares**: Cobertura ampla de patologias cardíacas
- ✅ **Pontuação Normalizada**: Escala de 0 a 10 pontos
- ✅ **Variações de Sintomas**: Múltiplas formas de descrever o mesmo sintoma

#### 📊 Estatísticas
- **Total de frases de teste**: 10
- **Regras no mapa de sintomas**: 30
- **Doenças cobertas**: 15
- **Pontuação média**: 5.5/10 (sistema escalonado otimizado)
- **Taxa de diagnóstico**: 100% (todas as frases geram sugestão)

#### 🏥 Doenças Incluídas
1. Infarto agudo do miocárdio
2. Angina estável
3. Angina instável
4. Insuficiência cardíaca
5. Arritmia cardíaca
6. Hipertensão arterial
7. Doença coronariana
8. Cardiomiopatia
9. Pericardite
10. Endocardite
11. Síndrome coronariana aguda
12. Taquicardia
13. Bradicardia
14. Fibrilação atrial
15. Doença valvular cardíaca

#### 📁 Arquivos
```
parte1/
├── diagnostico.py              # Script principal (~100 linhas)
├── mapa_sintomas.csv          # Base de conhecimento (30 regras)
├── phrases_10.txt             # Frases de teste (10 frases)
└── resultados_sugestao.csv    # Saída com diagnósticos (gerado automaticamente)
```

#### ⚙️ Como Funciona
1. **Normalização**: Remove acentos e converte texto para minúsculas
2. **Mapeamento**: Carrega regras do arquivo `mapa_sintomas.csv`
3. **Correspondência**: Identifica sintomas presentes na frase do paciente
4. **Pontuação Escalonada**: Calcula score baseado em sintomas únicos encontrados:
   - 1 sintoma único → 3.5 pontos (casos leves)
   - 2 sintomas únicos → 6.0 pontos (casos moderados)
   - 3 sintomas únicos → 8.0 pontos (casos graves)
   - 4+ sintomas únicos → 10.0 pontos (casos críticos)
5. **Diagnóstico**: Sugere a doença com maior correlação de sintomas

#### 🔍 Exemplo de Uso
```bash
cd parte1
python diagnostico.py
```

**Entrada** (phrases_10.txt):
```
Ha quatro dias sinto uma dor toracica intensa que se espalha para o braco esquerdo 
acompanhada de nausea forte e sudorese profusa que nao para
```

**Saída** (resultados_sugestao.csv):
```csv
Frase,Sintomas_Encontrados,Diagnóstico_Sugerido,Pontuação
"Ha quatro dias sinto uma dor toracica...","dor toracica;nausea;sudorese;sudorese profusa","Infarto agudo do miocardio",10.0
```

> **Nota**: A pontuação de 10.0 indica caso crítico com 4 sintomas únicos identificados.

---

### Parte 2: Classificação de Frases Médicas

#### 📝 Descrição
Sistema de **classificação de frases médicas** utilizando técnicas de Machine Learning e NLP.

#### 📁 Arquivos
```
parte2/
└── frases_medicas_rotuladas.csv            # Dataset rotulado para treinamento e testes do modelo
└── classificador_triagem_clinica.ipynb     # Notebook com código do classificador
```

#### Link para vídeo no YT mostrando o funcionamento da solução
https://www.youtube.com/watch?v=TMQu9GWmmbU


#### 🎯 Objetivos Planejados
- Classificação multi-classe de frases médicas
- Comparação de algoritmos (Naive Bayes, SVM, Redes Neurais)
- Análise de métricas (Precisão, Recall, F1-Score)
- Visualização de resultados

---

## 📂 Estrutura de Pastas

```
2025-2-fase2/
│
├── README.md                                   # Este arquivo (documentação principal)
├── .venv/                                      # Ambiente virtual Python
│
├── parte1/                                     # PARTE 1: Diagnóstico por Sintomas
│   ├── diagnostico.py                          # Script principal de diagnóstico
│   ├── mapa_sintomas.csv                       # Base de conhecimento (30 regras)
│   ├── phrases_10.txt                          # 10 frases de teste
│   └── resultados_sugestao.csv                 # Resultados gerados (criado ao executar)
│
└── parte2/                                     # PARTE 2: Classificação de Frases
    └── frases_medicas_rotuladas.csv            # Dataset rotulado
    └── classificador_triagem_clinica.ipynb     # Notebook com código do classificador
    
```

---

## 🖥️ Como Executar

### Pré-requisitos
- Python 3.13+ instalado

### Passo a Passo

#### 1️⃣ Clonar o Repositório
```bash
git clone https://github.com/FIAP-IA2024/2025-2-fase2.git
cd 2025-2-fase2
```

#### 2️⃣ Criar Ambiente Virtual
```bash
python -m venv .venv
```

#### 3️⃣ Ativar Ambiente Virtual
**Windows PowerShell:**
```powershell
.venv\Scripts\Activate.ps1
```

**Windows CMD:**
```cmd
.venv\Scripts\activate.bat
```

**Linux/Mac:**
```bash
source .venv/bin/activate
```

#### 4️⃣ Executar Parte 1
```bash
cd parte1
python diagnostico.py
```

#### 5️⃣ Verificar Resultados
```bash
cat resultados_sugestao.csv
```

---

## 🛠️ Tecnologias Utilizadas

### Linguagens e Frameworks
- **Python 3.13.6**: Linguagem principal
- **Bibliotecas Padrão**: `csv`, `re`, `pathlib`, `collections`

### Ferramentas
- **VS Code**: Editor de código
- **Git**: Controle de versão
- **PowerShell**: Terminal padrão (Windows)

### Metodologias
- **Pattern Matching**: Correspondência de padrões de sintomas
- **Text Normalization**: Normalização de texto para melhor matching
- **CSV-Based Knowledge Base**: Base de conhecimento em formato CSV
- **Escala de Pontuação Escalonada**: Sistema inteligente baseado em quantidade de sintomas únicos

---

## 📚 Fontes de Dados

### Parte 1: Mapa de Sintomas
- **Fonte**: Literatura médica especializada e guidelines clínicos cardiovasculares
- **Tipo**: Conhecimento estruturado em formato CSV com variações sintomáticas
- **Cobertura**: 30 regras de correlação sintoma-diagnóstico
- **Doenças**: 15 patologias cardiovasculares mapeadas

### Parte 2: Frases Médicas Rotuladas
- **Arquivo**: Gerado utilizando o ChatGPT
- **Status**: 400 linhas, sendo 200 para cada rótulo (baixo e alto risco)
- **Tipo**: Rotulação binária (baixo e alto risco)

---

## 📄 Licenças

### Código Fonte
- **Licença**:
- **Uso Acadêmico**: 
- **Uso Comercial**: 

### Dados Médicos
- **Aviso**: Os dados e diagnósticos fornecidos por este sistema são **exclusivamente educacionais**
- **Não substituem**: Consulta médica profissional qualificada
- **Responsabilidade**: Os autores não se responsabilizam por uso clínico real deste sistema

---

**Última atualização**: Outubro 2025
