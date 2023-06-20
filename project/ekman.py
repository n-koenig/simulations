from manim import *

class Geostrophic(MovingCameraScene):
    # Geostrohic velocities without ekman layer
    def construct(self):
        x_range = [1, 10, 0.5]
        y_range = [1, 7, 0.5]
        down_scale = 4
        left_scale = 7
        
        func = lambda pos: 3/pos[0] * RIGHT
        func2 = lambda pos: pos[1]/3 * UP
        
        sl = StreamLines(func, x_range=x_range, y_range=y_range, stroke_width=1.5)
        self.add(sl)
        sl.start_animation()
        
        sl2 = StreamLines(func2, x_range=x_range, y_range=y_range, stroke_width=1.5)
        self.add(sl2)
        sl2.start_animation()
        
        vf = ArrowVectorField(func, x_range=x_range, y_range=y_range, opacity=0.75)
        self.add(vf)
        vf2 = ArrowVectorField(func2, x_range=x_range, y_range=y_range, opacity=0.75)
        self.add(vf2)
        
        self.camera.frame.move_to([left_scale, down_scale, 0])
        self.wait(3)

class Combined(MovingCameraScene):
    # Combined velocities without ekman layer
    def construct(self):
        x_range = [1, 10, 0.5]
        y_range = [1, 7, 0.5]
        down_scale = 4
        left_scale = 7
        
        func = lambda pos: 3/pos[0] * RIGHT + pos[1]/3 * UP
        
        sl = StreamLines(func, x_range=x_range, y_range=y_range, stroke_width=1.5)
        self.add(sl)
        sl.start_animation()
        
        vf = ArrowVectorField(func, x_range=x_range, y_range=y_range, opacity=0.75)
        self.add(vf)
        
        self.camera.frame.move_to([left_scale, down_scale, 0])
        self.wait(3)

class Ekman(MovingCameraScene):
    # (Combined) velocitiers with ekman layer
    def construct(self):
        x_range = [1, 10, 0.5]
        y_range = [1, 6, 0.5]
        y_range2 = [7, 7, 0.5]
        down_scale = 4
        left_scale = 7
        
        # func = lambda pos: 3/pos[0] * RIGHT
        func = lambda pos: 3/pos[0] * RIGHT + pos[1]/3 * UP if pos[1] <= 7 else 3/pos[0] * RIGHT + 1/pos[1] * UP
        func2 = lambda pos: pos[0]/3 * RIGHT
        
        sl = StreamLines(func, x_range=x_range, y_range=y_range, stroke_width=1.5)
        self.add(sl)
        sl.start_animation()
        
        sl2 = StreamLines(func2, x_range=x_range, y_range=y_range2, stroke_width=1.5)
        self.add(sl2)
        sl2.start_animation()
        
        vf = ArrowVectorField(func, x_range=x_range, y_range=y_range, opacity=0.75)
        self.add(vf)
        
        vf2 = ArrowVectorField(func2, x_range=x_range, y_range=y_range2, opacity=0.75)
        self.add(vf2)

        self.camera.frame.move_to([left_scale, down_scale, 0])
        self.wait(3)