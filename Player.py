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

        self.talents = []
        self.attribute_term = [1, 1, 0.1, 1, 1]

        # Talents

        self.talents.append(Talent('Fire aura', 0))
        self.talents[0].description = 'Adds fire aura to your weapons, increasing your damage.'

        self.talents.append(Talent('Technic', 0))
        self.talents[1].description = 'You get better at using weapons, dealing more damage.'

        self.talents.append(Talent('Shield', 1))
        self.talents[2].description = 'Adds magic shield that protects you, increasing your health.'

        self.talents.append(Talent('Chaos chance', 2))
        self.talents[3].description = 'Your mastery over the chaos grows, increasing chance to strike critcial damage.'

        self.talents.append(Talent('Chaos slice', 3))
        self.talents[4].description = 'Empowers you to deliver strikes of critical damage.'

        self.talents.append(Talent('Potency', 4))
        self.talents[5].description = 'You master your skills at potion brewing, making it better.'

        print(f'Welcome to the world, {self.name}\n')

    def show_stats(self):
        '''
        Prints stats
        '''
        print(f'Warrior {self.name} of level {self.level}')
        print(f'XP: {self.xp}/{self.xp_to_level_up}')
        print(f'Health: {self.hp}/{self.max_hp}')
        print(f'Attack: {self.damage}')
        print(f'Protectiveness: {self.protectiveness}')
        print(f'Karma: {self.karma}')


    def show_map(self):
        '''
        Show map
        '''
        print(self.game_map._show_map())

    def show_location(self):
        '''
        Show location
        '''
        print(f'Location is {self.location}')

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

    def show_inventory(self):
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

    def show_talents(self):
        '''
        Prints talents
        '''
        print('Your talents:')
        for talent in self.talents:
            print(f'{talent.name}: {talent.attribute} - {talent.description}')

    def move(self, room):
        '''
        Move to the room if neighbor
        '''
        if self.location in self.game_map.rooms[room].neighbors or room in self.game_map.rooms[self.location].neighbors:
            self.location = room
            print(f'Moved to {room}')
        else:
            print(f'{room} is not the next room!')

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
        while player_health > 0 and npc.hp > 0:
            if random.random() <= self.crit_chance:
                crit = self.crit_damage
                print('Critial strike!')

            player_damage = self.damage + crit
            player_health = self.hp + self.protectiveness

            npc.hp -= player_damage
            player_health -= npc.damage

        if player_health <=0:
            print('YOU ARE DEAD.')
        if npc.hp <= 0:
            print(f'You have won {npc.name}')
            npc._die()
            self.add_xp(npc.damage + 1)

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

    def enhance_talent(self, talent_name):
        '''
        Improves a talent
        '''
        if self.talent_points > 0:
            for talent in self.talents:
                if talent.name == talent_name:
                    if talent.type == 2 and talent.attribute == 0:
                        print('You already are a god of chaos!')
                    talent.attribute += self.attribute_term[talent.type]
                    talent.update_attribute()
                    self.talent_points -= 1
                    print(f'You enhanced {talent.name}')
                    return None
            print('There is no such talent!')
        else:
            print('No talent points!')

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
        self.xp_to_level_up *= 2

        print(f'You reached level {self.level}!')


class Talent:
    '''
    type = 0 - adds damage
    type = 1 - adds health
    type = 2 - adds crit chance
    type = 3 - adds crit damage
    type = 4 - adds potions buff
    '''
    attributes = [0, 0, 0, 0, 0]

    def __init__(self, name, talent_type):
        self.name = name
        self.type = talent_type
        self.description = ''

        # attribute adds damage/health/etc depending on the talent type
        self.attribute = 0

    def update_attribute(self):
        '''
        Updates attributes which are used in fights
        '''
        type(self).attributes[self.type] = self.attribute
