class NPC:
    def __init__(self, id, name, karma):
        self.id = id
        self.name = name
        self.karma = karma
        self.loot = []
        self.location = ''

    def _interact(self):
        '''
        Dialog or something
        '''
        print('Hello fellow stranger!')

    def _attack(self):
        '''
        Compare damage, health and protectiveness
        If player kills npc, his karma -= int(npc karma * coefficient)
        '''
        print(f'You attacked {self.name}')
        # Player now has 99999999 of everything and insta kills
        # print(f'You killed {self.name}')
        self._die()

    def _die(self):
        '''
        Dying protocol
        '''
        print(f'{self.name}: Arrrrghh... You killed me...')