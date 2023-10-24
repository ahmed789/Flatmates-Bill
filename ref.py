
import numpy as np
from PLI import Image


class Squar:

    def __init__(self, x, y, side, color) -> None:
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def drow (self, canvas):
        canvas.penup()
        canvas.goto(self.x, self.y)
        canvas.pendown()
        canvas.forward(self.side)
        canvas.left(90)
        canvas.forward(self.side)
        canvas.left(90)
        canvas.forward(self.side)
        canvas.left(90)
        canvas.forward(self.side)
        shap = np.zeros((self.side, self.side, 3), dtype=np.uint8)
        shap[:] = self.color


sq = Squar(10, 10, 120, [255, 255, 0])