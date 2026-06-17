import arcade

from components.angle import Angle
from components.speed import Speed
from components.radius import Radius
from components.slip import Slip

from entities.stator_mechanical import StatorMechanical
from entities.field import Field
from entities.rotor_mechanical import RotorMechanical


class AsynchronousMotor:
    THICKNESS = 10

    def __init__(self, field_speed, slip_pct, stator_radius, rotor_radius):
        self.slip_pct = Slip(slip_pct)

        self.field_angle = Angle(0)
        self.rotor_mech_angle = Angle(0)

        self.field_speed = Speed(field_speed)
        self.rotor_mech_speed = Speed(field_speed)

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
        self.field = Field(
            self.field_angle,
            self.field_speed,
            self.stator_radius,
            arcade.color.BLUE,
            self.THICKNESS,
        )

        self.label_field_speed = arcade.Text(
            text="",
            x=0,
            y=0,
            color=arcade.color.WHITE,
            font_size=14,
            font_name="Liberation Mono",
        )
        self.label_rotor_mech_speed = arcade.Text(
            text="",
            x=0,
            y=0,
            color=arcade.color.WHITE,
            font_size=14,
            font_name="Liberation Mono",
        )

    def update(self, dt):
        self._update_rotor_speed()

        self.rotor_mech.update(dt)
        self.field.update(dt)

    def draw(self, cx, cy):
        self.stator_mech.draw(cx, cy)
        self.rotor_mech.draw(cx, cy)
        self.field.draw(cx, cy)

        legend_x = cx - self.stator_radius.value + 10
        legend_y = cy - self.stator_radius.value - 40

        arcade.draw_circle_filled(legend_x, legend_y - 2, 7, arcade.color.BLUE)
        self.label_field_speed.text = f"Field speed:      {self.field_speed.value:.2f} rad/s"
        self.label_field_speed.x = legend_x + 15
        self.label_field_speed.y = legend_y - 7
        self.label_field_speed.draw()

        arcade.draw_lbwh_rectangle_filled(legend_x - 5, legend_y - 27, 12, 12, arcade.color.DARK_GRAY)
        self.label_rotor_mech_speed.text = f"Rotor mech speed: {self.rotor_mech_speed.value:.2f} rad/s"
        self.label_rotor_mech_speed.x = legend_x + 15
        self.label_rotor_mech_speed.y = legend_y - 27
        self.label_rotor_mech_speed.draw()

    def _update_rotor_speed(self):
        self.rotor_mech_speed.value = self.field_speed.value - (self.slip_pct.value * self.field_speed.value / 100)
