class Player():
    '''
    Class contains Player's actions and information about their location.
    '''

    def __init__(self, player_name):

        self.__name = player_name
        print("Welcome to the world, " + self.__name)

        # Level gives talent points to the player when it's up
        self.__level = 1

        # The player can use talent points to enhance talents or open new ones
        self.__talent_points = 0

        # Strength gives damage
        self.__strength = 1

        # Health gives hp
        self.__health_max = 3
        self.__health = 3

        # Experience gives level
        self.__experience = 0

        # Experience needed to reach next level
        self.__experience_needed = 5

        # If crit is rolled (a number rolled between 0 and crit_chance), crit damage is given additionally to usuall attack
        self.__crit_chance = 0.1
        self.__crit_damage = 1

        # Protectiveness  is substracted from incoming damage
        self.__protectiveness = 0

        # Karma defines whether you're a bad guy or a good guy
        # karma < -25 => people will treat you as a 'bad guys helper' because you only help guys who want to break some rules
        # karma < -100 => you are expelled from the school and good guys are your enemies and they attack you
        # karma > 25 => people will treat you as a 'good guys helper' because you only help guys who are in trouble
        # karma > 100 => you are the hero of the school
        self.__karma = 0

        # Inventory
        self.loot = []

    def stats(self):
        '''
        Shows stats to the player.
        '''
        print(f'{self.__name} stats:')
        print(f'Level: {self.__level}')
        print(f'Unused talent points: {self.__talent_points}')
        print(f'Strength: {self.__strength}')
        print(f'Health: {self.__health}/{self.__health_max}')
        print(f'Experience: {self.__experience}/{self.__experience_needed}')
        print(f'Critical strike chance: {self.__crit_chance * 100}%')
        print(f'Critical damage: {self.__crit_damage}')
        print(f'Protectiveness: {self.__protectiveness}')
        print(f'Karma: {self.__karma}')

    def _get_experience(self, xp):
        '''
        Adds obtained experience to existed. Levels up when reaches new level.
        '''
        self.__experience += xp
        print(f'You gained {xp} experience.')
        while self.__experience >= self.__experience_needed:
            self.__experience -= self.__experience_needed
            self.__experience_needed *= 2
            self._level_up()

    def _level_up(self):
        '''
        Level up protocol.
        '''
        self.__level += 1
        self.__talent_points += 1
        self.__strength += 1
        self.__health_max += 1
        self.__health = self.__health_max
        self.__protectiveness += 1
        print(f'You reached level {self.__level}!')
        print(f'You can use {self.__talent_points} talent points to make yourself stronger than ever!')
        print('Your strength, health and protectiveness enhanced.')

    def _add_item(self, *item_ids):
        '''
        Add item to inventory
        '''
        self.loot.extend(item_ids)

    def show_inventory(self):
        '''
        Print inventory
        '''
        print(self.loot)

    def _remove_item(self, item_id):
        '''
        Delete an item from inventory
        '''
        self.loot.remove(item_id)


if __name__ == '__main__':

    player = Player('Marik')
    player._get_experience(5)
    player.stats()
    player._add_item(0, 1, 2)
    player.show_inventory()
    player._remove_item(1)
    player.show_inventory()