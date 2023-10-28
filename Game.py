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


player = Player('Maratik', game_map)
player.location = 'Hall'

Ogre_flesh = Item('Ogre Flesh')
Bone = Item('Bone')

Ogre = Warrior('Ogre', -100, game_map)
Ogre.loot = [Ogre_flesh, Bone]
Ogre._set_location('Hall')

player.take_item(Bone)
player.inventory()
player.show_loot()

player.interact(Ogre)

player.show_loot()
player.take_item(Bone)

player.show_talents()

player.add_xp(10)
print(player.xp)

player.enhance_talent('Fire aura')
player.enhance_talent('Fire aura')
player.enhance_talent('Fire aura')
player.enhance_talent('Fire aura')
player.enhance_talent('Fire aura')

player.show_talents()
player.show_stats()
