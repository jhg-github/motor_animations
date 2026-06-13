import arcade
import math


class StatorField:
    def __init__(self, angle, speed, radius, color, thickness):
        self.angle = angle
        self.speed = speed
        self.radius = radius
        self.color = color
        self.thickness = thickness

    def update(self, dt):
        self.angle.value += self.speed.value * dt

    def draw(self, cx, cy):
        x = cx + (self.radius.value - 2 * self.thickness) * math.cos(self.angle.value)
        y = cy + (self.radius.value - 2 * self.thickness) * math.sin(self.angle.value)
        arcade.draw_circle_filled(x, y, self.thickness, self.color)
