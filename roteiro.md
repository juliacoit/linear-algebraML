# Roteiro de Vídeo — Álgebra Linear Aplicada ao Machine Learning

**Disciplina:** Matemática Discreta  
**Duração total:** ~12 min 45 s  
**Formato:** narração em voz-over, tela 100% animada com Manim

---

## Apresentadoras

| Sigla | Nome                     | Bloco                                          |
|-------|--------------------------|------------------------------------------------|
| **M** | Milena Oliveira Penhalves| Introdução e Estruturas Fundamentais (~4 min)  |
| **G** | Giovanna Borges Basso    | Operações e Conceitos Centrais (~4 min)        |
| **J** | Júlia Santos Coité       | Redes Neurais, SVD, Aplicações e Conclusão (~4 min) |

---

## Tabela de tempos

| Apresentadora | Trecho                              | Tempo alvo    | Cena Manim                  | Arquivo de vídeo                                        |
|---------------|-------------------------------------|---------------|-----------------------------|---------------------------------------------------------|
| Milena        | Abertura e por que álgebra linear   | ≈ 1 min 30 s  | `Intro`                     | `Intro.mp4`                                             |
| Milena        | Escalar, vetor, matriz, tensor      | ≈ 2 min 30 s  | `ScalarsAndTensors`         | `ScalarsAndTensors.mp4`                                 |
| Giovanna      | Vetorização (imagem, texto, áudio)  | ≈ 1 min 45 s  | `ImageToMatrix` + `TextAudioVectorization` | `ImageToMatrix.mp4` + `TextAudioVectorization.mp4` |
| Giovanna      | Similaridade euclidiana e cosseno   | ≈ 1 min 30 s  | `SimilarityMetrics`         | `SimilarityMetrics.mp4`                                 |
| Giovanna      | Transformações lineares             | ≈ 1 min       | `LinearTransformationExample` | `LinearTransformationExample.mp4`                     |
| Júlia         | Redes neurais e Y = WX + b          | ≈ 1 min 45 s  | `NeuralNetwork`             | `NeuralNetwork.mp4`                                     |
| Júlia         | Redução de dimensionalidade (SVD)   | ≈ 1 min 15 s  | `SVDScene`                  | `SVDScene.mp4`                                          |
| Júlia         | Aplicações reais e conclusão        | ≈ 1 min 30 s  | `Conclusion`                | `Conclusion.mp4`                                        |
| **Total**     |                                     | **≈ 12 min 45 s** |                         |                                                         |

---

---

# BLOCO 1 — MILENA OLIVEIRA PENHALVES
## Introdução e Estruturas Fundamentais | ~4 min

---

## CENA 1 — INTRODUÇÃO
**Classe Manim:** `Intro`  
**Arquivo:** `Intro.mp4`  
**Duração:** ≈ 1 min 30 s

---

### [0:00 — 0:10] Tela escura + partículas surgindo

**ANIMAÇÃO:**  
`FadeIn(particles, lag_ratio=0.03)` — 90 pontos brancos surgem lentamente sobre o fundo `#0D0D1A`, como nós de uma rede.

**M:**
> "Quando você desbloqueia o celular pelo seu rosto, quando a Netflix sugere a próxima série antes mesmo de você procurar, quando o ChatGPT responde uma pergunta complexa em segundos — em todas essas situações há uma única disciplina matemática trabalhando por baixo dos panos."

---

### [0:10 — 0:28] Título principal surge

**ANIMAÇÃO:**  
`Write(title_line1)` — "Álgebra Linear aplicada ao"  
`Write(title_line2)` — "Machine Learning" (ciano bold)

**M:**
> "E essa disciplina é a álgebra linear."
> "Pode parecer estranho que algo tão abstrato esteja por trás de tecnologias tão sofisticadas, mas o motivo é simples. Máquinas não entendem o mundo. Elas entendem números."

---

### [0:28 — 0:48] Linha separadora + subtítulo + ícones flutuantes

**ANIMAÇÃO:**  
`Create(sep)` — linha horizontal ciano  
`FadeIn(subtitle)` — "Como a matemática dá vida à IA"  
`FadeIn(vec_group, mat_group, ang_group, nn_group)` — ícones nos 4 cantos

**M:**
> "E a álgebra linear é a ferramenta que transforma o mundo em números e os números em decisões inteligentes."
> "Eu sou Milena, e junto comigo estão Giovanna e Júlia. O tema é álgebra linear aplicada ao Machine Learning."

