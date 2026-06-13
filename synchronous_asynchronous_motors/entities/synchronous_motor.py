import arcade

from components.angle import Angle
from components.speed import Speed
from components.radius import Radius

from entities.stator_mechanical import StatorMechanical
from entities.stator_field import StatorField
from entities.rotor_mechanical import RotorMechanical
from entities.rotor_field import RotorField


class SynchronousMotor:
    THICKNESS = 10

    def __init__(
        self, stator_field_speed, rotor_field_speed, stator_radius, rotor_radius
    ):
        self.stator_angle = Angle()
        self.rotor_mech_angle = Angle()
        self.rotor_field_angle = Angle()

        self.stator_field_speed = Speed(stator_field_speed)
        self.rotor_mech_speed = Speed(rotor_field_speed)
        self.rotor_field_speed = Speed(rotor_field_speed)

        self.stator_radius = Radius(stator_radius)
        self.rotor_radius = Radius(rotor_radius)

        self.stator_mech = StatorMechanical(Angle(0), Speed(0), self.stator_radius)
        self.rotor_mech = RotorMechanical(
            self.rotor_mech_angle,
            self.rotor_mech_speed,
            self.rotor_radius,
            arcade.color.DARK_GRAY,
            self.THICKNESS,
        )
        self.stator_field = StatorField(
            self.stator_angle,
            self.stator_field_speed,
            self.stator_radius,
            arcade.color.BLUE,
            self.THICKNESS,
        )
        self.rotor_field = RotorField(
            self.rotor_field_angle,
            self.rotor_field_speed,
            self.rotor_radius,
            arcade.color.GREEN,
            self.THICKNESS,
        )

    def update(self, dt):
        self.rotor_mech.update(dt)
        self.stator_field.update(dt)
        self.rotor_field.update(dt)

    def draw(self, cx, cy):
        self.stator_mech.draw(cx, cy)
        self.rotor_mech.draw(cx, cy)
        self.stator_field.draw(cx, cy)
        self.rotor_field.draw(cx, cy)

        legend_x = cx - self.stator_radius.value + 10
        legend_y = cy - self.stator_radius.value - 40

        arcade.draw_circle_filled(legend_x, legend_y - 2, 7, arcade.color.BLUE)
        arcade.draw_text(
            f"Stator field speed: {self.stator_field_speed.value:.2f} rad/s",
            legend_x + 15,
            legend_y - 7,
            arcade.color.WHITE,
            14,
            font_name="Liberation Mono",
        )

        arcade.draw_lbwh_rectangle_filled(
            legend_x - 5, legend_y - 27, 12, 12, arcade.color.DARK_GRAY
        )
        arcade.draw_text(
            f"Rotor mech speed:   {self.rotor_mech_speed.value:.2f} rad/s",
            legend_x + 15,
            legend_y - 27,
            arcade.color.WHITE,
            14,
            font_name="Liberation Mono",
        )

        arcade.draw_circle_filled(legend_x, legend_y - 40, 7, arcade.color.GREEN)
        arcade.draw_text(
            f"Rotor field speed:  {self.rotor_field_speed.value:.2f} rad/s",
            legend_x + 15,
            legend_y - 47,
            arcade.color.WHITE,
            14,
            font_name="Liberation Mono",
        )
