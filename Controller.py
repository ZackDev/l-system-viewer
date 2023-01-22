class Controller:
    def __init__(self, model):
        self.model = model

    def on_view_init_complete(self, view):
        self.view = view
        menuitems = self.model.get_system_names()
        for m in menuitems:
            self.view.add_menu_entry(m)

    def get_system_by_name(self, name):
        data = self.model.get_system_by_name(name)
        if data:
            self.view.update_view(data.name, data.depth, data.str, data.starting_angle, data.angle)
        else:
            pass
