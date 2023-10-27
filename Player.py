import random

KARMA_GAP = 100 # difference in karma when npcs start attack player

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

        self.max_hp = 3
        self.hp = self.max_hp
        self.damage = 1
        self.protectiveness = 0
        self.crit_chance = 0
        self.crit_damage = 0

        self.level = 1
        self.xp = 0
        self.xp_to_level_up = 3
        self.talent_points = 0

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
            if abs(self.karma - npc.karma) >= KARMA_GAP:
                print('FIGHT!')
                self.fight(npc)
            else:
                npc._talk(self)
        else:
            print('Shizoid????')

    def fight(self, npc):
        '''
        Attack npc
        '''
        self.karma -= npc.karma // 2

        crit = 0

        player_damage = self.damage + crit
        player_health = self.hp + self.protectiveness

        print(f'{self.name} fights {npc.name}!')
        while player_health > 0 and npc.health > 0:
            if random.random() <= self.crit_chance:
                crit = self.crit_damage
                print('Critial strike!')

            player_damage = self.damage + crit
            player_health = self.hp + self.protectiveness

            npc.health -= player_damage
            player_health -= npc.damage

        if player_health <=0:
            print('YOU ARE DEAD.')
        if npc.health <= 0:
            print(f'You have won {npc.name}')
            npc._die()
            self.add_xp(npc.damage + 1)

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

    def add_xp(self, xp):
        '''
        Add experience points
        '''
        self.xp += xp
        while self.xp >= self.xp_to_level_up:
            self.xp -= self.xp_to_level_up
            self.level_up()

    def level_up(self):
        '''
        Level up protocol
        '''
        self.level += 1
        self.max_hp += 1
        self.hp = self.max_hp
        self.damage += 1
        self.protectiveness += 1
        self.talent_points += 1

        print(f'You reached level {self.level}!')



class Talents:
    '''
    Contains talents and their buffs
    '''
    def __init__(self):
        self.fire_aura = 0
        self.fire_aura_name = 'Fire aura'
        self.fire_aura_description = 'Adds a fire aura to the weapons, increasing damage'

        self.shield = 0
        self.shield_name = 'Shield'
        self.shield_description = 'Reduces incoming damage'
        self.absorption = 0
        self.absorption_name = 'Absorption'
        self.absorption_description = 'Creates a chance to not get incoming damage for an enemy'

        self.technic = 0
        self.technic_name = 'Technic'
        self.technic_description = 'Better weapon control, increases damage'
        self.chaos_slice = 0
        self.chaos_slice_name = 'Chaos slice'
        self.chaos_slice_description = 'Increases critical damage'
        self.chaos_chance = 0
        self.chaos_chance_name = 'Chaos chance'
        self.chaos_chance_description = 'Increases chance to strike critical damage'

        self.potency = 0
        self.potency_name = 'Potency'
        self.potency_description = 'Adds a buff to potions'

        self.branches = ['Fire', 'Shield', 'Weapon mastering', 'Potions']

    def show_talent_tree(self, branch = None):
        '''
        Prints talent tree
        '''
        if branch == None:
            print('------'.join(self.branches))
            print('Choose branch in parameters to see talents.')
        elif branch == self.branches[0]:
            print(f'---{self.branches[0]}---')
            print(f'{self.fire_aura_name}: {self.fire_aura} - {self.fire_aura_description}')
        elif branch == self.branches[1]:
            print(f'---{self.branches[1]}---')
            print(f'{self.shield_name}: {self.shield} - {self.shield_description}')
            print(f'{self.absorption_name}: {self.absorption} - {self.absorption_description}')
        elif branch == self.branches[2]:
            print(f'---{self.branches[2]}---')
            print(f'{self.technic_name}: {self.technic} - {self.technic_description}')
            print(f'{self.chaos_slice_name}: {self.chaos_slice} - {self.chaos_slice_description}')
            print(f'{self.chaos_chance_name}: {self.chaos_chance} - {self.chaos_chance_description}')
        elif branch == self.branches[3]:
            print(f'---{self.branches[3]}---')
            print(f'{self.potency_name}: {self.potency} - {self.potency_description}')

    def add_talent(self, talent = None):
        '''
        Improves chosen talent
        '''
        if

if __name__ == '__main__':
    a = Talents()
    a.show_talent_tree()
    a.show_talent_tree(branch='Weapon mastering')