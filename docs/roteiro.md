# Roteiro — Álgebra Linear Aplicada ao Machine Learning

**Disciplina:** Matemática Discreta
**Duração total:** ~15 minutos
**Formato:** Narração em voz-over sincronizada com animações Manim (tela 100% animada)

---

## Apresentadores

| Sigla | Nome       | Perfil narrativo                        |
|-------|------------|-----------------------------------------|
| **A1** | Apresentador 1 | Apresenta os conceitos motivadores e faz as transições entre blocos |
| **A2** | Apresentador 2 | Explica a matemática formal e as estruturas algébricas |
| **A3** | Apresentador 3 | Conecta os conceitos ao Machine Learning aplicado |

---

---

# CENA 1 — INTRODUÇÃO
**Duração estimada: 1min 40s**
**Classe Manim:** `Intro`

---

## [0:00 — 0:10] Tela preta com partículas surgindo

**ANIMAÇÃO:**
Fundo totalmente preto. Pequenos pontos brancos surgem lentamente, como estrelas ou nós de uma rede neural. Um brilho suave pulsa ao centro.

**A1 (narração):**
> "Vivemos em uma era em que máquinas reconhecem rostos, traduzem idiomas, recomendam filmes e diagnosticam doenças."

---

## [0:10 — 0:25] Título principal surge com Write

**ANIMAÇÃO:**
`Write(Text("Álgebra Linear aplicada ao Machine Learning", font_size=42))`
O texto é desenhado letra por letra, centralizado na tela. Cor branca sobre fundo escuro.

**A1 (narração):**
> "Mas o que há por baixo de tudo isso? Qual é o mecanismo matemático que torna a inteligência artificial possível?"

---

## [0:25 — 0:45] Subtítulo aparece com FadeIn

**ANIMAÇÃO:**
`FadeIn(Text("Como a matemática dá vida à IA", font_size=28))`
Subtítulo aparece suavemente abaixo do título principal. Uma linha horizontal fina surge entre eles.

**A2 (narração):**
> "A resposta está em uma área da matemática que você já conhece: a Álgebra Linear."
> "Vetores, matrizes, transformações — essas estruturas não são apenas teoria. Elas são o vocabulário operacional de toda IA moderna."

---

## [0:45 — 1:10] Ícones flutuantes ao redor do título

**ANIMAÇÃO:**
Ao redor do título, surgem pequenos elementos visuais com FadeIn em sequência:
- Um vetor com seta (canto inferior esquerdo)
- Uma grade de matriz 3×3 (canto inferior direito)
- O símbolo θ com um arco (canto superior esquerdo)
- A fórmula `Y = WX + b` (canto superior direito)

Cada elemento pulsa levemente como se estivesse vivo.

**A3 (narração):**
> "Nesta apresentação, vamos mostrar — visualmente — como conceitos da álgebra linear se tornam os blocos construtores do Machine Learning."
> "De vetores a redes neurais. De matrizes a decomposição SVD. Tudo conectado."

---

## [1:10 — 1:40] Pergunta central em destaque

**ANIMAÇÃO:**
O título e os ícones saem com FadeOut. Uma única pergunta surge no centro da tela, com `Write` animado em cor ciano:

```
"Como uma IA diferencia
um gato de um cachorro?"
```

Abaixo da pergunta, uma linha fina pulsa como um cursor aguardando resposta.

**A1 (narração):**
> "Vamos começar com uma pergunta simples: como uma inteligência artificial consegue diferenciar a foto de um gato da foto de um cachorro?"
> "A resposta a essa pergunta vai nos guiar por toda a apresentação."

---

---

# CENA 2 — VETORES
**Duração estimada: 2min 00s**
**Classe Manim:** `Vectors`

---

## [1:40 — 2:00] Plano cartesiano surge

**ANIMAÇÃO:**
`Create(NumberPlane())`
O plano cartesiano se expande a partir do centro, com linhas azuis sobre fundo escuro. Os eixos X e Y crescem primeiro, depois a grade se preenche suavemente.

**A2 (narração):**
> "Para que um computador processe qualquer dado — seja uma imagem, um texto ou um áudio — esse dado precisa ser convertido em números."
> "E esses números são organizados em vetores."

