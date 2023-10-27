from Map import Room, Map
from Player import Player
from NPC import NPC, Warrior
from Item import Item

game_map = Map()

game_map._add_room('Bedroom')
game_map._add_room('Hall')
game_map._add_room('Kitchen')
game_map._add_room('Bathroom')

game_map._add_lock('Bedroom', 'Hall', 0)
game_map._add_lock('Hall', 'Kitchen', 1)
game_map._add_lock('Hall', 'Bathroom', 1)

### Map initialisation ###

# game_map = Map()
# game_map._add_room('name')
# game_map._add_lock('name1', 'name2', 0/1)

### Player initialisation ###
# player = Player('name', game_map)
# player.location = 'location'
# player.loot.append(item)

### NPC initialisation ###
# NPC_name = Warrior('name', karma, game_map)
# NPC_name.loot = [] or NPC_name.loot.append(items)
# NPC_name.set_location('location')
# NPC_name.health = 0
# NPC_name.damage = 0



player = Player('Maratik', game_map)
player.location = 'Hall'

Ogre_flesh = Item('Ogre Flesh')
Bone = Item('Bone')

Ogre = Warrior('Ogre', -100, game_map)
Ogre.loot = [Ogre_flesh, Bone]
Ogre._set_location('Hall')

Ogre1 = Warrior('Ogre', -100, game_map)
Ogre1.loot = [Ogre_flesh, Bone]
Ogre1._set_location('Hall')

Ogre2 = Warrior('Ogre', -100, game_map)
Ogre2.loot = [Ogre_flesh, Bone]
Ogre2._set_location('Hall')

player.take_item(Bone)
player.inventory()
player.show_loot()

player.interact(Ogre)
player.interact(Ogre1)
player.interact(Ogre2)

player.show_loot()
player.take_item(Bone)
print(player.xp)

game_map._show_map()