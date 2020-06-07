import pygame
from source import setup,tool
class mainManu:
    def __init__(self):
        self.setup_background()
        self.setup_player()
        self.setup_cursor()

    def setup_background(self):
        pass
    def setup_player(self):
        pass
    def setup_cursor(self):
        pass
    def update(self,surface):
        import random
        surface.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))

