import arcade
from scene import Scene

class MotorView(arcade.Window):
    def __init__(self):
        super().__init__(1200, 1200, "Motor Animation")
        arcade.set_background_color(arcade.color.BLACK)
        self.scene = Scene()

    def on_update(self, dt):
        self.scene.update(dt)
        print(dt)

    def on_draw(self):
        self.clear()
        self.scene.draw()
