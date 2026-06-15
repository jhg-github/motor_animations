import arcade.gui


class CircleController:
    def __init__(self, circle):
        self.circle = circle
        self.gui = arcade.gui.UIManager()
        self.gui.enable()

        self.anchor = arcade.gui.UIAnchorLayout()
        self.v_box = arcade.gui.UIBoxLayout()

        # Radius slider
        self.radius_slider = arcade.gui.UISlider(value=self.circle.radius, min_value=20, max_value=500, width=300)
        self.v_box.add(arcade.gui.UILabel(text="Radius", text_color=arcade.color.WHITE))
        self.v_box.add(self.radius_slider, padding=(0, 0, 20, 0))

        # Speed slider
        self.speed_slider = arcade.gui.UISlider(value=self.circle.speed, min_value=0.1, max_value=5.0, width=300)
        self.v_box.add(arcade.gui.UILabel(text="Angular Speed", text_color=arcade.color.WHITE))
        self.v_box.add(self.speed_slider, padding=(0, 0, 20, 0))

        self.anchor.add(self.v_box, anchor_x="left", anchor_y="bottom")
        self.gui.add(self.anchor)

    def update(self):
        self.circle.radius = self.radius_slider.value
        self.circle.speed = self.speed_slider.value

    def draw(self):
        self.gui.draw()
