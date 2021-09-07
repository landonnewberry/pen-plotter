from config import Config
from controls.head import Head
from controls.pen import Pen
import time


class PenPlotter:

    config: Config
    head: Head
    pen: Pen

    def __init__(self) -> None:
        self.config = Config()
        self.head = Head()
        self.pen = Pen()

    def run(self) -> None:
        self.head.move(x=0, y=200)
        self.head.move(x=0, y=-300)
        self.head.move(x=0, y=100)
        self.head.move(x=0, y=-300)
        self.head.move(x=0, y=300)
