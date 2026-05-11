from manim import *
import numpy as np

# ==============================================================
# PALETA DE CORES DO PROJETO
# ==============================================================

BG       = "#0D0D1A"   # Fundo escuro
CYAN_C   = "#00D4FF"   # Ciano  — destaques principais
BLUE_C   = "#1E90FF"   # Azul   — vetores e elementos geométricos
GREEN_C  = "#39D353"   # Verde  — segundo vetor / confirmações
YELLOW_C = "#FFD700"   # Amarelo — destaques e ângulos
PURPLE_C = "#BB86FC"   # Roxo   — fórmulas e rede neural
GRAY_C   = "#8888AA"   # Cinza  — textos secundários


# ==============================================================
# CENA 1 — INTRODUÇÃO
# Duração: ~1min 40s
# ==============================================================

class Intro(Scene):
    def construct(self):
        self.camera.background_color = BG

        # ── Partículas de fundo ──────────────────────────────
        np.random.seed(42)
        particles = VGroup(*[
            Dot(
                point=[
                    np.random.uniform(-6.5, 6.5),
                    np.random.uniform(-3.5, 3.5),
                    0,
                ],
                radius=np.random.uniform(0.02, 0.05),
                color=WHITE,
            ).set_opacity(np.random.uniform(0.15, 0.55))
            for _ in range(90)
        ])
        self.play(FadeIn(particles, lag_ratio=0.03), run_time=1.5)

        # ── Título principal ─────────────────────────────────
        title_line1 = Text(
            "Álgebra Linear aplicada ao",
            font_size=38,
            color=WHITE,
        )
        title_line2 = Text(
            "Machine Learning",
            font_size=50,
            color=CYAN_C,
            weight=BOLD,
        )
        title_group = VGroup(title_line1, title_line2).arrange(DOWN, buff=0.25)

        self.play(Write(title_line1), run_time=1.2)
        self.play(Write(title_line2), run_time=1.0)

        # ── Linha separadora + subtítulo ─────────────────────
        sep = Line(LEFT * 4, RIGHT * 4, color=CYAN_C, stroke_width=1)
        sep.next_to(title_group, DOWN, buff=0.35)

        subtitle = Text(
            "Como a matemática dá vida à IA",
            font_size=26,
            color=GRAY_C,
        ).next_to(sep, DOWN, buff=0.25)

        self.play(Create(sep), run_time=0.5)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=0.8)
        self.wait(0.8)

        # ── Ícones flutuantes ────────────────────────────────
        vec_arrow = Arrow(ORIGIN, RIGHT * 0.9 + UP * 0.5, color=BLUE_C,
                          buff=0, stroke_width=3)
        vec_text  = Text("vetor", font_size=15, color=BLUE_C).next_to(vec_arrow, DOWN, buff=0.1)
        vec_group = VGroup(vec_arrow, vec_text).move_to([-5.5, -2.3, 0])

        mat_icon  = Matrix([[1, 2], [3, 4]], h_buff=0.55, v_buff=0.55).scale(0.38)
        mat_text  = Text("matriz", font_size=15, color=GREEN_C).next_to(mat_icon, DOWN, buff=0.1)
        mat_group = VGroup(mat_icon, mat_text).move_to([5.5, -2.3, 0])

        ang_icon  = MathTex(r"\theta", font_size=42, color=YELLOW_C)
        ang_text  = Text("ângulo", font_size=15, color=YELLOW_C).next_to(ang_icon, DOWN, buff=0.1)
        ang_group = VGroup(ang_icon, ang_text).move_to([-5.5, 2.3, 0])

        nn_icon   = MathTex("Y = WX + b", font_size=22, color=PURPLE_C)
        nn_text   = Text("rede neural", font_size=15, color=PURPLE_C).next_to(nn_icon, DOWN, buff=0.1)
        nn_group  = VGroup(nn_icon, nn_text).move_to([5.5, 2.3, 0])

        self.play(
            FadeIn(vec_group, shift=UP * 0.15),
            FadeIn(mat_group, shift=UP * 0.15),
            FadeIn(ang_group, shift=DOWN * 0.15),
            FadeIn(nn_group,  shift=DOWN * 0.15),
            lag_ratio=0.25,
            run_time=1.2,
        )
        self.wait(1.0)

        # ── Transição para pergunta central ──────────────────
        self.play(
            FadeOut(title_group),
            FadeOut(sep),
            FadeOut(subtitle),
            FadeOut(vec_group),
            FadeOut(mat_group),
            FadeOut(ang_group),
            FadeOut(nn_group),
            FadeOut(particles),
            run_time=0.8,
        )

        question = Text(
            "Como uma IA diferencia\num gato de um cachorro?",
            font_size=44,
            color=CYAN_C,
            line_spacing=1.5,
        )
        self.play(Write(question), run_time=2.2)

        # cursor piscando
        cursor = Rectangle(
            width=0.12, height=0.55,
            color=CYAN_C, fill_opacity=1, stroke_width=0,
        ).next_to(question, DOWN, buff=0.4)
        self.play(FadeIn(cursor))
        self.play(FadeOut(cursor), run_time=0.35)
        self.play(FadeIn(cursor),  run_time=0.35)
        self.wait(0.6)

        self.play(FadeOut(question), FadeOut(cursor), run_time=0.8)


