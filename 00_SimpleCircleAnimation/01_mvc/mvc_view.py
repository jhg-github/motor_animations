import arcade
from mvc_model import CircleModel
from mvc_controller import CircleController

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 1200
SCREEN_TITLE = "Circle Animation (MVC)"

class CircleView(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.BLACK)

        # Create model + controller
        self.model = CircleModel()
        self.controller = CircleController(self.model)

    def on_update(self, dt):
        # Controller updates model parameters
        self.controller.update_model_from_gui()

        # Model updates animation state
        self.model.update(dt)

    def on_draw(self):
        self.clear()

        # Compute point position
        x, y = self.model.get_position(SCREEN_WIDTH, SCREEN_HEIGHT)

        # Draw circle
        arcade.draw_circle_outline(
            SCREEN_WIDTH / 2,
            SCREEN_HEIGHT / 2,
            self.model.radius,
            arcade.color.DARK_GRAY,
            2
        )

        # Draw line
        arcade.draw_line(
            SCREEN_WIDTH / 2,
            SCREEN_HEIGHT / 2,
            x,
            y,
            arcade.color.BLUE,
            3
        )

        # Draw point
        arcade.draw_circle_filled(x, y, 8, arcade.color.RED)

        # Draw GUI
        self.controller.draw()

        # Draw dt
        arcade.draw_text(
            f"dt: {self.model.last_dt:.4f} s",
            10,
            SCREEN_HEIGHT - 20,
            arcade.color.WHITE,
            14
        )
