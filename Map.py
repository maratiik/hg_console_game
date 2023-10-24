class Room:

    '''
    Contains rooms and their neighbors
    '''

    def __init__(self, room_id):
        self.room_id = room_id
        self.neighbors = {}



class Map:

    '''
    Class contains one graph with rooms
    '''

    def __init__(self):
        self.rooms = {}
        self.loot = {}
        self.entities = {}
        self.location = ''

    def _add_room(self, room):
        '''
        Add a room to the graph
        '''
        self.rooms[room] = Room(room)
        self.loot[room] = []
        self.entities[room] = []

    def _add_lock(self, room1, room2, locked = 0):
        '''
        Add a lock to the door between rooms
        locked = 0 if door is unlocked (default)
        locked = 1 if door is locked.
        '''
        self.rooms[room1].neighbors[room2] = locked

        # Add key_ids as graph edges
        #if locked == 0:
        #    self.rooms[room_id1].neighbors[room_id2] = locked
        #    self.rooms[room_id2].neighbors[room_id1] = locked
        #else:
        #    self.rooms[room_id1].neighbors[room_id2] = self.key_id
        #    self.rooms[room_id2].neighbors[room_id1] = self.key_id
        #    self.key_id += 1

    def _show_map(self):
        '''
        Print map
        '''
        for room in self.rooms:
            print(f'{room}: {self.rooms[room].neighbors}')

if __name__ == '__main__':
    game_map = Map()

    game_map._add_room('Bedroom')
    game_map._add_room('Hall')
    game_map._add_room('Kitchen')
    game_map._add_room('Bathroom')

    game_map._add_lock('Bedroom', 'Hall', 0)
    game_map._add_lock('Hall', 'Kitchen', 1)
    game_map._add_lock('Hall', 'Bathroom', 1)

    game_map._show_map()

    player = Player('name', game_map)