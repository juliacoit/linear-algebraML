# Álgebra Linear Aplicada ao Machine Learning

### Disciplina

Matemática Discreta

### Objetivo Acadêmico

Este repositório contém o desenvolvimento técnico e visual de uma apresentação acadêmica em vídeo sobre o tema **Álgebra Linear aplicada ao Machine Learning**, com foco na relação entre estruturas algébricas estudadas em matemática discreta e sua aplicação prática em sistemas modernos de inteligência artificial.

O trabalho foi desenvolvido para demonstrar, de forma visual, intuitiva e computacionalmente ilustrada, como conceitos fundamentais da álgebra linear constituem a base matemática de algoritmos de aprendizado de máquina.

---

# Proposta da Apresentação

A apresentação tem duração aproximada de **15 minutos** e busca responder à pergunta central:

> Como sistemas de Machine Learning conseguem transformar dados brutos em decisões inteligentes?

A resposta é construída a partir da demonstração de que computadores não interpretam diretamente imagens, textos, sons ou vídeos.

Todo dado precisa ser convertido em representações matemáticas manipuláveis.

Essa conversão é viabilizada por estruturas da álgebra linear.

---

# Base Conceitual

A narrativa técnica da apresentação está fundamentada em três ideias centrais:

## 1. Representação Matemática dos Dados

Todo dado computacional pode ser expresso como:

* Escalares
* Vetores
* Matrizes
* Tensores

Essas estruturas permitem que algoritmos realizem processamento matemático sobre informações complexas.

---

## 2. Operações Algébricas como Mecanismo Computacional

O processamento interno de modelos de ML depende de operações como:

* Produto interno
* Multiplicação matricial
* Transformações lineares
* Cálculo de distâncias vetoriais
* Similaridade angular

---

## 3. Redução e Organização da Informação

Métodos como decomposição matricial permitem:

* compressão de dados
* extração de padrões
* redução dimensional
* aumento de eficiência computacional

---

# Referência Técnica

A estrutura narrativa foi inspirada em conteúdos educacionais da IBM sobre fundamentos matemáticos de Machine Learning.

A apresentação adota uma abordagem visual semelhante a:

* IBM Learning
* 3Blue1Brown
* visualizações matemáticas computacionais
* animações educacionais baseadas em álgebra linear

---

# Tecnologias Utilizadas

## Linguagem

Python 3.11+

---

## Biblioteca principal

Manim Community Edition

Responsável pela geração das animações matemáticas.

Uso principal:

* visualização vetorial
* transformações lineares
* animações matriciais
* ilustrações geométricas

---

## Dependências auxiliares

### MiKTeX

Necessário para renderização de expressões LaTeX.

Utilizado em:

* MathTex
* Matrix
* fórmulas matemáticas

---

### FFmpeg

Necessário para renderização e exportação de vídeo.

---

## Edição final

Opcionalmente:

* CapCut
* DaVinci Resolve
* Adobe Premiere

---

# Estrutura do Repositório

```text
projeto_video/
│
├── main.py
├── CLAUDE.md
├── assets/
│   ├── imagens
│   └── referências visuais
│
├── media/
│   └── renders gerados
│
└── videos/
    └── composição final
```

---

# Arquitetura das Animações

A apresentação é dividida em cenas independentes.

Cada cena representa um conceito matemático específico.

---

# Cena 1 — Introdução

## Objetivo

Apresentar o problema motivador.

Pergunta central:

> Como uma IA diferencia um gato de um cachorro?

## Conceito abordado

Necessidade de representação matemática dos dados.

## Elementos visuais

* título animado
* transição tecnológica
* introdução narrativa

---

# Cena 2 — Vetores

## Objetivo

Introduzir vetores como representação de características.

## Conceitos matemáticos

* espaço vetorial
* magnitude
* direção
* representação geométrica

## Aplicação em ML

Embeddings e feature vectors.

## Animações

* plano cartesiano
* vetores surgindo dinamicamente
* comparação angular

---

# Cena 3 — Matrizes

## Objetivo

