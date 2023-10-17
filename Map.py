class Room:

    '''
    Contains rooms and their neighbors
    '''

    def __init__(self, room_name):
        self.room_name = room_name
        self.neighbors = {}



class Map:

    '''
    Class contains one graph with rooms
    '''

    def __init__(self):
        self.rooms = {}
        self.loot = {}
        self.entities = {}

    def _add_room(self, room_name):
        '''
        Add a room to the graph
        '''
        self.rooms[room_name] = Room(room_name)
        self.loot[room_name] = []
        self.entities[room_name] = []

    def _add_lock(self, room_name1, room_name2, locked):
        '''
        Add a lock to the door between rooms
        locked = 1 if door is locked
        locked = 0 if door is unlocked
        '''
        self.rooms[room_name1].neighbors[room_name2] = locked
        self.rooms[room_name2].neighbors[room_name1] = locked

    def _check(self, room_name1, room_name2):
        '''
        Checks if the door is locked
        '''
        if room_name1 in self.rooms[room_name2].neighbors:
            return self.rooms[room_name1].neighbors[room_name2]
        else:
            return None

    def _show_map(self):
        '''
        Print map
        '''
        for room in self.rooms:
            print(f'{room}: {self.rooms[room].neighbors}')

    def _add_loot(self, room, loot_id):
        '''
        Add loot to the room
        '''

        self.loot[room].append(loot_id)

    def _show_loot(self, room_name = None):
        '''
        Print loot
        '''
        if room_name == None:
            print(self.loot)
        else:
            print(self.loot[room_name])

    def _add_entity(self, room, entity_id, close):
        '''
        Add entity
        '''

        self.entities[room].append([entity_id, close])

    def _show_entity(self, room_name = None):
        '''
        Print entity
        '''

        if room_name == None:
            print(self.entities)
        else:
            print(self.entities[room_name])
