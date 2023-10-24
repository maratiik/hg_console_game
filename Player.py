from Map import Room, Map

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
        if self.game_map