---

## [2:00 — 2:30] Vetor A surge

**ANIMAÇÃO:**
`GrowArrow(Vector([3, 2], color=BLUE))` + `Write(MathTex("A"))`
Uma seta azul cresce a partir da origem até o ponto (3, 2). A label "A" aparece na ponta do vetor.

**A2 (narração):**
> "Um vetor é simplesmente uma lista ordenada de números — uma direção e uma magnitude no espaço."
> "Aqui, o vetor A representa um ponto no plano com coordenadas 3 vírgula 2."

---

## [2:30 — 2:55] Vetor B surge

**ANIMAÇÃO:**
`GrowArrow(Vector([1, 4], color=GREEN))` + `Write(MathTex("B"))`
Uma seta verde cresce até (1, 4). A label "B" aparece acima da ponta.

**A2 (narração):**
> "E o vetor B representa outro ponto — coordenadas 1 vírgula 4."
> "No contexto de Machine Learning, cada uma dessas coordenadas pode representar uma característica de um dado."

---

## [2:55 — 3:20] Destaque nas coordenadas com boxes

**ANIMAÇÃO:**
Dois boxes coloridos surgem ao lado dos vetores listando:
- Vetor A: `[peso: 3, altura: 2]` (exemplo de features de um animal)
- Vetor B: `[peso: 1, altura: 4]`

As labels mudam de "A" e "B" para "Gato" e "Cachorro" com `Transform`.

**A3 (narração):**
> "Imagine que cada animal tem características mensuráveis: peso, altura, comprimento das orelhas..."
> "Cada conjunto de características forma um vetor. Um gato vira um ponto no espaço matemático. Um cachorro, outro ponto."
> "É assim que dados do mundo real se tornam algo que um algoritmo consegue processar."

---

## [3:20 — 3:40] Cena fecha com FadeOut e mensagem

**ANIMAÇÃO:**
Tudo some com FadeOut. Uma frase aparece centralizada:

`"Vetores = Representação matemática de dados"`

Com cor ciano, fonte grande, efeito de `Write`.

**A1 (narração):**
> "Vetores são a forma como traduzimos o mundo real para a linguagem da matemática. E tudo começa aqui."

---

---

# CENA 3 — MATRIZES
**Duração estimada: 1min 30s**
**Classe Manim:** `MatrixScene`

---

## [3:40 — 4:00] Título da cena

**ANIMAÇÃO:**
`Write(Text("Dados organizados em matrizes", font_size=32))`
Texto no topo da tela. Abaixo, o fundo escuro aguarda.

**A2 (narração):**
> "Um único vetor representa um dado. Mas em Machine Learning, trabalhamos com milhares — às vezes milhões — de dados ao mesmo tempo."
> "Como organizar tudo isso? Com matrizes."

---

## [4:00 — 4:30] Matriz 3×3 construída progressivamente

**ANIMAÇÃO:**
`Create(Matrix([[1,2,3],[4,5,6],[7,8,9]]))`
A matriz é criada com os colchetes e os números surgindo linha por linha. Os números aparecem com pequeno delay entre si para efeito visual.

**A2 (narração):**
> "Uma matriz é um arranjo retangular de números organizados em linhas e colunas."
> "Cada linha pode representar um dado — por exemplo, um animal com suas características."
> "Cada coluna representa uma característica — peso, altura, coloração..."

---

## [4:30 — 4:55] Labels nas linhas e colunas

**ANIMAÇÃO:**
Surgem labels com `FadeIn` nas laterais da matriz:
- Linhas: `Animal 1`, `Animal 2`, `Animal 3`
- Colunas: `Peso`, `Altura`, `Cor`

Uma seta destaca a linha 2 com `Indicate`.

**A3 (narração):**
> "No contexto prático: uma empresa de streaming tem uma matriz onde cada linha é um usuário e cada coluna é um filme assistido."
> "Uma rede neural carrega seus pesos em matrizes. Uma imagem de 100 por 100 pixels é uma matriz de 10 mil números."

---

## [4:55 — 5:10] Fechamento com frase

**ANIMAÇÃO:**
Matriz some. Frase central com `Write`:

`"Matrizes = Organização de grandes conjuntos de dados"`

