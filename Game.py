from Map import Room, Map
from Player import Player

g = Map()

g._add_room('Bedroom')
g._add_room('Hall')
g._add_room('Kitchen')
g._add_room('Bathroom')

g._add_lock('Bedroom', 'Hall', 0)
g._add_lock('Hall', 'Kitchen', 1)
g._add_lock('Hall', 'Bathroom', 1)

g._show_map()

player = Player('Maratik')
g._set_location('Bedroom')