# ==============================================================
# CENA 2 — VETORES
# Duração: ~2min
# ==============================================================

class Vectors(Scene):
    def construct(self):
        self.camera.background_color = BG

        # ── Plano cartesiano ─────────────────────────────────
        plane = NumberPlane(
            background_line_style={
                "stroke_color": BLUE_E,
                "stroke_opacity": 0.3,
            },
            axis_config={"stroke_color": GRAY_C, "stroke_opacity": 0.8},
        )
        self.play(Create(plane), run_time=1.5)

        # ── Vetor A ──────────────────────────────────────────
        vector_a = Vector([3, 2], color=BLUE_C, stroke_width=5)
        label_a  = MathTex(r"\vec{A}", color=BLUE_C, font_size=36)
        label_a.next_to(vector_a.get_end(), UR, buff=0.15)

        self.play(GrowArrow(vector_a), Write(label_a))

        # ── Vetor B ──────────────────────────────────────────
        vector_b = Vector([1, 4], color=GREEN_C, stroke_width=5)
        label_b  = MathTex(r"\vec{B}", color=GREEN_C, font_size=36)
        label_b.next_to(vector_b.get_end(), UL, buff=0.15)

        self.play(GrowArrow(vector_b), Write(label_b))
        self.wait(0.8)

        # ── Boxes com features ───────────────────────────────
        def feature_box(lines, color, pos):
            rect  = Rectangle(
                width=2.9, height=1.7, color=color,
                stroke_width=1.5, fill_opacity=0.1, fill_color=color,
            )
            texts = VGroup(*[
                Text(t, font_size=17, color=WHITE) for t in lines
            ]).arrange(DOWN, buff=0.18)
            texts.move_to(rect)
            return VGroup(rect, texts).move_to(pos)

        box_a = feature_box(["Peso:  3 kg", "Altura: 2 dm"], BLUE_C,  [-4.6, -1.6, 0])
        box_b = feature_box(["Peso:  1 kg", "Altura: 4 dm"], GREEN_C, [ 4.6, -1.6, 0])

        self.play(FadeIn(box_a), FadeIn(box_b), run_time=0.8)

        # ── Labels: A/B → Gato/Cachorro ──────────────────────
        label_a_new = Text("Gato",     font_size=22, color=BLUE_C)
        label_a_new.next_to(vector_a.get_end(), UR, buff=0.15)

        label_b_new = Text("Cachorro", font_size=22, color=GREEN_C)
        label_b_new.next_to(vector_b.get_end(), UL, buff=0.15)

        self.play(
            Transform(label_a, label_a_new),
            Transform(label_b, label_b_new),
            run_time=0.8,
        )
        self.wait(1.0)

        # ── Fechamento ───────────────────────────────────────
        self.play(
            FadeOut(plane), FadeOut(vector_a), FadeOut(vector_b),
            FadeOut(label_a), FadeOut(label_b),
            FadeOut(box_a),   FadeOut(box_b),
            run_time=0.8,
        )
        closing = Text(
            "Vetores = Representação matemática de dados",
            font_size=34, color=CYAN_C,
        )
        self.play(Write(closing), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(closing))