**A1 (narração):**
> "Matrizes são o container padrão da álgebra linear. Tudo o que um modelo de Machine Learning aprende está armazenado nelas."

---

---

# CENA 4 — IMAGEM PARA MATRIZ
**Duração estimada: 1min 30s**
**Classe Manim:** `ImageToMatrix`

---

## [5:10 — 5:25] Quadrado colorido como "imagem"

**ANIMAÇÃO:**
`Write(Text("Imagens são matrizes numéricas", font_size=36))` no topo.
`FadeIn(Square(side_length=3, fill_color=BLUE, fill_opacity=1))` no centro.

**A1 (narração):**
> "Vamos entender como uma IA enxerga uma imagem."
> "Para nós, isso aqui é uma imagem. Para o computador, é outra coisa completamente diferente."

---

## [5:25 — 5:55] Transformação: imagem vira matriz

**ANIMAÇÃO:**
`Transform(image, Matrix([[255,120,90],[130,210,40],[10,50,180]]))`
A imagem se "dissolve" e se reorganiza na forma de uma matriz com valores numéricos. Os números surgem no lugar dos pixels, representando valores RGB.

**A2 (narração):**
> "Cada pixel de uma imagem é representado por um número — ou três números, no caso de imagens coloridas, representando os canais vermelho, verde e azul."
> "Uma imagem de 28 por 28 pixels — como as do dataset MNIST — é uma matriz de 784 números."

---

## [5:55 — 6:15] Zoom nos valores numéricos

**ANIMAÇÃO:**
Zoom em parte da matriz. Os valores 255, 130, 10 são destacados com `Indicate`. Uma label aparece: `"Intensidade do pixel (0 a 255)"`.

**A3 (narração):**
> "Quando você treina uma rede neural para reconhecer dígitos escritos à mão, você está alimentando a rede com essas matrizes de números."
> "A rede nunca 'vê' a imagem. Ela só processa os números."

---

## [6:15 — 6:40] Seta do processo

**ANIMAÇÃO:**
Uma sequência horizontal aparece no centro da tela com `Write` em cada etapa:

`Imagem` → `Pixels` → `Valores numéricos` → `Matriz` → `Algoritmo`

Cada item aparece com uma pequena pausa entre eles.

**A1 (narração):**
> "Esse processo — converter qualquer dado em representação matricial — é o primeiro passo de todo sistema de inteligência artificial."

---

---

# CENA 5 — SIMILARIDADE COSSENO
**Duração estimada: 2min 00s**
**Classe Manim:** `CosineSimilarity`

---

## [6:40 — 7:00] Plano cartesiano + fórmula

**ANIMAÇÃO:**
`Create(NumberPlane())`
`Write(MathTex(r"\cos(\theta)=\frac{A\cdot B}{||A||||B||}"))`

O plano surge primeiro. A fórmula aparece no topo com `Write`.

**A2 (narração):**
> "Agora que sabemos representar dados como vetores, surge uma pergunta fundamental:"
> "Como medir o quanto dois vetores se parecem? Como comparar dados matematicamente?"

---

## [7:00 — 7:20] Vetor A azul cresce

**ANIMAÇÃO:**
`GrowArrow(Vector([4, 2], color=BLUE))`
Vetor azul A cresce da origem até (4, 2).

**A2 (narração):**
> "Considere dois vetores no plano. O vetor A representa um texto sobre esportes."

---

## [7:20 — 7:40] Vetor B verde cresce + ângulo

**ANIMAÇÃO:**
`GrowArrow(Vector([3, 3], color=GREEN))`
`Create(Angle(vector_a, vector_b, radius=0.5))`

Vetor verde B cresce. Um arco com label θ aparece entre os dois vetores.

**A2 (narração):**
> "O vetor B representa outro texto — também sobre esportes, mas diferente."
> "O ângulo theta entre eles mede a similaridade. Quanto menor o ângulo, mais parecidos são os vetores."

---

## [7:40 — 8:10] Highlight na fórmula + explicação

**ANIMAÇÃO:**
A fórmula no topo é destacada com `Indicate`. Abaixo dela, surgem dois resultados:

```
θ ≈ 0°  →  cos(θ) = 1  →  "textos idênticos"
θ ≈ 90° →  cos(θ) = 0  →  "textos sem relação"
```

