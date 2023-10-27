class NPC:
    '''
    Class contains basic information about NPCs
    '''
    def __init__(self, karma, game_map):
        self.karma = karma
        self.loot = []
        self.location = ''
        self.game_map = game_map

        self.health = 0 # health of NPC
        self.damage = 0 # damage of NPC
        print('NPC has arrived!\n')

    def _die(self):
        '''
        Die protocol.
        Drops loot, gives player experience.
        '''
        print('Arghhhh...')
        self.game_map.loot[self.location].extend(self.loot)
        self.loot = None
        self.game_map.npcs[self.location].remove(self)
        self.location = None

    def _talk(self, player):
        '''
        Interaction
        '''
        print('Hello, fellow stranger!')

    def _set_location(self, location):
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
        self.name = name
        super().__init__(karma, game_map)

    def _talk(self, player):
        '''
        Conversation with player
        '''
        print('We have nothing to talk about, bruh.')