# ==============================================================
# CENA 3 — MATRIZES
# Duração: ~1min 30s
# ==============================================================

class MatrixScene(Scene):
    def construct(self):
        self.camera.background_color = BG

        # ── Título ───────────────────────────────────────────
        title = Text("Dados organizados em matrizes", font_size=34, color=WHITE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1.0)

        # ── Matriz 3×3 ───────────────────────────────────────
        matrix = Matrix(
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            h_buff=1.0, v_buff=0.8,
        ).set_color(WHITE)

        self.play(Create(matrix), run_time=1.5)
        self.wait(0.5)

        # ── Labels nas linhas ────────────────────────────────
        row_labels = VGroup(
            Text("Animal 1", font_size=18, color=BLUE_C),
            Text("Animal 2", font_size=18, color=BLUE_C),
            Text("Animal 3", font_size=18, color=BLUE_C),
        )
        for i, lbl in enumerate(row_labels):
            lbl.next_to(matrix.get_rows()[i], LEFT, buff=0.5)

        # ── Labels nas colunas ───────────────────────────────
        col_labels = VGroup(
            Text("Peso",   font_size=18, color=GREEN_C),
            Text("Altura", font_size=18, color=GREEN_C),
            Text("Cor",    font_size=18, color=GREEN_C),
        )
        for i, lbl in enumerate(col_labels):
            lbl.next_to(matrix.get_columns()[i], UP, buff=0.4)

        self.play(
            LaggedStart(*[FadeIn(l) for l in row_labels], lag_ratio=0.3),
            LaggedStart(*[FadeIn(l) for l in col_labels], lag_ratio=0.3),
            run_time=1.0,
        )

        # ── Destaque na linha 2 ──────────────────────────────
        self.play(Indicate(matrix.get_rows()[1], color=YELLOW_C, scale_factor=1.1))
        self.wait(0.8)

        # ── Fechamento ───────────────────────────────────────
        self.play(
            FadeOut(matrix), FadeOut(row_labels),
            FadeOut(col_labels), FadeOut(title),
            run_time=0.8,
        )
        closing = Text(
            "Matrizes = Organização de grandes conjuntos de dados",
            font_size=28, color=CYAN_C,
        )
        self.play(Write(closing), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(closing))


# ==============================================================
# CENA 4 — IMAGEM PARA MATRIZ
# Duração: ~1min 30s
# ==============================================================

class ImageToMatrix(Scene):
    def construct(self):
        self.camera.background_color = BG

        # ── Título ───────────────────────────────────────────
        title = Text("Imagens são matrizes numéricas", font_size=36, color=WHITE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1.0)

        # ── "Imagem" representada como quadrado ──────────────
        image_rect = Square(
            side_length=3.2, color=BLUE_C,
            fill_color=BLUE_C, fill_opacity=0.85,
        )
        pixel_label = Text("Imagem\n(pixels)", font_size=22, color=WHITE)
        pixel_label.move_to(image_rect)
        image_group = VGroup(image_rect, pixel_label)

        self.play(FadeIn(image_group, scale=0.85), run_time=0.8)
        self.wait(0.8)

        # ── Transformação: imagem → valores numéricos ────────
        matrix = Matrix(
            [[255, 120, 90], [130, 210, 40], [10, 50, 180]],
            h_buff=1.1, v_buff=0.8,
        ).set_color(WHITE).scale(0.85)

        self.play(
            ReplacementTransform(image_group, matrix),
            run_time=1.5,
        )
        self.wait(0.5)

        # ── Destaque nos valores de pixel ────────────────────
        entries = matrix.get_entries()
        boxes = VGroup(
            SurroundingRectangle(entries[0], color=RED,   stroke_width=2, buff=0.07),
            SurroundingRectangle(entries[3], color=GREEN, stroke_width=2, buff=0.07),
            SurroundingRectangle(entries[6], color=BLUE,  stroke_width=2, buff=0.07),
        )
        intensity_label = Text(
            "Intensidade do pixel  (0 a 255)",
            font_size=22, color=GRAY_C,
        ).next_to(matrix, DOWN, buff=0.5)

        self.play(Create(boxes), FadeIn(intensity_label), run_time=0.8)
        self.wait(0.8)

        # ── Pipeline visual ──────────────────────────────────
        self.play(
            FadeOut(matrix), FadeOut(boxes),
            FadeOut(intensity_label), FadeOut(title),
            run_time=0.8,
        )

        steps  = ["Imagem", "Pixels", "Valores", "Matriz", "Algoritmo"]
        colors = [CYAN_C, BLUE_C, GREEN_C, YELLOW_C, PURPLE_C]

        pipeline_items = []
        for i, (s, c) in enumerate(zip(steps, colors)):
            pipeline_items.append(Text(s, font_size=26, color=c))
            if i < len(steps) - 1:
                pipeline_items.append(
                    Arrow(LEFT * 0.05, RIGHT * 0.05, color=GRAY_C,
                          buff=0, stroke_width=2.5)
                )

        pipeline = VGroup(*pipeline_items).arrange(RIGHT, buff=0.3)

        self.play(
            LaggedStart(*[Write(obj) for obj in pipeline], lag_ratio=0.25),
            run_time=2.0,
        )
        self.wait(1.5)
        self.play(FadeOut(pipeline))