---

### [0:48 — 1:10] Todos os elementos somem. Pergunta central surge.

**ANIMAÇÃO:**  
`FadeOut(...)` de tudo.  
`Write(question)` — "Como uma IA diferencia / um gato de um cachorro?" em ciano, com cursor piscando.

**M:**
> "Vamos começar pela pergunta mais importante: por que álgebra linear?"
> "Todo sistema de aprendizado de máquina precisa fazer cinco coisas."

---

### [1:10 — 1:30] 5 bullets surgem em sequência

**ANIMAÇÃO:**  
A pergunta central some. 5 itens surgem em `LaggedStart` com `FadeIn`:

```
① Representar dados de forma numérica
② Organizar esses dados em estruturas
③ Transformar estruturas para extrair informação
④ Comparar informações para identificar padrões
⑤ Fazer tudo isso a bilhões de operações/segundo
```

Cada item aparece com `Write`, numeração em ciano.

**M:**
> "Primeiro, representar dados de forma numérica. Segundo, organizar esses dados em estruturas. Terceiro, transformar essas estruturas para extrair informação útil. Quarto, comparar informações entre si para identificar padrões. E quinto, fazer tudo isso em uma escala que envolve milhões — em alguns casos, bilhões — de operações por segundo."

---

### [1:30 — 1:35] Frase de fechamento do bloco introdutório

**ANIMAÇÃO:**  
Os bullets somem com `FadeOut`. Uma linha surge:

`"A álgebra linear é a única ferramenta matemática que faz as cinco coisas de maneira eficiente."`

Em branco, `Write`.

**M:**
> "A álgebra linear é a única ferramenta matemática que faz as cinco coisas de maneira eficiente. Por isso ela não é uma escolha de design dos engenheiros. Ela é uma necessidade computacional. Sem álgebra linear, o Machine Learning moderno simplesmente não existiria."

---

## CENA 2 — ESCALARES, VETORES, MATRIZES E TENSORES
**Classe Manim:** `ScalarsAndTensors`  
**Arquivo:** `ScalarsAndTensors.mp4`  
**Duração:** ≈ 2 min 30 s

---

### [1:35 — 1:50] Título da cena surge + card do Escalar

**ANIMAÇÃO:**  
`Write(title)` — "Estruturas da Álgebra Linear"  
`Write(sc_lbl)` + `Write(sc_val)` — "Escalar" e o número "3,7" em destaque  
`FadeIn(sc_ex)` — exemplos: temperatura, probabilidade, taxa de aprendizado

**M:**
> "Agora, para entender como ela funciona na prática, precisamos conhecer suas estruturas básicas. Temos quatro: escalar, vetor, matriz e tensor."
> "O escalar é a unidade mais simples. É apenas um número. Um único valor. A temperatura ambiente é um escalar. A probabilidade de uma previsão estar correta é um escalar. A taxa de aprendizado de um modelo — que define o quanto ele se ajusta a cada passo do treinamento — também é um escalar."

---

### [1:50 — 2:15] Card do Vetor surge ao lado do Escalar

**ANIMAÇÃO:**  
`Write(ve_lbl)` + `Create(ve_val)` — "Vetor" com a matriz coluna `[idade, altura, renda, ⋮]`  
`FadeIn(ve_ex)` — "características de um objeto"

**M:**
> "Quando juntamos vários escalares em uma sequência ordenada, temos um vetor. E é aqui que as coisas ficam interessantes. Um vetor pode representar qualquer objeto descrito por características numéricas. Uma pessoa, por exemplo, pode ser representada pelo vetor idade, altura, renda. Três posições, três características."
> "Mas você pode ter um vetor de cem posições para descrever um cliente de banco, ou um vetor de setecentas e sessenta e oito posições para representar o significado de uma palavra dentro de um modelo de linguagem moderno. Cada posição é uma característica, e o vetor inteiro descreve o objeto."

---

### [2:15 — 2:40] Card da Matriz surge

**ANIMAÇÃO:**  
`Write(ma_lbl)` + `Create(ma_val)` — "Matriz" com a grade 3×3  
`FadeIn(ma_ex)` — "conjunto de dados"