Mostrar como grandes conjuntos de dados são organizados.

## Conceitos matemáticos

* linhas e colunas
* organização matricial
* estrutura algébrica bidimensional

## Aplicação em ML

* datasets
* pesos de redes neurais
* imagens digitalizadas

## Efeito visual

Construção progressiva da matriz.

---

# Cena 4 — Imagem para Matriz

## Objetivo

Demonstrar vetorização visualmente.

## Processo ilustrado

Imagem → Pixels → Valores numéricos → Matriz

## Importância conceitual

Explica como computadores interpretam imagens.

---

# Cena 5 — Similaridade Vetorial

## Objetivo

Mostrar como algoritmos medem semelhança.

## Fórmula principal

Cosine Similarity

## Aplicações

* NLP
* embeddings semânticos
* recomendação de conteúdo
* busca vetorial

## Elementos animados

* vetores com diferentes ângulos
* arco angular
* aproximação vetorial

---

# Cena 6 — Transformações Lineares

## Objetivo

Visualizar ação de matrizes sobre espaços vetoriais.

## Conceitos matemáticos

* transformação linear
* cisalhamento
* rotação
* escala

## Aplicação em ML

Transformações internas em redes neurais.

## Visualização

Deformação da grade cartesiana.

---

# Cena 7 — Rede Neural

## Objetivo

Relacionar álgebra linear ao fluxo computacional real.

## Fórmula central

Y = WX + b

## Interpretação

* X → entrada
* W → matriz de pesos
* b → viés
* Y → saída

## Visualização

* neurônios conectados
* fluxo propagado
* representação matricial

---

# Cena 8 — Decomposição SVD

## Objetivo

Apresentar redução dimensional.

## Fórmula

A = UΣVᵀ

## Conceitos trabalhados

* fatoração matricial
* compressão de informação
* extração de componentes relevantes

## Aplicações práticas

* sistemas de recomendação
* compressão
* embeddings compactos

## Visualização

Matriz se decompondo em três estruturas menores.

---

# Cena 9 — Conclusão

## Mensagem final

Dados → Matemática → Inteligência

A cena reforça a tese principal:

> A inteligência artificial moderna depende diretamente da álgebra linear.

---

# Diretrizes Visuais

## Paleta recomendada

* azul marinho
* ciano
* branco
* roxo escuro

---

## Estilo gráfico

Inspirado em visualizações científicas modernas.

Características:

* fundo escuro
* contraste alto
* animações suaves
* minimalismo técnico

---

# Objetivo Pedagógico

A apresentação busca:

## Demonstrar interdisciplinaridade

Conectar matemática discreta com ciência da computação.

## Tornar abstrações visuais

Facilitar compreensão intuitiva.

## Mostrar aplicação real

Evidenciar uso industrial da matemática.

## Relacionar teoria e prática

Apresentar como estruturas algébricas sustentam sistemas modernos.

---

# Público-Alvo

* professor da disciplina
* colegas de graduação
* estudantes com conhecimento básico de matemática discreta

---

# Resultado Esperado

Ao final da apresentação, espera-se que o espectador compreenda que:

1. Dados precisam ser matematicamente representados
2. Álgebra linear estrutura essa representação
3. Operações matriciais executam processamento
4. Machine Learning depende diretamente dessas estruturas

---

# Comandos de Renderização

Renderização individual:

```bash
manim -pqh main.py NomeDaCena
```

Renderização rápida:

```bash
manim -pql main.py NomeDaCena
```

---

# Observações de Desenvolvimento

Este projeto prioriza:

* clareza conceitual
* fidelidade matemática
* estética visual profissional
* didática acessível

Não busca formalismo matemático excessivo.

O foco é visualização aplicada.

---

# Síntese Final

Este repositório demonstra como estruturas algébricas deixam de ser abstrações formais e tornam-se ferramentas fundamentais para construção de sistemas inteligentes.

A apresentação mostra que a álgebra linear não é apenas teoria matemática.

Ela é a linguagem operacional da inteligência artificial contemporânea.
