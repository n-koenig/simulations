from manim import *

class CreateCircle(Scene):
    def construct(self):
        circle=Circle()
        circle.set_fill(PINK, opacity=0.5)
        self.play(Create(circle))

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)

        square = Square()
        square.rotate(PI / 4)

        self.play(Create(square))
        self.wait()
        self.play(Transform(square, circle))
        self.wait()
        self.play(FadeOut(square))

class SquareAndCircle(Scene):
    def construct(self):
        circle=Circle()
        circle.set_fill(PINK, opacity=0.5)

        square=Square()
        square.set_fill(BLUE, opacity=0.5)

        square.next_to(circle, RIGHT, buff=0.5)
        self.play(Create(circle), Create(square))

class AnimatedSquareToCircle(Scene):
    def construct(self):
        circle=Circle()
        square=Square()

        self.play(Create(square))
        self.play(square.animate.rotate(PI/4))
        self.play(ReplacementTransform(square, circle))
        self.play(circle.animate.set_fill(PINK, opacity=0.5))

class DifferentRotations(Scene):
    def construct(self):
        left_square=Square(color=BLUE, fill_opacity=0.7).shift(2*LEFT)
        right_square=Square(color=GREEN, fill_opacity=0.7).shift(2*RIGHT)
        
        self.play(left_square.animate.rotate(PI), Rotate(right_square, angle=PI), run_time=2)
        self.wait()

class ContinuousMotion(Scene):
    def construct(self):
        func = lambda pos: np.sin(pos[0] / 2) * UR + np.cos(pos[1] / 2) * LEFT
        stream_lines = StreamLines(func, stroke_width=2, max_anchors_per_line=30)
        self.add(stream_lines)
        stream_lines.start_animation(warm_up=False, flow_speed=1.5)
        self.wait(stream_lines.virtual_time / stream_lines.flow_speed)