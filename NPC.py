class NPC:
    '''
    Class contains basic information about NPCs
    '''
    def __init__(self, name, karma, game_map):
        self.name = name
        self.karma = karma
        self.loot = []
        self.location = ''
        self.game_map = game_map

        self.hp = 0 # health of NPC
        self.damage = 0 # damage of NPC

    def die(self):
        '''
        Die protocol.
        Drops loot, gives player experience.
        '''
        print(f'\n{self.name} > Arghhhh...\n')
        self.game_map.loot[self.location].extend(self.loot)
        self.loot = None
        self.game_map.npcs[self.location].remove(self)
        self.location = None

    def talk(self, player):
        '''
        Interaction
        '''
        print(f'\n{self.name} > Hello {player.name}\n')

    def set_location(self, location):
        '''
        Sets location
        '''
        self.location = location
        self.game_map.npcs[location].append(self)


class Warrior(NPC):
    '''
    Class contains information about warrior npcs (they fight)
    '''
    def __init__(self, name, karma, game_map):
        # self.name = name
        super().__init__(name, karma, game_map)

    def talk(self, player):
        '''
        Conversation with player
        '''
        print(f'\n{self.name} > We have nothing to talk about, {player.name}.\n')