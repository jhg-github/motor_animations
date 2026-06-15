import arcade
import arcade.gui
import math

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 1200
SCREEN_TITLE = "Circle Animation with Sliders"


class CircleAnimation(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)

        # GUI manager
        self.gui_manager = arcade.gui.UIManager()
        self.gui_manager.enable()

        # Layout box for sliders
        v_box = arcade.gui.UIBoxLayout()

        # Radius slider
        self.radius = 150
        self.radius_slider = arcade.gui.UISlider(value=self.radius, min_value=20, max_value=500, width=300)
        v_box.add(arcade.gui.UILabel(text="Radius", text_color=arcade.color.WHITE))
        v_box.add(self.radius_slider, padding=(0, 0, 20, 0))

        # Speed slider
        self.speed = 1.0
        self.speed_slider = arcade.gui.UISlider(value=self.speed, min_value=0.1, max_value=5.0, width=300)
        v_box.add(arcade.gui.UILabel(text="Angular Speed", text_color=arcade.color.WHITE))
        v_box.add(self.speed_slider, padding=(0, 0, 20, 0))

        # Anchor the sliders to the bottom-left
        self.gui_manager.add(arcade.gui.UIAnchorLayout(x=0, y=0, children=[v_box]))

        # Animation state
        self.angle = 0.0
        self.last_delta_time = 0.0

    def on_update(self, delta_time):
        # Update parameters from sliders
        self.radius = self.radius_slider.value
        self.speed = self.speed_slider.value

        # Record delta_time for display
        self.last_delta_time = delta_time

        # Update angle
        self.angle += self.speed * delta_time

    def on_draw(self):
        self.clear()

        # Compute point position
        x = SCREEN_WIDTH / 2 + self.radius * math.cos(self.angle)
        y = SCREEN_HEIGHT / 2 + self.radius * math.sin(self.angle)

        # Draw circle outline
        arcade.draw_circle_outline(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, self.radius, arcade.color.DARK_GRAY, 2)

        # Draw line from center to point
        arcade.draw_line(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, x, y, arcade.color.BLUE, 3)

        # Draw moving point
        arcade.draw_circle_filled(x, y, 8, arcade.color.RED)

        # Draw GUI
        self.gui_manager.draw()

        # Draw delta_time readout
        arcade.draw_text(
            f"dt: {self.last_delta_time:.4f} s",
            10,
            SCREEN_HEIGHT - 20,
            arcade.color.WHITE,
            14,
        )


if __name__ == "__main__":
    CircleAnimation()
    arcade.run()
