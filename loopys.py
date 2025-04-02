from manim import *

class loop1(Scene):
    def construct(self):
        for i in range(9):
            a = Circle()
            t1 = Square()
            t2 = Triangle()
            t3 = RegularPolygon()
            t4 = Circle()
            self.wait(1)
            for t in [t1,t2,t3,t4]:
                self.play(Transform(a,t))
                
                self.play(FadeOut(t))