# ==============================================================
# CENA 5 — SIMILARIDADE COSSENO
# Duração: ~2min
# ==============================================================

class CosineSimilarity(Scene):
    def construct(self):
        self.camera.background_color = BG

        # ── Plano + fórmula ──────────────────────────────────
        plane = NumberPlane(
            background_line_style={
                "stroke_color": BLUE_E,
                "stroke_opacity": 0.3,
            },
            axis_config={"stroke_color": GRAY_C, "stroke_opacity": 0.7},
        )
        formula = MathTex(
            r"\cos(\theta) = \frac{\vec{A} \cdot \vec{B}}{\|\vec{A}\|\,\|\vec{B}\|}",
            color=WHITE, font_size=38,
        ).to_edge(UP, buff=0.4)

        self.play(Create(plane), run_time=1.2)
        self.play(Write(formula), run_time=1.0)

        # ── Vetores ──────────────────────────────────────────
        a_end = [4, 1.5, 0]
        b_end = [2, 3.5, 0]

        vec_a = Vector(a_end, color=BLUE_C,  stroke_width=5)
        vec_b = Vector(b_end, color=GREEN_C, stroke_width=5)

        lbl_a = MathTex(r"\vec{A}", color=BLUE_C,  font_size=36)
        lbl_b = MathTex(r"\vec{B}", color=GREEN_C, font_size=36)
        lbl_a.next_to(vec_a.get_end(), RIGHT, buff=0.15)
        lbl_b.next_to(vec_b.get_end(), UR,    buff=0.15)

        self.play(GrowArrow(vec_a), Write(lbl_a))
        self.play(GrowArrow(vec_b), Write(lbl_b))

        # ── Ângulo θ ─────────────────────────────────────────
        line_a = Line(ORIGIN, a_end)
        line_b = Line(ORIGIN, b_end)
        angle  = Angle(line_a, line_b, radius=1.0, color=YELLOW_C)

        # posição da label θ no meio do arco
        mid_dir = (
            np.array(a_end) / np.linalg.norm(a_end) +
            np.array(b_end) / np.linalg.norm(b_end)
        )
        mid_dir = mid_dir / np.linalg.norm(mid_dir) * 1.45
        theta_lbl = MathTex(r"\theta", color=YELLOW_C, font_size=32)
        theta_lbl.move_to(mid_dir)

        self.play(Create(angle), Write(theta_lbl))
        self.wait(0.8)
        self.play(Indicate(formula, color=YELLOW_C, scale_factor=1.04))

        # ── Casos de similaridade ────────────────────────────
        self.play(
            FadeOut(plane), FadeOut(vec_a), FadeOut(vec_b),
            FadeOut(lbl_a), FadeOut(lbl_b),
            FadeOut(angle), FadeOut(theta_lbl),
            run_time=0.8,
        )

        cases = VGroup(
            Text('θ ≈ 0°    →  cos(θ) = 1    →  "textos idênticos"',   font_size=25, color=GREEN_C),
            Text('θ ≈ 90°   →  cos(θ) = 0    →  "sem relação"',        font_size=25, color=YELLOW_C),
            Text('θ ≈ 180°  →  cos(θ) = −1   →  "totalmente opostos"', font_size=25, color=RED),
        ).arrange(DOWN, buff=0.55, aligned_edge=LEFT)

        self.play(
            LaggedStart(*[Write(c) for c in cases], lag_ratio=0.4),
            run_time=1.8,
        )
        self.wait(0.8)

        # ── Aplicações práticas ──────────────────────────────
        self.play(FadeOut(cases), FadeOut(formula), run_time=0.6)

        app_title = Text("Aplicações", font_size=30, color=CYAN_C)
        app_title.to_edge(UP, buff=0.5)

        def app_card(lines, color):
            rect  = RoundedRectangle(
                corner_radius=0.15, width=2.6, height=1.4,
                color=color, fill_color=color, fill_opacity=0.14, stroke_width=1.5,
            )
            text  = VGroup(*[
                Text(l, font_size=19, color=WHITE) for l in lines
            ]).arrange(DOWN, buff=0.15)
            text.move_to(rect)
            return VGroup(rect, text)

        cards = VGroup(
            app_card(["NLP",        "Semântica de texto"], BLUE_C),
            app_card(["Busca",      "Vetorial"],           CYAN_C),
            app_card(["Reco-",      "mendação"],           PURPLE_C),
        ).arrange(RIGHT, buff=0.6)

        self.play(Write(app_title))
        self.play(
            LaggedStart(*[FadeIn(c, scale=0.88) for c in cards], lag_ratio=0.3),
            run_time=1.2,
        )
        self.wait(1.5)
        self.play(FadeOut(cards), FadeOut(app_title))


