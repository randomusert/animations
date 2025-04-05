from manim import *

class ee(Scene):
    def construct(self):
        a = Circle(3)
        self.add(a)
        t1 = Square(3)
        t2 = Triangle()
        t3 = RegularPolygon(6)
        self.wait(4)
        txt = Text("large animation")
        txt.scale(1.5).shift(UP*2)
        self.wait(2)
        self.play(Write(txt))
        self.wait(2)
        self.play(FadeOut(txt))
        self.wait(2)
        for t in [t1,t2,t3]:
            self.play(Transform(a,t))