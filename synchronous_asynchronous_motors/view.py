import arcade
from scene import Scene


class MotorView(arcade.Window):
    def __init__(self):
        super().__init__(1400, 1200, "Motor Animation")
        arcade.resources.load_liberation_fonts()
        arcade.set_background_color(arcade.color.BLACK)
        self.scene = Scene()
        self.dt_list = []

    def on_update(self, dt):
        self.scene.update(dt)
        self.dt_list.append(dt)
        if len(self.dt_list) == 60:
            avg = sum(self.dt_list) / 60.0
            print(f"Rate={avg:.3f}ms. FPS={1 / avg:.0f}")
            self.dt_list = []

    def on_draw(self):
        self.clear()
        self.scene.draw()
