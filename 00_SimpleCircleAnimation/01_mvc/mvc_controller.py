import arcade.gui

class CircleController:
    def __init__(self, model):
        self.model = model
        self.gui_manager = arcade.gui.UIManager()
        self.gui_manager.enable()

        # Root layout
        self.anchor = arcade.gui.UIAnchorLayout()

        # Vertical layout
        self.v_box = arcade.gui.UIBoxLayout()

        # Radius slider
        self.radius_slider = arcade.gui.UISlider(
            value=self.model.radius,
            min_value=20,
            max_value=500,
            width=300
        )
        self.v_box.add(arcade.gui.UILabel(text="Radius", text_color=arcade.color.WHITE))
        self.v_box.add(self.radius_slider, padding=(0, 0, 20, 0))

        # Speed slider
        self.speed_slider = arcade.gui.UISlider(
            value=self.model.speed,
            min_value=0.1,
            max_value=5.0,
            width=300
        )
        self.v_box.add(arcade.gui.UILabel(text="Angular Speed", text_color=arcade.color.WHITE))
        self.v_box.add(self.speed_slider, padding=(0, 0, 20, 0))

        # Add to anchor layout
        self.anchor.add(
            child=self.v_box,
            anchor_x="left",
            anchor_y="bottom"
        )

        self.gui_manager.add(self.anchor)

    def update_model_from_gui(self):
        self.model.radius = self.radius_slider.value
        self.model.speed = self.speed_slider.value

    def draw(self):
        self.gui_manager.draw()
