class Controller:
    def __init__(self, model):
        self.model = model

    def on_view_init_complete(self, view):
        self.view = view
        ls_names = self.model.get_system_names()
        [self.view.add_menu_entry(n) for n in ls_names]

    def get_system_by_name(self, name):
        ls = self.model.get_system_by_name(name)
        if ls:
            self.view.update_view(ls.name, ls.depth, ls.str, ls.starting_angle, ls.angle)
        else:
            pass
