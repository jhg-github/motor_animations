import arcade
import arcade.gui
from scene import Scene


class MotorView(arcade.Window):
    def __init__(self):
        super().__init__(1400, 1200, "Motor Animation")
        arcade.resources.load_liberation_fonts()
        arcade.set_background_color(arcade.color.BLACK)
        self.scene = Scene()
        self.dt_list = []
        self._load_gui()

    def on_update(self, dt):
        # Push slider value into the motor component
        self.scene.motor_sync.stator_field_speed.value = self.stator_field_speed_slider.value
        self.stator_field_speed_label.text = f"Stator Field Speed: {self.scene.motor_sync.stator_field_speed.value:.2f} [rad/s]"
        self.scene.update(dt)
        self.dt_list.append(dt)
        if len(self.dt_list) == 60:
            avg = sum(self.dt_list) / 60.0
            print(f"Rate={avg:.3f}ms. FPS={1 / avg:.0f}")
            self.dt_list = []

    def on_draw(self):
        self.clear()
        self.scene.draw()
        self.ui.draw()

    def _load_gui(self):
        # --- GUI ---
        self.ui = arcade.gui.UIManager()
        self.ui.enable()

        self.stator_field_speed_label = arcade.gui.UILabel(
            x=205,
            y=270,
            text="Stator Field Speed [rad/s]",
            text_color=arcade.color.WHITE,
        )
        self.ui.add(self.stator_field_speed_label)

        self.stator_field_speed_slider = arcade.gui.UISlider(
            x=197,
            y=245,
            value=self.scene.motor_sync.stator_field_speed.value,
            min_value=0.1,
            max_value=10.0,
            width=300,
        )
        self.ui.add(self.stator_field_speed_slider)