# ==============================================================
# CENA 6 — TRANSFORMAÇÕES LINEARES
# Duração: ~1min 30s
# ==============================================================

class LinearTransformationExample(LinearTransformationScene):
    def __init__(self, **kwargs):
        LinearTransformationScene.__init__(
            self,
            show_coordinates=True,
            leave_ghost_vectors=True,
            show_basis_vectors=False,
            **kwargs
        )

    def construct(self):
        # ── Título e label: adicionados como foreground para não
        #    participarem da transformação matricial ────────────
        title = Text("Transformações Lineares", font_size=36, color=WHITE)
        title.to_edge(UP).set_z_index(10)

        matrix_label = MathTex(
            r"M = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}",
            font_size=34, color=YELLOW_C,
        ).to_corner(DR, buff=0.45).set_z_index(10)

        # add_foreground_mobjects evita que o Write/Transform
        # cause conflito de submobjects durante apply_matrix
        self.add_foreground_mobjects(title, matrix_label)

        # ── Vetor amarelo + aplicação da transformação ────────
        shear = [[1, 1], [0, 1]]
        vec   = Vector([2, 1], color=YELLOW_C, stroke_width=5)
        self.add_vector(vec)
        self.wait(0.8)

        self.apply_matrix(shear)
        self.wait(1.0)

        # ── Caixa explicativa (adicionada após a transformação) ─
        note_rect = RoundedRectangle(
            corner_radius=0.12, width=4.4, height=1.1,
            color=CYAN_C, fill_color=CYAN_C,
            fill_opacity=0.14, stroke_width=1.5,
        )
        note_text = Text(
            "Cada camada de uma rede neural\naplicauma transformação  M · x",
            font_size=17, color=WHITE,
        )
        note_text.move_to(note_rect)
        note = VGroup(note_rect, note_text).to_corner(DL, buff=0.4).set_z_index(10)

        self.play(FadeIn(note))
        self.wait(1.5)


# ==============================================================
# CENA 7 — REDE NEURAL
# Duração: ~1min 30s
# ==============================================================

