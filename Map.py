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
        self.key_id = 1

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
        locked = 1 if door is locked. In this case, unique id will be given to door
        '''
        if locked == 0:
            self.rooms[room_id1].neighbors[room_id2] = locked
            self.rooms[room_id2].neighbors[room_id1] = locked
        else:
            self.rooms[room_id1].neighbors[room_id2] = self.key_id
            self.rooms[room_id2].neighbors[room_id1] = self.key_id
            self.key_id += 1

    def _check(self, room_id1, room_id2):
        '''
        Checks if the door is locked
        '''
        if room_id1 in self.rooms[room_id2].neighbors:
            return self.rooms[room_id1].neighbors[room_id2]
        else:
            return None

    def _show_map(self):
        '''
        Print map
        '''
        for room_id in self.rooms:
            print(f'{room_id}: {self.rooms[room_id].neighbors}')

    def _add_loot(self, room_id, item_id):
        '''
        Add loot to the room
        '''
        self.loot[room_id].append(item_id)

        print(f'Item_{item_id} added to {room_id}.')

    def _show_loot(self, room_id = None):
        '''
        Print loot
        '''
        if room_id is None:
            print(self.loot)
        else:
            print(self.loot[room_id])

    def _add_entity(self, room_id, entity_id, close):
        '''
        Add entity
        '''
        self.entities[room_id].append([entity_id, close])

        print(f'Entity_{entity_id} added to {room_id}.')

    def _show_entity(self, room_id = None):
        '''
        Print entity
        '''
        if room_id is None:
            print(self.entities)
        else:
            print(self.entities[room_id])

    def _set_location(self, room_id):
        '''
        Set location of the player
        '''
        self.location = room_id

        print(f'Location set to {room_id}.')

    def where(self):
        '''
        Print current room
        '''
        print(f'Current location is {self.location}.')

    def doors(self):
        '''
        Print doors in the current room
        '''
        neighbors = map(str, self.rooms[self.location].neighbors.keys())
        print(f'Doors in current room lead to: {", ".join(neighbors)}.')

    def move(self, room_id):
        '''
        Moves to the room_id if door isn't locked
        '''
        if self._check(self.location, room_id) is None:
            print(f'{room_id} is not the next room!')
        elif self._check(self.location, room_id) == 1:
            ### add key_check to the room_id so that the door can be opened with the key.
            print(f'Door to {room_id} is locked!')
        else:
            self._set_location(room_id)