Cada linha aparece com `FadeIn` sequencial.

**A3 (narração):**
> "Essa medida se chama Similaridade Cosseno. É amplamente usada em sistemas de busca e recomendação."
> "Quando você pesquisa algo no Google, o algoritmo calcula a similaridade entre o seu vetor de busca e os vetores de milhões de documentos."
> "Os mais similares aparecem primeiro nos resultados."

---

## [8:10 — 8:40] Aplicações práticas aparecem

**ANIMAÇÃO:**
Os vetores somem. No centro da tela, três cards surgem com `FadeIn`:

- Card 1: `"NLP — Semântica de textos"`
- Card 2: `"Recomendação — Netflix, Spotify"`
- Card 3: `"Busca vetorial — Google, ChatGPT"`

Cada card tem um ícone simples e cor distinta.

**A3 (narração):**
> "Do ranking do Google às recomendações do Spotify — tudo usa variações dessa ideia: medir distância ou ângulo entre vetores."

---

---

# CENA 6 — TRANSFORMAÇÕES LINEARES
**Duração estimada: 1min 30s**
**Classe Manim:** `LinearTransformationExample`

---

## [8:40 — 9:00] Grade cartesiana inicial

**ANIMAÇÃO:**
`LinearTransformationScene` inicia com a grade do plano cartesiano e os vetores base i e j visíveis. Um vetor amarelo em (1, 2) surge com `add_vector`.

**A2 (narração):**
> "Até agora vimos vetores estáticos. Mas em Machine Learning, os dados passam por transformações."
> "Uma transformação linear é a ação de uma matriz sobre um espaço vetorial."

---

## [9:00 — 9:30] Transformação é aplicada

**ANIMAÇÃO:**
`apply_matrix([[1, 1], [0, 1]])`
A grade inteira se deforma — uma cisalhamento. O vetor amarelo se move para sua nova posição. Os vetores fantasma (ghost vectors) mostram a posição original em cinza.

**A2 (narração):**
> "Essa matriz representa uma transformação de cisalhamento. Observe como toda a grade se deforma — mas as linhas continuam paralelas, e a origem permanece fixa."
> "Isso é a definição de linearidade."

---

## [9:30 — 10:00] Conexão com camadas de rede neural

**ANIMAÇÃO:**
A grade para. No canto direito, surge uma representação simplificada de duas camadas de neurônios. Uma seta conecta a grade deformada à camada neural, com a label:

`"Cada camada aplica uma transformação linear"`

**A3 (narração):**
> "Cada camada de uma rede neural profunda aplica exatamente isso: uma transformação matricial nos dados."
> "Com dezenas de camadas, a rede vai distorcendo o espaço dos dados até que exemplos de classes diferentes fiquem linearmente separáveis."
> "É por isso que redes neurais profundas conseguem aprender padrões tão complexos."

---

---

# CENA 7 — REDE NEURAL
**Duração estimada: 1min 30s**
**Classe Manim:** `NeuralNetwork`

---

## [10:00 — 10:15] Título e conexões surgem

**ANIMAÇÃO:**
`Write(Text("Redes neurais usam operações matriciais", font_size=34))`
`Create(connections)` — as linhas de conexão entre neurônios aparecem primeiro, com opacidade baixa.

**A1 (narração):**
> "Chegamos ao coração do Machine Learning: a rede neural."

---

## [10:15 — 10:40] Neurônios surgem

**ANIMAÇÃO:**
`Create(layers)` — os círculos de cada camada surgem sobre as conexões. Três camadas: entrada (3 neurônios), oculta (4 neurônios), saída (2 neurônios).

**A2 (narração):**
> "Uma rede neural é organizada em camadas. A camada de entrada recebe os dados — no nosso exemplo, as características do animal."
> "As camadas ocultas processam essa informação por meio de operações matemáticas."
> "A camada de saída fornece a decisão: gato ou cachorro."

---

## [10:40 — 11:10] Fórmula Y = WX + b