class NeuralNetwork(Scene):
    def construct(self):
        self.camera.background_color = BG

        # ── Título ───────────────────────────────────────────
        title = Text(
            "Redes neurais usam operações matriciais",
            font_size=32, color=WHITE,
        ).to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1.0)

        # ── Construção das camadas ────────────────────────────
        layer_specs = [
            (3, BLUE_C,   "Entrada\n(X)",         -3.8),
            (4, PURPLE_C, "Camadas\nocultas",       0.0),
            (2, GREEN_C,  "Saída\n(Y)",             3.8),
        ]

        layers_groups = []
        for count, color, _, x in layer_specs:
            g = VGroup(*[
                Circle(
                    radius=0.28, color=color,
                    stroke_width=2, fill_opacity=0.18, fill_color=color,
                ).move_to([x, (i - (count - 1) / 2) * 1.15, 0])
                for i in range(count)
            ])
            layers_groups.append(g)

        # Conexões
        connections = VGroup()
        for i in range(len(layers_groups) - 1):
            for n1 in layers_groups[i]:
                for n2 in layers_groups[i + 1]:
                    connections.add(
                        Line(
                            n1.get_center(), n2.get_center(),
                            stroke_opacity=0.2, stroke_width=1, color=GRAY_C,
                        )
                    )

        self.play(Create(connections), run_time=1.0)
        for lg in layers_groups:
            self.play(Create(lg), run_time=0.45)

        # Labels das camadas
        layer_labels = VGroup(*[
            Text(lbl_text, font_size=17, color=color).move_to([x, -2.45, 0])
            for _, color, lbl_text, x in layer_specs
        ])
        self.play(FadeIn(layer_labels), run_time=0.5)

        # ── Fórmula Y = WX + b ───────────────────────────────
        formula = MathTex("Y", "=", "W", "X", "+", "b", font_size=52, color=WHITE)
        formula.to_edge(DOWN, buff=0.5)
        self.play(Write(formula), run_time=0.8)

        # Destaque em cada símbolo
        highlights = [
            (0, YELLOW_C, "saída"),
            (2, GREEN_C,  "pesos (matriz)"),
            (3, BLUE_C,   "entrada"),
            (5, PURPLE_C, "viés"),
        ]
        for idx, color, _ in highlights:
            self.play(
                Indicate(formula[idx], color=color, scale_factor=1.5),
                run_time=0.45,
            )

        # Caixa de legenda
        legend = VGroup(*[
            VGroup(
                MathTex(sym, color=color, font_size=22),
                Text(f" → {desc}", font_size=17, color=WHITE),
            ).arrange(RIGHT, buff=0.08)
            for sym, color, desc in [
                ("X", BLUE_C,   "entrada"),
                ("W", GREEN_C,  "pesos (matriz)"),
                ("b", PURPLE_C, "viés"),
                ("Y", YELLOW_C, "saída"),
            ]
        ]).arrange(DOWN, buff=0.2, aligned_edge=LEFT).to_corner(DR, buff=0.5)

        self.play(FadeIn(legend), run_time=0.8)
        self.wait(1.0)

        # ── Fechamento ───────────────────────────────────────
        self.play(
            FadeOut(title), FadeOut(connections),
            *[FadeOut(lg) for lg in layers_groups],
            FadeOut(layer_labels), FadeOut(formula), FadeOut(legend),
            run_time=0.8,
        )
        closing = Text(
            "Treinar uma rede neural = ajustar os valores de W",
            font_size=28, color=CYAN_C,
        )
        self.play(Write(closing), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(closing))


# ==============================================================
# CENA 8 — DECOMPOSIÇÃO SVD
# Duração: ~1min 30s
# ==============================================================

