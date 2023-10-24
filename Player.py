class Player():
    '''
    Class contains Player's actions and information about their location.
    '''

    def __init__(self, player_name, game_map):

        self.name = player_name
        self.loot = []
        self.location = ''
        self.karma = 0
        self.game_map = game_map

        print(f'Welcome to the world, {self.name}')

    def move(self, room):
        '''
        Moves to the room if neighbor
        '''
        if self.location in self.game_map.rooms[room].neighbors or room in self.game_map.rooms[self.location].neighbors:
            self.location = room
            print(f'Moved to {room}')
        else:
            print(f'{room} is not the next room!')

    def show_location(self):
        '''
        Show location
        '''
        print(f'Location is {self.location}')

    def interact(self, npc):
        '''
        Interact with npc
        '''
        if self.location == npc.location:
            npc._interact()
        else:
            print('Shizoid????')

    def show_loot(self):
        '''
        Show loot in the room
        '''
        if len(self.game_map.loot) == 0:
            print(f'Nothing interesting in {self.location}')
        else:
            print(f'Items in the {self.location}:')
        to_print = []
        for item in self.game_map.loot[self.location]:
            to_print.append(item.name)
        print(', '.join(to_print))

    def inventory(self):
        '''
        Show inventory
        '''
        if len(self.loot) == 0:
            print('Your backpack is empty')
        else:
            print('Inventory:')
        to_print = []
        for item in self.loot:
            to_print.append(item.name)
        print(', '.join(to_print))

    def drop_item(self, item):
        '''
        Drop an item
        '''
        if item in self.loot:
            self.loot.remove(item)
            print(f'You dropped {item.name}')
            self.game_map.loot[self.location].append(item)
        else:
            print(f'You don\'t have {item.name} to drop')