**M:**
> "Se um vetor descreve um objeto, uma matriz descreve um conjunto deles. Uma matriz é uma tabela bidimensional: linhas e colunas. Cada linha representa um objeto, cada coluna representa uma característica."
> "Quando o Spotify armazena os hábitos musicais de milhões de usuários, ele guarda isso em uma matriz. Quando uma rede neural armazena o conhecimento que aprendeu, esse conhecimento está em matrizes que chamamos de matrizes de pesos. Imagens em escala de cinza também são matrizes, porque cada posição corresponde à intensidade luminosa de um pixel."

---

### [2:40 — 3:10] Card do Tensor surge

**ANIMAÇÃO:**  
`Write(te_lbl)` + `FadeIn(te_stack)` — "Tensor" com 3 quadrados empilhados coloridos (R, G, B)  
`FadeIn(rgb_lbl)` — "R  G  B  (3 canais)"

**M:**
> "E quando precisamos de algo ainda mais complexo, usamos tensores. Um tensor é a generalização da matriz para qualquer número de dimensões. Uma imagem colorida, por exemplo, é um tensor de três dimensões: largura, altura e três canais de cor — vermelho, verde e azul. Um vídeo é um tensor de quatro dimensões, porque adicionamos o tempo."
> "Não é por acaso que as duas bibliotecas mais usadas no mundo para aprendizado profundo se chamam TensorFlow e PyTorch — toda operação dentro delas é, no fundo, uma operação sobre tensores."

---

### [3:10 — 3:30] Hierarquia final surge na parte inferior

**ANIMAÇÃO:**  
`Write` em sequência:  
`escalar → vetor → matriz → tensor`  
cada palavra na sua cor (ciano, azul, verde, amarelo).

**M:**
> "Agora temos as estruturas. Sabemos como guardar a informação. O próximo passo é entender o que fazer com ela. E é sobre isso que a Giovanna vai falar."

---

---

# BLOCO 2 — GIOVANNA BORGES BASSO
## Operações e Conceitos Centrais | ~4 min

---

## CENA 3 — VETORIZAÇÃO: IMAGEM, TEXTO, ÁUDIO
**Classes Manim:** `ImageToMatrix` + `TextAudioVectorization`  
**Arquivos:** `ImageToMatrix.mp4` + `TextAudioVectorization.mp4`  
**Duração:** ≈ 1 min 45 s

---

### [3:30 — 3:45] Transição — abertura da Giovanna

**ANIMAÇÃO:**  
A hierarquia da cena anterior some.  
Título "Vetorização de Dados" surge com `Write`.

**G:**
> "Tudo o que vimos até agora — escalares, vetores, matrizes, tensores — assume que os dados já são números. Mas o mundo real não é assim. Uma foto não é um número. Uma palavra não é um número. Um som não é um número. Então surge a pergunta: como traduzir o mundo real para a álgebra linear? Esse processo de tradução se chama vetorização."

---

### [3:45 — 4:15] Imagem → Pixels → Matriz (cena ImageToMatrix)

**ANIMAÇÃO:**  
`Write(title)` — "Imagens são matrizes numéricas"  
`FadeIn(image_group)` — quadrado azul representando uma imagem  
`ReplacementTransform(image_group, matrix)` — imagem se transforma em matriz de valores  
`Create(boxes)` + `FadeIn(intensity_label)` — destaque nos valores 0–255  
Pipeline final: `Imagem → Pixels → Valores → Matriz → Algoritmo`

**G:**
> "Vamos começar pelas imagens, porque é o caso mais simples de entender. Toda imagem digital é, na sua origem, uma grade de pixels. Cada pixel tem um valor de intensidade. Em uma imagem em escala de cinza, esse valor é um número entre zero e duzentos e cinquenta e cinco. Pretos são zero, brancos são duzentos e cinquenta e cinco, e os tons de cinza ficam no meio."
> "Uma foto de mil por mil pixels é, portanto, uma matriz com um milhão de números. Imagens coloridas vão um passo adiante: cada pixel tem três valores, um para vermelho, um para verde e um para azul — e a imagem inteira vira um tensor. Esse é o ponto de partida de toda a visão computacional moderna."

---

### [4:15 — 4:45] Texto → Embedding (cena TextAudioVectorization, seção 1)

**ANIMAÇÃO:**  
`Write(sec1)` — "Texto → Embedding"  
`Write('"gato"')` + `GrowArrow` + `Create(embed_vals)` — palavra vira vetor de 768 dimensões  
`Create(axes)` + pontos coloridos — "gato" e "cachorro" próximos, "mesa" distante  
`Create(prox_line)` — linha tracejada entre gato e cachorro

