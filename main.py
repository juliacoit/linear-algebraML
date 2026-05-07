from manim import *
import numpy as np

# ============================================
# CENA 1 — ABERTURA
# ============================================

class Intro(Scene):
    def construct(self):
        title = Text(
            "Álgebra Linear aplicada ao Machine Learning",
            font_size=42
        )

        subtitle = Text(
            "Como a matemática dá vida à IA",
            font_size=28
        ).next_to(title, DOWN)

        self.play(Write(title))
        self.play(FadeIn(subtitle))
        self.wait(2)


# ============================================
# CENA 2 — VETORES
# ============================================

class Vectors(Scene):
    def construct(self):
        plane = NumberPlane()

        vector1 = Vector([3, 2], color=BLUE)
        vector2 = Vector([1, 4], color=GREEN)

        label1 = MathTex("A")
        label1.next_to(vector1.get_end(), RIGHT)

        label2 = MathTex("B")
        label2.next_to(vector2.get_end(), UP)

        self.play(Create(plane))
        self.play(GrowArrow(vector1), Write(label1))
        self.play(GrowArrow(vector2), Write(label2))

        self.wait(2)


# ============================================
# CENA 3 — MATRIZES
# ============================================

class MatrixScene(Scene):
    def construct(self):
        matrix = Matrix([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ])

        text = Text("Dados organizados em matrizes", font_size=32)
        text.to_edge(UP)

        self.play(Write(text))
        self.play(Create(matrix))

        self.wait(2)


# ============================================
# CENA 4 — IMAGEM VIRANDO MATRIZ
# ============================================

class ImageToMatrix(Scene):
    def construct(self):
        title = Text("Imagens são matrizes numéricas", font_size=36)
        title.to_edge(UP)

        image = Square(side_length=3, fill_color=BLUE, fill_opacity=1)

        matrix = Matrix([
            [255, 120, 90],
            [130, 210, 40],
            [10, 50, 180]
        ])

        matrix.scale(0.8)

        self.play(Write(title))
        self.play(FadeIn(image))

        self.wait(1)

        self.play(
            Transform(image, matrix)
        )

        self.wait(2)


# ============================================
# CENA 5 — COSINE SIMILARITY
# ============================================

class CosineSimilarity(Scene):
    def construct(self):
        plane = NumberPlane()

        vector_a = Vector([4, 2], color=BLUE)
        vector_b = Vector([3, 3], color=GREEN)

        angle = Angle(vector_a, vector_b, radius=0.5)

        formula = MathTex(
            r"\cos(\theta)=\frac{A\cdot B}{||A||||B||}"
        )

        formula.to_edge(UP)

        self.play(Create(plane))
        self.play(Write(formula))

        self.play(GrowArrow(vector_a))
        self.play(GrowArrow(vector_b))

        self.play(Create(angle))

        self.wait(2)


# ============================================
# CENA 6 — TRANSFORMAÇÃO LINEAR
# ============================================

class LinearTransformationExample(LinearTransformationScene):
    def __init__(self, **kwargs):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True,
            **kwargs
        )

    def construct(self):
        matrix = [[1, 1],
                  [0, 1]]

        vector = Vector([1, 2], color=YELLOW)

        self.add_vector(vector)

        self.wait()

        self.apply_matrix(matrix)

        self.wait(2)


# ============================================
# CENA 7 — REDE NEURAL
# ============================================

class NeuralNetwork(Scene):
    def construct(self):
        title = Text("Redes neurais usam operações matriciais", font_size=34)
        title.to_edge(UP)

        layers = VGroup()

        positions = [-4, 0, 4]
        counts = [3, 4, 2]

        for x, count in zip(positions, counts):
            layer = VGroup()

            for i in range(count):
                neuron = Circle(radius=0.25)
                neuron.move_to([x, i - count/2, 0])
                layer.add(neuron)

            layers.add(layer)

        connections = VGroup()

        for i in range(len(layers)-1):
            for n1 in layers[i]:
                for n2 in layers[i+1]:
                    line = Line(
                        n1.get_center(),
                        n2.get_center(),
                        stroke_opacity=0.4
                    )
                    connections.add(line)

        formula = MathTex("Y = WX + b")
        formula.to_edge(DOWN)

        self.play(Write(title))
        self.play(Create(connections))
        self.play(Create(layers))
        self.play(Write(formula))

        self.wait(2)


# ============================================
# CENA 8 — SVD
# ============================================

class SVDScene(Scene):
    def construct(self):
        title = Text("Decomposição SVD", font_size=36)
        title.to_edge(UP)

        formula = MathTex(
            r"A = U\Sigma V^T"
        )

        matrix_a = Matrix([
            [5, 3],
            [4, 2]
        ])

        matrix_u = Matrix([
            [1, 0],
            [0, 1]
        ]).scale(0.6)

        sigma = Matrix([
            [7, 0],
            [0, 2]
        ]).scale(0.6)

        vt = Matrix([
            [1, 0],
            [0, 1]
        ]).scale(0.6)

        group = VGroup(matrix_u, sigma, vt)
        group.arrange(RIGHT, buff=1)
        group.move_to(DOWN)

        self.play(Write(title))
        self.play(Create(matrix_a))

        self.wait(1)

        self.play(
            Transform(matrix_a, group)
        )

        self.play(Write(formula))

        self.wait(2)


# ============================================
# CENA 9 — CONCLUSÃO
# ============================================

class Conclusion(Scene):
    def construct(self):
        text1 = Text(
            "Dados → Matemática → Inteligência",
            font_size=42
        )

        text2 = Text(
            "A Álgebra Linear é a base do Machine Learning",
            font_size=30
        )

        text2.next_to(text1, DOWN)

        self.play(Write(text1))
        self.play(FadeIn(text2))

        self.wait(3)