class SVDScene(Scene):
    def construct(self):
        self.camera.background_color = BG

        # ── Título ───────────────────────────────────────────
        title = Text("Decomposição SVD", font_size=38, color=WHITE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=0.8)

        # ── Matriz original A ────────────────────────────────
        lbl_a  = MathTex("A =", color=CYAN_C, font_size=44)
        mat_a  = Matrix([[5, 3], [4, 2]], h_buff=1.0, v_buff=0.8).set_color(WHITE)
        group_a = VGroup(lbl_a, mat_a).arrange(RIGHT, buff=0.3)

        self.play(Write(lbl_a), Create(mat_a), run_time=1.0)
        self.wait(0.8)

        # ── Fórmula SVD ───────────────────────────────────────
        formula_svd = MathTex(r"A = U \Sigma V^T", font_size=44, color=WHITE)
        formula_svd.to_edge(UP, buff=0.5)

        # ── Três matrizes decompostas ────────────────────────
        mat_u = Matrix([[1, 0], [0, 1]], h_buff=0.8, v_buff=0.7).scale(0.62).set_color(WHITE)
        mat_s = Matrix([[7, 0], [0, 2]], h_buff=0.8, v_buff=0.7).scale(0.62).set_color(WHITE)
        mat_v = Matrix([[1, 0], [0, 1]], h_buff=0.8, v_buff=0.7).scale(0.62).set_color(WHITE)

        lbl_u = MathTex("U",       color=BLUE_C,   font_size=28).next_to(mat_u, UP, buff=0.2)
        lbl_s = MathTex(r"\Sigma", color=YELLOW_C, font_size=28).next_to(mat_s, UP, buff=0.2)
        lbl_v = MathTex("V^T",     color=GREEN_C,  font_size=28).next_to(mat_v, UP, buff=0.2)

        t1 = MathTex(r"\times", font_size=28, color=GRAY_C)
        t2 = MathTex(r"\times", font_size=28, color=GRAY_C)

        decomposed = VGroup(
            VGroup(lbl_u, mat_u), t1,
            VGroup(lbl_s, mat_s), t2,
            VGroup(lbl_v, mat_v),
        ).arrange(RIGHT, buff=0.45).move_to(DOWN * 0.5)

        self.play(
            ReplacementTransform(group_a, decomposed),
            ReplacementTransform(title, formula_svd),
            run_time=1.8,
        )
        self.wait(0.8)

        # ── Aplicações práticas ──────────────────────────────
        self.play(FadeOut(decomposed), FadeOut(formula_svd), run_time=0.6)

        apps_title = Text("Aplicações do SVD", font_size=30, color=CYAN_C)
        apps_title.to_edge(UP, buff=0.5)

        bullets = VGroup(
            Text("•  Compressão de imagens",               font_size=26, color=WHITE),
            Text("•  Sistemas de recomendação (Netflix)",   font_size=26, color=WHITE),
            Text("•  Redução dimensional (PCA)",            font_size=26, color=WHITE),
            Text("•  Embeddings compactos em NLP",          font_size=26, color=WHITE),
        ).arrange(DOWN, buff=0.45, aligned_edge=LEFT)

        self.play(Write(apps_title))
        self.play(
            LaggedStart(*[FadeIn(b, shift=RIGHT * 0.3) for b in bullets], lag_ratio=0.3),
            run_time=1.5,
        )
        self.wait(1.0)

        self.play(FadeOut(apps_title), FadeOut(bullets), run_time=0.6)
        closing = Text(
            "SVD = Encontrar a estrutura essencial de qualquer matriz",
            font_size=26, color=CYAN_C,
        )
        self.play(Write(closing), run_time=1.5)
        self.wait(1.5)
        self.play(FadeOut(closing))


# ==============================================================
# CENA 9 — CONCLUSÃO
# Duração: ~2min
# ==============================================================

