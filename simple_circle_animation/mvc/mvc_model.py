import math


class CircleModel:
    def __init__(self, radius=150, speed=1.0):
        self.radius = radius
        self.speed = speed
        self.angle = 0.0
        self.last_dt = 0.0

    def update(self, dt):
        self.last_dt = dt
        self.angle += self.speed * dt

    def get_position(self, screen_width, screen_height):
        x = screen_width / 2 + self.radius * math.cos(self.angle)
        y = screen_height / 2 + self.radius * math.sin(self.angle)
        return x, y
