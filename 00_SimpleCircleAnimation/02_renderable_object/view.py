import arcade
from circle_object import CircleObject
from circle_controller import CircleController

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 1200

class CircleView(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Circle Animation")

        arcade.set_background_color(arcade.color.BLACK)

        self.circle = CircleObject()
        self.controller = CircleController(self.circle)

    def on_update(self, dt):
        self.controller.update()
        self.circle.update(dt)

    def on_draw(self):
        self.clear()

        cx = SCREEN_WIDTH / 2
        cy = SCREEN_HEIGHT / 2

        self.circle.draw(cx, cy)
        self.controller.draw()
