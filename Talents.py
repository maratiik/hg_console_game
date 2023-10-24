class Talent:
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
