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

    def _add_room(self, room_id):
        '''
        Add a room to the graph
        '''
        self.rooms[room_id] = Room(room_id)
        self.loot[room_id] = []
        self.entities[room_id] = []

    def _add_lock(self, room_id1, room_id2, locked = 0):
        '''
        Add a lock to the door between rooms
        locked = 0 if door is unlocked (default)
        locked = 1 if door is locked.
        '''
        self.rooms[room_id1].neighbors[room_id2] = locked

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
        for room_id in self.rooms:
            print(f'{room_id}: {self.rooms[room_id].neighbors}')
