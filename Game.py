from Map import Room, Map
from Player import Player
from NPC import NPC
from Item import Item
g = Map()

g._add_room('Bedroom')
g._add_room('Hall')
g._add_room('Kitchen')
g._add_room('Bathroom')

g._add_lock('Bedroom', 'Hall', 0)
g._add_lock('Hall', 'Kitchen', 1)
g._add_lock('Hall', 'Bathroom', 1)

g._show_map()

player = Player('Maratik', g)
player.location = 'Hall'

Ogre = NPC(1, 'Ogre', -100)
g.npcs['Hall'].append(Ogre)

Ogre.location = 'Hall'

Ogre_flesh = Item(1, 'Ogre Flesh')
Bone = Item(2, 'Bone')
player.loot.append(Ogre_flesh)
player.loot.append(Bone)

player.inventory()

player.drop_item(Bone)
player.show_loot()