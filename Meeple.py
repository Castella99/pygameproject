from Prototypegame import *
import os


class Meeple(Prototype):
    path = os.path.dirname(os.path.abspath(__file__))

    def __init__(self):
        super().__init__()
