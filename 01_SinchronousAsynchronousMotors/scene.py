import arcade
from entities.synchronous_motor import SynchronousMotor

class Scene:
    def __init__(self):
        self.motor = SynchronousMotor(stator_field_speed=2.0, rotor_field_speed=2.0, stator_radius=200, rotor_radius=120)

    def update(self, dt):
        self.motor.update(dt)

    def draw(self):
        cx = 400
        cy = 600
        self.motor.draw(cx, cy)
