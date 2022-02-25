class Controller:
    def __init__(self, model):
        self.model = model

    def on_view_init_complete(self, view):
        self.view = view
        self.view.run()

    def get_data(self):
        data = self.model.get_system()
        if data:
            self.view.update_view(data.name, data.depth, data.str, data.angle)
        else:
            exit()
