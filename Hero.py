class SuperHero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points,  catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def __str__(self):
        return f'{self.nickname} {self.superpower} {self.health_points}'

    def __len__(self):
        return len(self.catchphrase)
    def get_name(self):
        print(self.name)

    def double_health(self):
        self.health_points *= 2


class Air(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        SuperHero.__init__(self, name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def __str__(self):
        return f'{self.nickname} {self.superpower} {self.health_points} {self.damage} {self.fly}'

    def double_health(self):
        self.health_points **= 2
        self.fly = True

    def phrase(self):
        print('True in the True_phrase')


class Earth(SuperHero):
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly=False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def __str__(self):
        return f'{self.nickname} {self.superpower} {self.health_points} {self.damage} {self.fly}'

    def double_health(self):
        self.health_points **= 2
        self.fly = True

    def phrase(self):
        print('True in the True_phrase')


class Vilian(Earth):
    people = 'monster'

    def gen_x(self):
        pass

    def crit(self):
        self.damage **= 2


Hero = Earth('Grount', 'Grock', 'Shield', 1000, 'GROOOCK!!!', 5)
Hero2 = Air('Sky', 'Skii', 'Fly', 200, 'Pew', 20)
print(Hero)
Hero2.double_health()
print(Hero2)
Hero.phrase()
'''И как жто должно было работать?'''
print(Vilian.crit(Hero2))
