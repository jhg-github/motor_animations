import arcade

from components.angle import Angle
from components.speed import Speed
from components.radius import Radius

from entities.stator_mechanical import StatorMechanical
from entities.stator_field import StatorField
from entities.rotor_mechanical import RotorMechanical
from entities.rotor_field import RotorField


class SynchronousMotor:
    def __init__(self, stator_speed, rotor_speed, stator_radius, radius):
        self.stator_angle = Angle()
        self.rotor_angle = Angle()
        self.rotor_field_angle = Angle()

        self.stator_mech = StatorMechanical(Angle(0), Speed(0), Radius(stator_radius))
        self.rotor_mech = RotorMechanical(self.rotor_angle, Speed(rotor_speed), Radius(radius), arcade.color.DARK_GRAY)
        self.stator_field = StatorField(self.stator_angle, Speed(stator_speed), Radius(stator_radius), arcade.color.BLUE)
        self.rotor_field = RotorField(self.rotor_field_angle, Speed(stator_speed), Radius(radius), arcade.color.GREEN)

    def update(self, dt):
        self.rotor_mech.update(dt)
        self.stator_field.update(dt)
        self.rotor_field.update(dt)

    def draw(self, cx, cy):
        self.stator_mech.draw(cx, cy)
        self.rotor_mech.draw(cx, cy)
        self.stator_field.draw(cx, cy)
        self.rotor_field.draw(cx, cy)

        text_x = cx - 120
        text_y = cy - self.stator_mech.radius.value - 40
        arcade.draw_text(f"Stator field speed: {self.stator_field.speed.value:.2f} rad/s", text_x, text_y, arcade.color.WHITE, 14,)
        arcade.draw_circle_filled(text_x - 15, text_y + 5, 7, arcade.color.BLUE)
        arcade.draw_text(f"Rotor mech speed: {self.rotor_mech.speed.value:.2f} rad/s", text_x, text_y - 20, arcade.color.WHITE, 14,)
        arcade.draw_lbwh_rectangle_filled(text_x - 20, text_y - 20, 12, 12, arcade.color.DARK_GRAY)
        arcade.draw_text(f"Rotor field speed: {self.rotor_field.speed.value:.2f} rad/s", text_x, text_y - 40, arcade.color.WHITE, 14,)
        arcade.draw_circle_filled(text_x - 15, text_y - 35, 7, arcade.color.GREEN)
