from manim import *

class eeeeeeeeeeeeeeee(Scene):
    def construct(self):
        a = Circle()
        text1 = Text("this is the video animation compilation.", color=GRAY)
        credits = Text("credits go to manin community developers,\n python developers, \n and the kdenlive developers.", color=BLUE)
        txt2 = Text("These  animations are made in manim.", color=RED)
        txt3 = Text("Enjoy.\n I have compiled this video from my manim animations!")
        
        txt2.scale(1)
        txt3.scale(0.8).shift(DOWN*1.5)
        text1.scale(1).shift(UP)
        self.play(Write(text1))
        self.wait(4)
        self.add(a)
        self.wait(2)
        credits.shift(UP*1.9).scale(0.8)
        self.play(Write(txt2))
        self.wait(2)
        self.play(Write(txt3))
        self.wait(2)
        self.play(Write(credits))
        self.wait(1)