**G:**
> "Com texto, o problema é mais sutil. Como representar a palavra gato como número? Atribuir o número um para gato e dois para cachorro não funciona, porque a matemática vai concluir que cachorro é o dobro de gato — o que não faz sentido nenhum."
> "A solução foi inventar os embeddings. Um embedding é um vetor numérico em que palavras com significados parecidos ficam matematicamente próximas no espaço. Um bom embedding coloca gato e cachorro próximos, porque ambos são animais domésticos, e deixa mesa distante dos dois. É essa representação que permite que modelos de linguagem entendam o sentido do que estão lendo, e não apenas as letras."

---

### [4:45 — 5:15] Áudio → Fourier → Espectrograma (seção 2)

**ANIMAÇÃO:**  
`Write(sec2)` — "Áudio → Matriz de Frequências"  
`Create(wave_axes)` + `Create(wave_curve)` — onda senoidal representando som  
`GrowArrow(arr1)` + `FadeIn(steps)` — etapas: ① amostrar, ② Fourier  
`GrowArrow(arr2)` + `Create(freq_matrix)` — matriz de espectrograma

**G:**
> "Áudio segue uma lógica parecida. Som é onda — uma variação de pressão no ar. Quando o microfone captura um som, ele amostra essa onda em milhares de pontos por segundo, gerando uma sequência longa de números."
> "Em seguida, uma técnica matemática chamada Transformada de Fourier converte essa sequência em uma representação no domínio da frequência, gerando uma matriz que mostra quais frequências aparecem em cada instante. É essa matriz que um sistema de reconhecimento de voz analisa para entender o que você disse."

---

## CENA 4 — MÉTRICAS DE SIMILARIDADE
**Classe Manim:** `SimilarityMetrics`  
**Arquivo:** `SimilarityMetrics.mp4`  
**Duração:** ≈ 1 min 30 s

---

### [5:15 — 5:25] Abertura da seção

**ANIMAÇÃO:**  
A cena de vetorização termina. `Write(title)` — "Métricas de Similaridade".

**G:**
> "Beleza. Os dados viraram números. Mas isso, por si só, não basta. Precisamos comparar esses números — descobrir se duas imagens são parecidas, se dois textos tratam do mesmo assunto, se dois usuários têm gostos semelhantes. Para isso usamos métricas de similaridade. E duas delas são fundamentais."

---

### [5:25 — 5:55] Distância euclidiana

**ANIMAÇÃO:**  
`Write(sec1)` — "Distância Euclidiana"  
`Create(plane1)` — plano cartesiano  
`FadeIn(dot_a, dot_b)` + `Create(dist_line)` + `Create(dist_brace)` — linha entre dois pontos A e B  
`Write(euc_formula)` — d = √Σ(aᵢ − bᵢ)²  
`FadeIn(use1)` — casos de uso: agrupamento, anomalias, classificação

**G:**
> "A primeira é a distância euclidiana. Ela é, basicamente, a generalização para muitas dimensões da régua que usamos no plano cartesiano. Dados dois vetores, subtraímos um do outro, elevamos ao quadrado cada diferença, somamos tudo e tiramos a raiz quadrada. Quanto menor o resultado, mais próximos os vetores estão."
> "Essa métrica funciona bem quando os dados estão na mesma escala e a noção de distância é apropriada — agrupamento de clientes parecidos, classificação de plantas pelas suas medidas, detecção de anomalias em sensores. É uma das métricas mais antigas e mais usadas em aprendizado de máquina."

---

### [5:55 — 6:40] Similaridade de cosseno

**ANIMAÇÃO:**  
Distância some. `Write(sec2)` — "Similaridade de Cosseno"  
`Create(plane2)` + `Write(cos_formula)`  
`GrowArrow(vec_a)` + `GrowArrow(vec_b)` — dois vetores  
`Create(angle)` + `Write(theta_lbl)` — arco com θ entre eles  
Vetores somem. 3 casos surgem em sequência:  
`θ ≈ 0° → cos = 1 → idênticos` (verde)  
`θ ≈ 90° → cos = 0 → sem relação` (amarelo)  
`θ ≈ 180° → cos = −1 → opostos` (vermelho)  
`FadeIn(use2)` — busca semântica, recomendação, LLMs

