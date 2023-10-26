import random

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

        self.health = 3
        self.damage = 1
        self.protectiveness = 0
        self.crit_chance = 0
        self.crit_damage = 0

        print(f'Welcome to the world, {self.name}\n')

    def show_map(self):
        '''
        Show map
        '''
        print(self.game_map._show_map())

    def move(self, room):
        '''
        Move to the room if neighbor
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
            npc._interact(self)
        else:
            print('Shizoid????')

    def fight(self, npc):
        '''
        Attack npc
        '''
        crit = 0

        player_damage = self.damage + crit
        player_health = self.health + self.protectiveness

        print(f'{self.name} fights {npc.name}!')
        while player_health > 0 and npc.health > 0:
            if random.random() <= self.crit_chance:
                crit = self.crit_damage
                print('Critial strike!')

            player_damage = self.damage + crit
            player_health = self.health + self.protectiveness

            npc.health -= player_damage
            player_health -= npc.damage

        if player_health <=0:
            print('YOU ARE DEAD.')
        if npc.health <= 0:
            print(f'You have won {npc.name}')
            npc._die()




    def show_loot(self):
        '''
        Show loot in the room
        '''
        if len(self.game_map.loot[self.location]) == 0:
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

    def take_item(self, item):
        '''
        Take an item from room
        '''
        if item in self.game_map.loot[self.location]:
            self.loot.append(item)
            self.game_map.loot[self.location].remove(item)
        else:
            print(f'No such item in {self.location}\n')