import random

KARMA_GAP = 100 # difference in karma when npcs start attack player
MAX_HP = 10

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

        self.max_hp = MAX_HP
        self.hp = self.max_hp
        self.damage = 1
        self.protectiveness = 0
        self.crit_chance = 0
        self.crit_damage = 0
        self.potency = 0

        self.level = 1
        self.xp = 0
        self.xp_to_level_up = 1
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

        print(f'\nWelcome to the world, {self.name}\n')

    def show_stats(self):
        print(f'''\nWarrior {self.name} of level {self.level}
            XP: {self.xp}/{self.xp_to_level_up}
            Health: {self.hp}/{self.max_hp}
            Attack: {self.damage}
            Protectiveness: {self.protectiveness}
            Karma: {self.karma}\n''')


    def show_map(self):
        print(f'\n{self.game_map.get_map()}\n')

    def show_location(self):
        print(f'\nLocation is {self.location}\n')

    def show_loot(self):
        if len(self.game_map.loot[self.location]) == 0:
            print(f'\nNothing interesting in {self.location}\n')
            return None
        else:
            print(f'\nItems in the {self.location}:')
        to_print = []
        for item in self.game_map.loot[self.location]:
            to_print.append(item.name)
        print(f"\n{', '.join(to_print)}\n")

    def show_npcs(self):
        if len(self.game_map.npcs[self.location]) == 0:
            print(f'\nNothing interesting in {self.location}\n')
            return None
        else:
            print(f'\nNPCs in the {self.location}:')
            to_print = []
            for npc in self.game_map.npcs[self.location]:
                to_print.append(npc.name)
            print(f"\n{', '.join(to_print)}\n")

    def show_inventory(self):
        if len(self.loot) == 0:
            print('\nYour backpack is empty\n')
        else:
            print('\nInventory:')
        to_print = []
        for item in self.loot:
            to_print.append(item.name)
        print(f"{', '.join(to_print)}\n")

    def show_talents(self):
        print('\nYour talents:')
        for talent in self.talents:
            print(f"{talent.name}: {talent.attribute} - {talent.description}")
        print(f'You have {self.talent_points} talent points.\n')

    def move(self, room):
        if self.location in self.game_map.rooms[room].neighbors or room in self.game_map.rooms[self.location].neighbors:
            self.location = room
            self.game_map.player_location = room
            print(f'\nMoved to {room}\n')
        else:
            print(f"\n{room} is not the next room or doesn't exist!\n")

    def interact(self, npc):
        if self.location == npc.location:
            if abs(self.karma - npc.karma) >= KARMA_GAP:
                print('\nFIGHT!\n')
                self.fight(npc)
            else:
                npc.talk(self)
        else:
            print('\nShizoid????\n')

    def fight(self, npc):
        self.karma -= npc.karma // 2

        crit = 0

        player_damage = self.damage + crit
        player_health = self.hp + self.protectiveness

        print(f'\nYou attack {npc.name}!\n')
        while player_health > 0 and npc.hp > 0:
            if random.random() <= self.crit_chance:
                crit = self.crit_damage
                print('\nCritial strike!\n')

            player_damage = self.damage + crit
            player_health = self.hp + self.protectiveness

            npc.hp -= player_damage
            player_health -= npc.damage

        if player_health <=0:
            print('\nYOU ARE DEAD.\n')
        if npc.hp <= 0:
            print(f'\nYou killed {npc.name}\n')
            npc.die()
            self.add_xp(npc.damage + 1)

    def drop_item(self, item):
        if item in self.loot:
            self.loot.remove(item)
            print(f'\nYou dropped {item.name}\n')
            self.game_map.loot[self.location].append(item)
        else:
            print(f'\nYou don\'t have {item.name} to drop.\n')

    def take_item(self, item):
        if item in self.game_map.loot[self.location]:
            self.loot.append(item)
            self.game_map.loot[self.location].remove(item)
        else:
            print(f'\nNo such item in {self.location}\n')

    def enhance_talent(self, talent_name):
        '''
        Improves a talent
        '''
        if self.talent_points == 0:
            print('\nNo talent points!\n')
            return None
        for talent in self.talents:
            if talent_name == talent.name:
                talent.attribute += self.attribute_term[talent.type]
                self.update_talent_stats(talent)
                talent.update_attribute()
                self.talent_points -= 1
                print(f'\nYou enhanced {talent.name}\n')
                return None
        print('\nThere is no such talent!\n')

    def update_talent_stats(self, talent):
        if talent.type == 0:
            self.damage += self.attribute_term[0]
        elif talent.type == 1:
            self.max_hp += self.attribute_term[1]
        elif talent.type == 2:
            self.crit_chance += self.attribute_term[2]
        elif talent.type == 3:
            self.crit_damage += self.attribute_term[3]
        elif talent.type == 4:
            self.potency += self.attribute_term[4]


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

        print(f'\nYou reached level {self.level}!\n')


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