**G:**
> "A segunda é a similaridade de cosseno. Em vez de medir a distância entre dois vetores, ela mede o ângulo entre eles. O resultado vai de menos um a mais um. Quando dois vetores apontam exatamente para a mesma direção, o cosseno entre eles é um — temos similaridade máxima. Quando são perpendiculares, o cosseno é zero — não há relação. Quando apontam para direções opostas, o cosseno é menos um."
> "A similaridade de cosseno é particularmente útil quando o tamanho do vetor não importa, só a direção. E esse é exatamente o caso dos embeddings de texto. Dois documentos podem ter tamanhos muito diferentes, mas tratar do mesmo assunto. A distância euclidiana entre eles seria enorme, mas o cosseno seria próximo de um. Por isso, essa é a métrica padrão por trás da busca semântica, dos sistemas de recomendação modernos e dos grandes modelos de linguagem."

---

## CENA 5 — TRANSFORMAÇÕES LINEARES
**Classe Manim:** `LinearTransformationExample`  
**Arquivo:** `LinearTransformationExample.mp4`  
**Duração:** ≈ 1 min

---

### [6:40 — 7:00] Grade surge com título e label da matriz

**ANIMAÇÃO:**  
`LinearTransformationScene` inicia a grade.  
`add_foreground_mobjects(title, matrix_label)` — "Transformações Lineares" e M aparecem estáticos.  
`add_vector(vec)` — vetor amarelo (2, 1) cresce.

**G:**
> "Agora chegamos ao último conceito desta seção, que é o mais importante de todos: a transformação linear. Uma transformação linear é uma função que recebe um vetor e devolve outro vetor, obedecendo a duas regras: ela preserva a origem do espaço, e ela preserva linhas retas."
> "Pode parecer abstrato, mas existem quatro exemplos clássicos que todo mundo já viu visualmente: rotação, que gira o vetor; escala, que aumenta ou diminui seu tamanho; cisalhamento, que inclina o espaço; e projeção, que joga o vetor sobre um eixo ou um plano."

---

### [7:00 — 7:30] Cisalhamento aplicado + caixa explicativa

**ANIMAÇÃO:**  
`apply_matrix([[1, 1], [0, 1]])` — toda a grade se deforma (cisalhamento).  
O vetor amarelo se move mostrando sua posição original em cinza (ghost vector).  
`FadeIn(note)` — caixa: "Cada camada de uma rede neural aplica uma transformação M·x"

**G:**
> "E por que isso importa? Porque cada camada de uma rede neural é, no fundo, uma transformação linear seguida de uma operação não linear. Os dados entram em um formato — uma foto, por exemplo — e, camada por camada, são transformados em representações cada vez mais úteis até chegarem ao formato final, que é a previsão."
> "O aprendizado do qual tanto se fala em Machine Learning é, na prática, descobrir quais transformações lineares fazem essa tradução funcionar. E é exatamente sobre isso que a Júlia vai falar a seguir."

---

---

# BLOCO 3 — JÚLIA SANTOS COITÉ
## Redes Neurais, SVD, Aplicações e Conclusão | ~4 min

---

## CENA 6 — REDES NEURAIS E Y = WX + b
**Classe Manim:** `NeuralNetwork`  
**Arquivo:** `NeuralNetwork.mp4`  
**Duração:** ≈ 1 min 45 s

---

### [7:30 — 7:45] Abertura + rede surge

**ANIMAÇÃO:**  
`Write(title)` — "Redes neurais usam operações matriciais"  
`Create(connections)` — linhas de conexão entre neurônios  
`Create(layers)` — 3 camadas: entrada (3), oculta (4), saída (2)  
`FadeIn(layer_labels)` — "Entrada (X)", "Camadas ocultas", "Saída (Y)"

**J:**
> "Obrigado, Giovanna. Tudo o que vimos até agora — estruturas, vetorização, similaridade, transformações — converge em uma única coisa: as redes neurais. E o coração de toda rede neural é uma equação muito simples: Y igual a W vezes X, mais b."
> "Essa equação parece pequena, mas é a fórmula que move o mundo do aprendizado profundo. Vou destrinchar cada termo."

---

### [7:45 — 8:20] Fórmula Y = WX + b com destaques

