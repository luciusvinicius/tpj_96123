import random

from Resource import Resource


class Food(Resource):
    def __init__(self, scale, screen, width=80, height=60):
        super().__init__(scale, screen, width, height)
        self.color = "red"


