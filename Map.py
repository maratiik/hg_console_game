class Room:
    '''
    Class contains rooms and their neighbors.
    '''

    def __init__(self, room_name):
        self.room_name = room_name
        self.neighbors = {}


class Map:
    '''
    Class contains one graph with rooms.
    '''

    def __init__(self):
        self.rooms = {}

    def add_room(self, room_name):
        '''
        Add a room to the graph.
        '''
        self.rooms[room_name] = Room(room_name)

    def add_lock(self, room_name1, room_name2, locked):
        '''
        Add a lock to the door between rooms.
        locked = 1 if door is locked,
        locked = 0 if door is unlocked
        '''
        self.rooms[room_name1].neighbors[room_name2] = locked
        self.rooms[room_name2].neighbors[room_name1] = locked


if __name__ == '__main__':
    g = Map()

    g.add_room('Bedroom')
    g.add_room('Hall')
    g.add_room('Kitchen')
    g.add_room('Bathroom')

    g.add_lock('Bedroom', 'Hall', 0)
    g.add_lock('Hall', 'Kitchen', 0)
    g.add_lock('Hall', 'Bathroom', 1)

    for room in g.rooms:
        print(f'{room}: {g.rooms[room].neighbors}')
