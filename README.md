# Álgebra Linear Aplicada ao Machine Learning

**Disciplina:** Matemática Discreta  
**Universidade Federal de Goiás**  
**Duração total:** ~12 min 45 s

---

## Apresentadoras

| Nome | Bloco |
|---|---|
| Milena Oliveira Penhalves | Introdução e Estruturas Fundamentais |
| Giovanna Borges Basso | Operações e Conceitos Centrais |
| Júlia Santos Coité | Redes Neurais, SVD e Conclusão |

---

## Sobre o Projeto

Apresentação acadêmica em vídeo que responde à pergunta:

> Como sistemas de Machine Learning conseguem transformar dados brutos em decisões inteligentes?

A narrativa demonstra que toda IA moderna depende diretamente da álgebra linear — da representação dos dados até o treinamento de redes neurais.

---

## Cenas

| # | Classe Manim | Arquivo | Apresentadora | Duração |
|---|---|---|---|---|
| 1 | `Intro` | `Intro.mp4` | Milena | ≈ 1 min 30 s |
| 2 | `ScalarsAndTensors` | `ScalarsAndTensors.mp4` | Milena | ≈ 2 min 30 s |
| 3 | `ImageToMatrix` | `ImageToMatrix.mp4` | Giovanna | ≈ 55 s |
| 4 | `TextAudioVectorization` | `TextAudioVectorization.mp4` | Giovanna | ≈ 50 s |
| 5 | `SimilarityMetrics` | `SimilarityMetrics.mp4` | Giovanna | ≈ 1 min 30 s |
| 6 | `LinearTransformationExample` | `LinearTransformationExample.mp4` | Giovanna | ≈ 1 min |
| 7 | `NeuralNetwork` | `NeuralNetwork.mp4` | Júlia | ≈ 1 min 45 s |
| 8 | `SVDScene` | `SVDScene.mp4` | Júlia | ≈ 1 min 15 s |
| 9 | `Conclusion` | `Conclusion.mp4` | Júlia | ≈ 1 min 30 s |

Os vídeos renderizados ficam em `media/videos/main/1080p60/`.

---

## Estrutura do Repositório

```
linear-algebraML/
├── main.py               # todas as cenas Manim
├── roteiro.md            # roteiro completo com falas e tempos
├── requirements.txt      # dependências Python
├── manim.cfg             # configuração padrão (quality = high_quality)
├── assets/
│   ├── cat.jpg           # usada na Intro e TextAudioVectorization
│   ├── dog.jpg           # usada na Intro e TextAudioVectorization
│   └── image.jpg         # usada na ImageToMatrix
├── docs/
│   └── *.pdf             # referências e roteiro original
└── media/
    └── videos/main/
        └── 1080p60/      # vídeos finais renderizados
```

---

## Tecnologias

| Ferramenta | Uso |
|---|---|
| Python 3.11+ | linguagem principal |
| Manim Community Edition | geração das animações |
| MiKTeX | renderização de LaTeX (MathTex, fórmulas) |
| FFmpeg | exportação de vídeo |
| Sony Vegas | edição final (opcional) |

---

## Instalação

```bash
pip install -r requirements.txt
```

MiKTeX e FFmpeg precisam ser instalados separadamente no sistema.

---

## Renderização

O arquivo `manim.cfg` já configura a qualidade como 1080p60 por padrão.

**Renderizar uma cena:**
```bash
manim main.py NomeDaCena
```

**Forçar qualidade explicitamente:**
```bash
manim -qh main.py NomeDaCena   # 1080p60
manim -ql main.py NomeDaCena   # 480p15 (rascunho)
```

**Renderizar todas as cenas:**
```bash
manim main.py Intro
manim main.py ScalarsAndTensors
manim main.py ImageToMatrix
manim main.py TextAudioVectorization
manim main.py SimilarityMetrics
manim main.py LinearTransformationExample
manim main.py NeuralNetwork
manim main.py SVDScene
manim main.py Conclusion
```

---

## Paleta de Cores

| Variável | Hex | Uso |
|---|---|---|
| `BG` | `#0D0D1A` | fundo escuro |
| `CYAN_C` | `#00D4FF` | destaques principais |
| `BLUE_C` | `#1E90FF` | vetores e geometria |
| `GREEN_C` | `#39D353` | segundo vetor / confirmações |
| `YELLOW_C` | `#FFD700` | ângulos e destaques |
| `PURPLE_C` | `#BB86FC` | fórmulas e rede neural |
| `GRAY_C` | `#8888AA` | textos secundários |
