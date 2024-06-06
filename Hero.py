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


Hero = SuperHero('Sky', 'Skii', 'Fly', 200, 'Oops')
Hero.get_name()
Hero.double_health()
print(Hero)
print(Hero.health_points)
print(len(Hero))
