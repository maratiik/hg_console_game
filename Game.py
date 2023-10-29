from Map import Room, Map
from Player import Player
from NPC import NPC, Warrior
from Item import Item

# Initialise map, player, couple of npcs in different rooms, their loot

game_map = Map()

game_map.add_room('Bedroom')
game_map.add_room('Hall')
game_map.add_room('Kitchen')
game_map.add_room('Bathroom')

game_map.add_lock('Bedroom', 'Hall', 0)
game_map.add_lock('Hall', 'Kitchen', 1)
game_map.add_lock('Hall', 'Bathroom', 1)


Gold = Item('Gold')
Healing_potion = Item('Healing potion')
Sword = Item('Sword')
Vest = Item('Vest')

player = Player('Marat', game_map)
player.location = 'Bedroom'

Ogre1 = Warrior('Ogre', -100, game_map)
Ogre1.set_location('Bedroom')
Ogre1.loot.append(Gold)
Ogre1.health = 2
Ogre1.damage = 1

Ogre2 = Warrior('Ogre', -100, game_map)
Ogre2.set_location('Hall')
Ogre2.loot.append(Gold)
Ogre2.health = 2
Ogre2.damage = 1

Knight = Warrior('Knight', 100, game_map)
Knight.set_location('Kitchen')
Knight.loot.append(Gold)
Knight.health = 10
Knight.damage = 3

Citizen = NPC('Citizen', 20, game_map)
Citizen.set_location('Kitchen')
Citizen.health = 1
Citizen.damage = 1

player.interact(Ogre1)

player.show_location()

player.show_npcs()

player.show_loot()

player.move('Hall')

player.show_npcs()

player.fight(Ogre2)

player.move('Kitchen')

player.show_npcs()

player.interact(Knight)

player.interact(Citizen)

player.show_stats()

player.show_talents()

player.enhance_talent('Fire aura')
player.enhance_talent('Technic')
player.show_stats()
player.show_talents()