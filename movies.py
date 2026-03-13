from manim import *

class Movie1(Scene):
    def construct(self):
        title = Text("What Happens When You Press Power?")
        self.play(Write(title))
        self.wait()

        cpu = Square().set_color(BLUE)
        cpu_label = Text("CPU").next_to(cpu, DOWN)

        self.play(FadeOut(title))
        self.play(Create(cpu), Write(cpu_label))
        self.wait()

        arrow = Arrow(cpu.get_right(), RIGHT*3)
        bios = Text("BIOS")

        bios.next_to(arrow, RIGHT)

        self.play(Create(arrow), Write(bios))
        self.wait()