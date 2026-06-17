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
        self.scene.motor_sync.field_speed.value = self.sync_field_speed_slider.value
        self.sync_field_speed_label.text = f"Field Speed: {self.scene.motor_sync.field_speed.value:.2f} [rad/s]"

        self.scene.motor_async.field_speed.value = self.async_field_speed_slider.value
        self.async_field_speed_label.text = f"Field Speed: {self.scene.motor_async.field_speed.value:.2f} [rad/s]"

        self.scene.motor_async.slip_pct.value = self.async_slip_slider.value
        self.async_slip_label.text = f"Slip: {self.scene.motor_async.slip_pct.value:.2f} [%]"

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

        self.sync_field_speed_label = arcade.gui.UILabel(
            x=205,
            y=270,
            text="Field Speed [rad/s]",
            text_color=arcade.color.WHITE,
        )
        self.ui.add(self.sync_field_speed_label)
        self.sync_field_speed_slider = arcade.gui.UISlider(
            x=197,
            y=245,
            value=self.scene.motor_sync.field_speed.value,
            min_value=0.1,
            max_value=10.0,
            width=300,
        )
        self.ui.add(self.sync_field_speed_slider)

        self.async_field_speed_label = arcade.gui.UILabel(
            x=805,
            y=270,
            text="Field Speed [rad/s]",
            text_color=arcade.color.WHITE,
        )
        self.ui.add(self.async_field_speed_label)
        self.async_field_speed_slider = arcade.gui.UISlider(
            x=797,
            y=245,
            value=self.scene.motor_async.field_speed.value,
            min_value=0.1,
            max_value=10.0,
            width=300,
        )
        self.ui.add(self.async_field_speed_slider)
        self.async_slip_label = arcade.gui.UILabel(
            x=805,
            y=220,
            text="Slip [%]",
            text_color=arcade.color.WHITE,
        )
        self.ui.add(self.async_slip_label)
        self.async_slip_slider = arcade.gui.UISlider(
            x=797,
            y=195,
            value=self.scene.motor_async.slip_pct.value,
            min_value=0,
            max_value=5.0,
            width=300,
        )
        self.ui.add(self.async_slip_slider)
