import random


class Car:
    def __init__(self, model):
        self.model = model
        self.speed = random.randint(1, 5)

    def get_model(self):
        return self.model
