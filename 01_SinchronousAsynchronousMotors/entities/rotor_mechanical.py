import arcade
import math

class RotorMechanical:
    def __init__(self, angle, speed, radius, color, thickness):
        self.angle = angle
        self.speed = speed
        self.radius = radius
        self.color = color
        self.thickness = thickness

    def update(self, dt):
        self.angle.value += self.speed.value * dt

    def draw(self, cx, cy):
        arcade.draw_circle_filled(cx, cy, self.radius.value, self.color)
        x = cx + (self.radius.value + self.thickness) * math.cos(self.angle.value)
        y = cy + (self.radius.value + self.thickness) * math.sin(self.angle.value)
        arcade.draw_line(cx, cy, x, y, self.color, self.thickness * 2)