import arcade
import math

class StatorMechanical:
    def __init__(self, angle, speed, radius, color=arcade.color.GRAY, thickness=40):
        self.angle = angle
        self.speed = speed
        self.radius = radius
        self.color = color
        self.thicknes = thickness

    def draw(self, cx, cy):
        arcade.draw_circle_outline(cx, cy, self.radius.value, self.color, self.thicknes)
        arcade.draw_line(cx - self.radius.value, cy - self.radius.value, cx + self.radius.value, cy - self.radius.value, self.color, self.thicknes)
