from NPC import NPC

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
        self.npcs = {}
        self.player_location = ''

    def add_room(self, room):
        '''
        Add a room to the graph
        '''
        self.rooms[room] = Room(room)
        self.loot[room] = []
        self.npcs[room] = []

    def add_lock(self, room1, room2, locked = 0):
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

    def get_map(self):
        to_print = []
        for room in self.rooms:
           to_print.append(f'{room}: {self.rooms[room].neighbors}')

        return '\n'.join(to_print)
