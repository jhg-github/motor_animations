from entities.synchronous_motor import SynchronousMotor


class Scene:
    def __init__(self):
        self.motor_sync = SynchronousMotor(
            stator_field_speed=2.0,
            stator_radius=200,
            rotor_radius=120,
        )

        self.motor_async = SynchronousMotor(
            stator_field_speed=2.0,
            stator_radius=200,
            rotor_radius=120,
        )

    def update(self, dt):
        self.motor_sync.update(dt)
        self.motor_async.update(dt)

    def draw(self):
        cx = 400
        cy = 600
        self.motor_sync.draw(cx, cy)
        cx = 1000
        self.motor_async.draw(cx, cy)