**ANIMAÇÃO:**  
`Write(formula)` — Y = WX + b em fonte grande (52pt)  
`Indicate(formula[3], BLUE_C)` — X em azul  
`Indicate(formula[2], GREEN_C)` — W em verde  
`Indicate(formula[5], PURPLE_C)` — b em roxo  
`Indicate(formula[0], YELLOW_C)` — Y em amarelo  
`FadeIn(legend)` — caixa com legenda X/W/b/Y e seus significados

**J:**
> "X é a entrada. Pode ser o vetor que representa um cliente, os pixels de uma imagem, o embedding de uma palavra. Qualquer dado que queiramos processar vira X."
> "W é a matriz de pesos. E é nessa matriz que mora todo o conhecimento que a rede aprendeu. Cada número dentro de W foi ajustado para fazer a rede tomar decisões corretas."
> "b é o viés, do inglês bias. É um pequeno ajuste que dá flexibilidade à rede, permitindo que ela aprenda padrões que não passariam exatamente pela origem do espaço."
> "E Y é a saída. A previsão. O que a rede entrega no final."

---

### [8:20 — 9:15] Fechamento com mensagem + escala do GPT-4

**ANIMAÇÃO:**  
A rede e a fórmula somem.  
`Write(closing)` — "Treinar uma rede neural = ajustar os valores de W"

**J:**
> "Quando multiplicamos W por X, estamos aplicando uma transformação linear nos dados de entrada. Quando somamos b, deslocamos o resultado. E esse processo se repete em cada camada da rede."
> "Modelos modernos como o GPT-4 têm centenas de camadas com bilhões de parâmetros nessas matrizes W. O que significa treinar uma rede neural? Significa ajustar, repetidamente, os números dentro de cada matriz W até que a saída Y fique tão próxima quanto possível do resultado correto."
> "Cada vez que você usa o ChatGPT, bilhões dessas operações estão acontecendo em frações de segundo."

---

## CENA 7 — DECOMPOSIÇÃO SVD
**Classe Manim:** `SVDScene`  
**Arquivo:** `SVDScene.mp4`  
**Duração:** ≈ 1 min 15 s

---

### [9:15 — 9:35] Matriz A surge + contexto do problema

**ANIMAÇÃO:**  
`Write(title)` — "Decomposição SVD"  
`Write(lbl_a)` + `Create(mat_a)` — A = [[5,3],[4,2]]

**J:**
> "Mas há um problema prático com tudo isso. Dados modernos têm muitas dimensões. Uma imagem de qualidade tem centenas de milhares de pixels. Um embedding de palavra pode ter centenas ou milhares de posições. E quando combinamos tudo isso em modelos grandes, chegamos rapidamente a bilhões de números. Processar tudo isso diretamente seria computacionalmente impossível."
> "A álgebra linear resolve esse problema com técnicas de redução de dimensionalidade. A mais importante delas é a Decomposição em Valores Singulares — em inglês, Singular Value Decomposition, ou SVD."

---

### [9:35 — 10:00] Matriz se decompõe em U, Σ, Vᵀ

**ANIMAÇÃO:**  
`ReplacementTransform(group_a, decomposed)` — A se divide em U × Σ × Vᵀ  
`Write(formula_svd)` — A = UΣVᵀ surge no topo

**J:**
> "O que o SVD faz, em essência, é pegar uma matriz grande e decompor em três matrizes menores. O produto dessas três matrizes aproxima a original, mas com muito menos informação. As partes mais importantes dos dados são preservadas, e o ruído é descartado. Isso permite comprimir dados, extrair padrões escondidos e construir sistemas inteligentes."

---

### [10:00 — 10:30] Aplicações práticas

**ANIMAÇÃO:**  
Matrizes somem. `Write(apps_title)` — "Aplicações do SVD"  
`FadeIn` em sequência:
- Compressão de imagens
- Sistemas de recomendação (Netflix)
- Redução dimensional (PCA)
- Embeddings compactos em NLP

**J:**
> "A aplicação clássica do SVD é o sistema de recomendação. Imagine uma matriz enorme: as linhas são usuários da Netflix, as colunas são filmes, e o valor em cada célula é a nota que aquele usuário deu àquele filme. Essa matriz tem dezenas de milhões de linhas e milhares de colunas, e a maior parte dela está em branco — nenhum usuário assistiu a todos os filmes."
> "O SVD descobre padrões escondidos nessa matriz. Ele percebe que existem gêneros latentes, perfis de gosto, conexões sutis entre usuários e filmes. É assim que a Netflix recomenda algo que você nunca viu, mas que combina com o que você gosta."

