from Model import LSystemModel
from View import LSystemView
from Controller import Controller


class Client:
    def __init__(self):
        model = LSystemModel()
        controller = Controller(model)
        view = LSystemView(controller)


if __name__ == '__main__':
    Client()