**ANIMAÇÃO:**
`Write(MathTex("Y = WX + b"))`
A fórmula surge na parte inferior. Cada símbolo é destacado em sequência com `Indicate`:
- `X` em azul: `"entrada"`
- `W` em verde: `"pesos (matriz)"`
- `b` em amarelo: `"viés"`
- `Y` em vermelho: `"saída"`

**A2 (narração):**
> "A operação central é esta: Y igual a W X mais b."
> "X é o vetor de entrada. W é a matriz de pesos — os parâmetros aprendidos durante o treinamento."
> "b é o viés, e Y é o vetor de saída que passa para a próxima camada."

---

## [11:10 — 11:30] Fechamento

**ANIMAÇÃO:**
A rede neural some. Frase central com `Write`:

`"Treinar uma rede neural = ajustar os valores de W"`

**A3 (narração):**
> "O processo de treinamento ajusta iterativamente os valores da matriz W para minimizar os erros de classificação."
> "Álgebra linear está em cada passo desse processo."

---

---

# CENA 8 — DECOMPOSIÇÃO SVD
**Duração estimada: 1min 30s**
**Classe Manim:** `SVDScene`

---

## [11:30 — 11:50] Título e matriz original

**ANIMAÇÃO:**
`Write(Text("Decomposição SVD", font_size=36))`
`Create(Matrix([[5,3],[4,2]]))`

Uma matriz 2×2 surge ao centro. Destaque visual com bordas coloridas.

**A2 (narração):**
> "E se pudéssemos pegar uma matriz complexa e desmontá-la em partes mais simples e interpretáveis?"
> "Isso é exatamente o que a Decomposição em Valores Singulares — o SVD — faz."

---

## [11:50 — 12:20] Transformação: matriz vira três matrizes

**ANIMAÇÃO:**
`Transform(matrix_a, VGroup(matrix_u, sigma, vt))`
A matriz original se divide em três matrizes menores dispostas em linha: U, Σ, Vᵀ.
`Write(MathTex(r"A = U\Sigma V^T"))` aparece acima.

**A2 (narração):**
> "O SVD decompõe qualquer matriz A no produto de três matrizes: U, sigma e V transposto."
> "U captura as direções nos dados. Sigma contém a importância de cada direção. V transposto captura as relações entre variáveis."

---

## [12:20 — 12:50] Aplicações práticas

**ANIMAÇÃO:**
As três matrizes ficam ao fundo. Três bullets surgem à direita com `FadeIn`:

- `"Compressão de imagens"`
- `"Sistemas de recomendação"`
- `"Redução dimensional (PCA)"`

Uma animação mostra uma imagem sendo comprimida progressivamente, mantendo apenas os K maiores valores singulares.

**A3 (narração):**
> "Na prática: o Netflix usa SVD para modelar preferências de usuários e filmes como vetores em um espaço latente."
> "Aplicativos de compressão de imagem usam SVD para reduzir o tamanho dos arquivos mantendo a qualidade visual."
> "E o algoritmo PCA — fundamental em ciência de dados — é diretamente derivado do SVD."

---

## [12:50 — 13:00] Fechamento

**ANIMAÇÃO:**
Tudo some. Frase central:

`"SVD = Encontrar a estrutura essencial de qualquer matriz"`

**A1 (narração):**
> "A decomposição matricial é uma das ferramentas mais poderosas da álgebra linear aplicada."

---

---

# CENA 9 — CONCLUSÃO
**Duração estimada: 2min 00s**
**Classe Manim:** `Conclusion`

---

## [13:00 — 13:20] Frase central surge

**ANIMAÇÃO:**
`Write(Text("Dados → Matemática → Inteligência", font_size=42))`
O texto surge em três partes com pequena pausa entre cada elemento da sequência.

**A1 (narração):**
> "Chegamos ao fim da nossa apresentação. E a mensagem central é esta:"
> "Dados. Matemática. Inteligência. Essas três palavras resumem toda a cadeia da inteligência artificial moderna."

---

## [13:20 — 13:50] Subtítulo e recapitulação visual

**ANIMAÇÃO:**
`FadeIn(Text("A Álgebra Linear é a base do Machine Learning", font_size=30))`

Abaixo da frase central, surgem os conceitos cobertos em miniatura — como ícones em grade:

| Vetores | Matrizes | Imagens |
|---------|----------|---------|
| Cosine  | Transf.  | Redes   |
| SVD     |          |         |

