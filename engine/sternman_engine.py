from engine import Engine


class SternmanEngine(Engine):
    def __init__(self, warning_lights):
        self.warning_lights = warning_lights

    def needs_service(self):
        if self.warning_lights:
            return True
        else:
            return False
