KARMA_GAP = 100 # difference in karma when npc start attack player

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

    def _interact(self, player):
        '''
        Compare karma, talk if ok, attack if not
        '''
        if abs(self.karma - player.karma) >= KARMA_GAP:
            self._fight(player)
        else:
            self._talk(player)


    def _fight(self, player):
        '''
        Compare damage, health and protectiveness
        If player kills npc, his karma -= int(npc karma * coefficient)
        '''
        print(f'NPC fights you back!')
        player.fight(self)

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
        self.location = location
        self.game_map.npcs[location].append(self)


class Warrior(NPC):
    '''
    Class contains information about warrior npcs (they fight)
    '''
    def __init__(self, name, karma, game_map):
        self.name = name
        super().__init__(karma, game_map)