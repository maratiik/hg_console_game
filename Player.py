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

    def get_experience(self, xp):
        '''
        Adds obtained experience to existed. Levels up when reaches new level.
        '''
        self.__experience += xp
        print(f'You gained {xp} experience.')
        while self.__experience >= self.__experience_needed:
            self.__experience -= self.__experience_needed
            self.__experience_needed *= 2
            self.__level_up()

    def __level_up(self):
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

    # Talents attributes:
    # Fire
    # Fire aura gives +damage (passive)
    __fire_aura = 0
    #Fire rain gives damage to all enemies in the room (active)
    __fire_rain_damage = 0

    # Shield
    # Magic shield gives -damage (passive)
    __magic_shield = 0
    # Absorption gives +chance to absorb all damage from one enemy (passive)
    __absorption = 0

    # Weapon mastering
    # Technic gives +damage (passive)
    __technic = 0
    # Chaos slice gives +damage to crit damage (passive)
    __chaos_slice = 0
    # Chaos chance gives +chance to crit chance
    __chaos_chance = 0

    # Potions
    # Toleracy gives +1 buff to every potion's buff (passive)
    __toleracy = 0

    def talent_tree(self, branch = None):
        '''
        Prints talent tree.
        '''
        if branch == None:
            print('Fire--------Shield--------Weapon mastering--------Potions')
            print('Choose branch in parameters of talent tree.')
        elif branch == 'Fire':
            print(f'Fire aura: {self.__fire_aura} - Adds a fire aura to the weapons, increasing damage (passive);')
            print(f'Fire rain: {self.__fire_rain_damage} - Summons fire rain that deals damage to all enemies in the room (active).')
        elif branch == 'Shield':
            print(f'Magic shield: {self.__magic_shield} - Reduces incoming damage (passive);')
            print(f'Absorption: {self.__absorption} - Creates a chance to not get incoming damage from an enemy (passive).')
        elif branch == 'Weapon mastering':
            print(f'Technic: {self.__technic} - Better weapon control, increasing damage (passive);')
            print(f'Chaos slice: {self.__chaos_slice} - Increases critical damage (passive);')
            print(f'Chaos chance: {self.__chaos_chance} - Increases chance to strike critical damage (passive).')
        elif branch == 'Potions':
            print(f'Toleracy: {self.__toleracy} - Adds a buff to potions.')
        else:
            print('Please choose the correct branch.')

    def get_talent(self, talent = None):
        '''
        Improves choosen talent.
        '''
        if self.__talent_points == 0:
            print("You don't have talent points.")
            return
        if talent == None:
            print('Please choose a talent to improve:')
            print('Fire aura, Fire rain, Magic Shield, Absorption, Technic, Chaos slice, Chaos chance, Toleracy.')
        if talent == 'Fire aura':
            self.__fire_aura += 1
            self.__strength += 1
            self.__talent_points -= 1
            print('Your strength is increased by 1.')
        if talent == 'Fire rain':
            ######## add fire rain to actions
            self.__fire_rain_damage += 1
            self.__talent_points -= 1
            print("Fire rain damage is increased by 1.")
        if talent == 'Magic shield':
            self.__magic_shield += 1
            self.__protectiveness += 1
            self.__talent_points -= 1
            print("Your protectiveness is increased by 1.")
        if talent == 'Absorption':
            if self.__absorption == 1:
                print('You are already invincible!')
            else:
                self.__absorption += 0.1
                self.__talent_points -= 1
                print("The chance to absorb damage is increased by 10%.")
        if talent == 'Technic':
            self.__strength += 1
            self.__talent_points -= 1
            print('Your strength is increased by 1.')
        if talent == 'Chaos slice':
            self.__chaos_slice += 1
            self.__crit_damage += 1
            self.__talent_points -= 1
            print('Critical damage is increased by 1.')
        if talent == 'Chaos chance':
            if self.__chaos_chance == 1:
                print('You already hit critical damage every time!')
            else:
                self.__chaos_chance += 0.1
                self.__crit_chance += 0.1
                self.__talent_points -= 1
                print('Your chance to hit critical damage is increased by 10%!')



if __name__ == '__main__':

    player = Player('Marik')
    player.get_experience(5)
    player.get_talent('Fire aura')
    player.stats()
    player.get_experience(5)