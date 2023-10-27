class Item:
    id_counter = 0
    def __init__(self, name):
        self.id = type(self).id_counter
        self.name = name

        type(self).id_counter += 1