class Conclusion(Scene):
    def construct(self):
        self.camera.background_color = BG

        # ── Partículas (espelho da abertura) ─────────────────
        np.random.seed(42)
        particles = VGroup(*[
            Dot(
                point=[
                    np.random.uniform(-6.5, 6.5),
                    np.random.uniform(-3.5, 3.5),
                    0,
                ],
                radius=np.random.uniform(0.02, 0.05),
                color=WHITE,
            ).set_opacity(np.random.uniform(0.08, 0.35))
            for _ in range(90)
        ])
        self.play(FadeIn(particles, lag_ratio=0.03), run_time=1.0)

        # ── Frase central colorida ───────────────────────────
        phrase = VGroup(
            Text("Dados",        font_size=42, color=BLUE_C),
            Text("→",            font_size=42, color=GRAY_C),
            Text("Matemática",   font_size=42, color=CYAN_C),
            Text("→",            font_size=42, color=GRAY_C),
            Text("Inteligência", font_size=42, color=PURPLE_C),
        ).arrange(RIGHT, buff=0.35)

        self.play(Write(phrase), run_time=2.0)

        subtitle = Text(
            "A Álgebra Linear é a base do Machine Learning",
            font_size=28, color=GRAY_C,
        ).next_to(phrase, DOWN, buff=0.5)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=0.8)
        self.wait(0.8)

        # ── Mini-ícones de recap ─────────────────────────────
        self.play(FadeOut(phrase), FadeOut(subtitle), run_time=0.6)

        icons_data = [
            ("Vetores",        BLUE_C),
            ("Matrizes",       GREEN_C),
            ("Imagens",        CYAN_C),
            ("Similaridade",   YELLOW_C),
            ("Transf. Lin.",   PURPLE_C),
            ("Redes Neurais",  "#FF6B6B"),
            ("SVD",            "#C77DFF"),
        ]

        def icon_card(name, color):
            rect  = RoundedRectangle(
                corner_radius=0.12, width=2.3, height=0.85,
                color=color, fill_color=color,
                fill_opacity=0.15, stroke_width=1.5,
            )
            label = Text(name, font_size=19, color=WHITE).move_to(rect)
            return VGroup(rect, label)

        icon_groups = [icon_card(n, c) for n, c in icons_data]
        icons = VGroup(*icon_groups)

        row1 = VGroup(*icon_groups[:4]).arrange(RIGHT, buff=0.3)
        row2 = VGroup(*icon_groups[4:]).arrange(RIGHT, buff=0.3)
        row2.next_to(row1, DOWN, buff=0.35)
        row2.set_x(0)
        VGroup(row1, row2).center()

        self.play(
            LaggedStart(*[FadeIn(ic, scale=0.82) for ic in icons], lag_ratio=0.12),
            run_time=1.8,
        )
        self.play(
            LaggedStart(
                *[Flash(ic, color=ic[0].get_color(), line_length=0.14, num_lines=8)
                  for ic in icons],
                lag_ratio=0.1,
            ),
            run_time=1.5,
        )
        self.wait(0.5)
        self.play(FadeOut(icons), run_time=0.6)

        # ── Os quatro pilares ────────────────────────────────
        pillars_title = Text("Em síntese:", font_size=28, color=CYAN_C)
        pillars_title.to_edge(UP, buff=0.5)
        self.play(Write(pillars_title))

        pillars = VGroup(
            VGroup(
                Text("1", font_size=32, color=CYAN_C,   weight=BOLD),
                Text("Dados precisam ser matematicamente representados",      font_size=21, color=WHITE),
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                Text("2", font_size=32, color=GREEN_C,  weight=BOLD),
                Text("Álgebra linear estrutura essa representação",           font_size=21, color=WHITE),
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                Text("3", font_size=32, color=YELLOW_C, weight=BOLD),
                Text("Operações matriciais executam o processamento",         font_size=21, color=WHITE),
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                Text("4", font_size=32, color=PURPLE_C, weight=BOLD),
                Text("Machine Learning depende diretamente dessas estruturas",font_size=21, color=WHITE),
            ).arrange(RIGHT, buff=0.3),
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT)

        self.play(
            LaggedStart(*[FadeIn(p, shift=RIGHT * 0.3) for p in pillars], lag_ratio=0.4),
            run_time=2.0,
        )
        self.wait(1.5)

        # ── Créditos finais ───────────────────────────────────
        self.play(
            FadeOut(pillars), FadeOut(pillars_title),
            FadeOut(particles),
            run_time=0.8,
        )

        credits = VGroup(
            Text("Álgebra Linear aplicada ao Machine Learning",
                 font_size=35, color=CYAN_C, weight=BOLD),
            Text("Disciplina: Matemática Discreta",
                 font_size=22, color=GRAY_C),
            Text("Universidade Federal de Goiás",
                 font_size=22, color=GRAY_C),
            Text("Júlia Santos Coité",
                 font_size=20, color=GRAY_C),
            Text("Giovanna Borges Basso",
                 font_size=20, color=GRAY_C),
            Text("Milena Oliveira Penhalves",
                 font_size=20, color=GRAY_C),
        ).arrange(DOWN, buff=0.45)

        self.play(
            LaggedStart(*[FadeIn(c) for c in credits], lag_ratio=0.4),
            run_time=1.5,
        )
        self.wait(2.5)
        self.play(FadeOut(credits), run_time=1.5)