Cada ícone pulsa suavemente com uma animação de `Flash`.

**A2 (narração):**
> "Vimos como vetores representam dados. Como matrizes organizam grandes conjuntos. Como imagens são grades numéricas."
> "Como a similaridade cosseno mede relações. Como transformações lineares moldam espaços. Como redes neurais aplicam álgebra em cada camada."
> "E como o SVD extrai a estrutura essencial de qualquer matriz."

---

## [13:50 — 14:20] Mensagem final — os quatro pilares

**ANIMAÇÃO:**
Os ícones somem. Quatro frases surgem em sequência, uma de cada vez, com `Write`:

1. `"Dados precisam ser matematicamente representados"`
2. `"Álgebra linear estrutura essa representação"`
3. `"Operações matriciais executam o processamento"`
4. `"Machine Learning depende diretamente dessas estruturas"`

Cada frase tem numeração em destaque e uma cor diferente.

**A3 (narração):**
> "Para resumir em quatro pontos:"
> "Primeiro: qualquer dado do mundo real precisa de representação matemática."
> "Segundo: a álgebra linear fornece as estruturas para essa representação."
> "Terceiro: operações matriciais são o motor computacional dos algoritmos."
> "Quarto: sem álgebra linear, o Machine Learning simplesmente não existiria."

---

## [14:20 — 14:50] Fechamento com créditos

**ANIMAÇÃO:**
As frases saem com FadeOut. Surge uma tela final minimalista:

- Nome do trabalho (fonte grande)
- Disciplina: Matemática Discreta
- Nomes dos apresentadores
- Logo da universidade (se disponível)

Animação de partículas de fundo retorna — espelhando a abertura.

**A1 (narração):**
> "Esta foi nossa apresentação sobre Álgebra Linear aplicada ao Machine Learning."
> "A matemática que muitas vezes parece abstrata na sala de aula é, na prática, a linguagem que ensina máquinas a pensar."

**A2 (narração):**
> "Obrigado pela atenção."

**A3 (narração):**
> "Ficamos à disposição para perguntas."

---

## [14:50 — 15:00] Fade out final

**ANIMAÇÃO:**
`FadeOut` de tudo. Tela preta por 3 segundos. Fim.

---

---

# Resumo de Distribuição de Falas

| Cena | A1 | A2 | A3 |
|------|----|----|----|
| 1 — Introdução | Abertura e pergunta central | Álgebra linear e estruturas | Visão geral da apresentação |
| 2 — Vetores | Fechamento conceitual | Definição matemática | Aplicação em ML |
| 3 — Matrizes | Fechamento conceitual | Definição e estrutura | Exemplos práticos |
| 4 — Imagem → Matriz | Motivação visual | Processo técnico | Aplicação em IA |
| 5 — Cosine Similarity | — | Definição matemática | Aplicações (NLP, busca) |
| 6 — Transf. Lineares | — | Definição e visualização | Conexão com redes neurais |
| 7 — Rede Neural | Introdução | Fórmula Y=WX+b | Treinamento |
| 8 — SVD | Fechamento | Definição e fórmula | Aplicações práticas |
| 9 — Conclusão | Abertura e encerramento | Recapitulação técnica | Os quatro pilares |

---

# Notas de Gravação

- **Formato sugerido:** gravação de voz individual por apresentador, sincronizada em edição
- **Tempo de fala:** cada apresentador fala por aproximadamente **5 minutos** no total
- **Ritmo:** pausas de 1–2 segundos entre falas de apresentadores diferentes para respiração narrativa
- **Tom:** didático, fluido, sem ser excessivamente formal — como uma explicação entre colegas
- **Sincronização:** cada bloco de fala deve começar no segundo indicado e terminar antes da próxima animação principal

---

# Comandos para Renderizar Cada Cena

```bash
manim -pqh main.py Intro
manim -pqh main.py Vectors
manim -pqh main.py MatrixScene
manim -pqh main.py ImageToMatrix
manim -pqh main.py CosineSimilarity
manim -pqh main.py LinearTransformationExample
manim -pqh main.py NeuralNetwork
manim -pqh main.py SVDScene
manim -pqh main.py Conclusion
```
