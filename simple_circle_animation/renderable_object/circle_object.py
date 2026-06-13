import arcade
import math


class CircleObject:
    def __init__(self, radius=150, speed=1.0, color=arcade.color.RED):
        self.radius = radius
        self.speed = speed
        self.angle = 0.0
        self.color = color

    def update(self, dt):
        self.angle += self.speed * dt

    def draw(self, cx, cy):
        # Compute point
        x = cx + self.radius * math.cos(self.angle)
        y = cy + self.radius * math.sin(self.angle)

        # Draw circle outline
        arcade.draw_circle_outline(cx, cy, self.radius, arcade.color.DARK_GRAY, 2)

        # Draw radius line
        arcade.draw_line(cx, cy, x, y, arcade.color.BLUE, 3)

        # Draw moving point
        arcade.draw_circle_filled(x, y, 8, self.color)
