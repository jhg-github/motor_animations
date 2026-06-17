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

    def __init__(self, stator_field_speed, stator_radius, rotor_radius):
        self.stator_angle = Angle()
        self.rotor_mech_angle = Angle()
        self.rotor_field_angle = Angle()

        self.stator_field_speed = Speed(stator_field_speed)
        self.rotor_mech_speed = Speed(stator_field_speed)
        self.rotor_field_speed = Speed(stator_field_speed)

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

        self.label_stator_field_speed = arcade.Text(
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
        self.label_rotor_field_speed = arcade.Text(
            text="",
            x=0,
            y=0,
            color=arcade.color.WHITE,
            font_size=14,
            font_name="Liberation Mono",
        )

    def update(self, dt):
        # Lock rotor mechanical speed to stator field speed
        self.rotor_mech_speed.value = self.stator_field_speed.value
        self.rotor_field_speed.value = self.stator_field_speed.value

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
        self.label_stator_field_speed.text = f"Stator field speed: {self.stator_field_speed.value:.2f} rad/s"
        self.label_stator_field_speed.x = legend_x + 15
        self.label_stator_field_speed.y = legend_y - 7
        self.label_stator_field_speed.draw()

        arcade.draw_lbwh_rectangle_filled(legend_x - 5, legend_y - 27, 12, 12, arcade.color.DARK_GRAY)
        self.label_rotor_mech_speed.text = f"Rotor mech speed:   {self.rotor_mech_speed.value:.2f} rad/s"
        self.label_rotor_mech_speed.x = legend_x + 15
        self.label_rotor_mech_speed.y = legend_y - 27
        self.label_rotor_mech_speed.draw()

        arcade.draw_circle_filled(legend_x, legend_y - 40, 7, arcade.color.GREEN)
        self.label_rotor_field_speed.text = f"Rotor field speed:  {self.rotor_field_speed.value:.2f} rad/s"
        self.label_rotor_field_speed.x = legend_x + 15
        self.label_rotor_field_speed.y = legend_y - 47
        self.label_rotor_field_speed.draw()