---

## CENA 8 — APLICAÇÕES E CONCLUSÃO
**Classe Manim:** `Conclusion`  
**Arquivo:** `Conclusion.mp4`  
**Duração:** ≈ 1 min 30 s

---

### [10:30 — 10:50] Partículas + frase central colorida

**ANIMAÇÃO:**  
`FadeIn(particles, lag_ratio=0.03)` — espelho da abertura  
`Write(phrase)` em sequência: **Dados** → **Matemática** → **Inteligência**  
`FadeIn(subtitle)` — "A Álgebra Linear é a base do Machine Learning"

**J:**
> "E é exatamente esse conjunto de ferramentas matemáticas que está por trás de praticamente todas as tecnologias inteligentes que conhecemos hoje. Os modelos de linguagem da OpenAI são, no fundo, milhões de operações com matrizes acontecendo a cada palavra gerada. As recomendações da Netflix e as playlists do Spotify usam decomposições e similaridade vetorial. A busca do Google moderna é movida por embeddings comparados por similaridade de cosseno. Reconhecimento facial, diagnóstico médico por imagem, carros autônomos, tradutores automáticos — em todos eles, a base matemática é a mesma."

---

### [10:50 — 11:20] Mini-ícones de recap + flash

**ANIMAÇÃO:**  
`FadeIn` dos 7 cards em grade (Vetores, Matrizes, Imagens, Similaridade, Transf. Lin., Redes Neurais, SVD)  
`Flash` em cada card em sequência

**J:**
> "A álgebra linear é, em última análise, a linguagem que torna o aprendizado de máquina possível. Ela representa o mundo em forma de dados, organiza esses dados em estruturas computáveis, transforma essas estruturas em informação útil, e mede as relações entre tudo isso."
> "Em uma frase: ela transforma dados em estrutura, estrutura em computação, e computação em inteligência."

---

### [11:20 — 12:00] Os quatro pilares surgem

**ANIMAÇÃO:**  
`Write(pillars_title)` — "Em síntese:"  
4 linhas surgem com `FadeIn` em sequência:  
`1` (ciano) — "Dados precisam ser matematicamente representados"  
`2` (verde) — "Álgebra linear estrutura essa representação"  
`3` (amarelo) — "Operações matriciais executam o processamento"  
`4` (roxo) — "Machine Learning depende diretamente dessas estruturas"

**J:**
> "Por isso, compreender álgebra linear não é apenas estudar uma área da matemática. É compreender os fundamentos da inteligência artificial moderna — a tecnologia que está redefinindo o século vinte e um."

---

### [12:00 — 12:45] Créditos finais + fade out

**ANIMAÇÃO:**  
Os pilares somem. Partículas somem. Créditos surgem com `LaggedStart`:

```
Álgebra Linear aplicada ao Machine Learning
Disciplina: Matemática Discreta
Universidade Federal de Goiás
Júlia Santos Coité
Giovanna Borges Basso
Milena Oliveira Penhalves
```

`FadeOut(credits)` — tela preta.

**J:**
> "Muito obrigado por assistirem."

*(Silêncio de 3 segundos. Fade out.)*

---

---

# Notas de Gravação

- **Ritmo:** pausas de 1–2 s entre trocas de apresentadora para respiração narrativa
- **Tom:** didático e fluido — como explicar para colegas de graduação
- **Sincronização:** cada fala começa no segundo indicado acima e deve terminar antes da animação seguinte
- **Corte de tempo:** se passar de 13 min nos ensaios, cortar exemplos antes de cortar conceitos
- **Texto do PDF:** as falas acima reproduzem exatamente o roteiro do arquivo `docs/Roteiro_Algebra_Linear_ML.pdf`

---

# Comandos de Renderização

```bash
# Cenas originais
manim -pqh main.py Intro
manim -pqh main.py Vectors
manim -pqh main.py MatrixScene
manim -pqh main.py ImageToMatrix
manim -pqh main.py LinearTransformationExample
manim -pqh main.py NeuralNetwork
manim -pqh main.py SVDScene
manim -pqh main.py Conclusion

# Cenas novas (adicionadas após mesclagem com o PDF)
manim -pqh main.py ScalarsAndTensors
manim -pqh main.py TextAudioVectorization
manim -pqh main.py SimilarityMetrics
```
