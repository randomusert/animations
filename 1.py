from manim import *

class Random(Scene):
    def construct(self):
        a = Circle()
        t1 = Square()
        t2 = Triangle()
        t3 = RegularPolygon(6)
        
        text = Text("random  text in manim")
        self.play(Write(text))
        self.add(a)
        self.wait()
        for t in [t1,t2,t3]:
            self.play(Transform(a,t))