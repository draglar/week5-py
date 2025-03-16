'''
Assignment 1: Design Your Own Class! 🏗️
Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
Add attributes and methods to bring the class to life!
Use constructors to initialize each object with unique values.
Add an inheritance layer to explore polymorphism or encapsulation.
'''

class Hero:
    def __init__ (self,name,country,infractions,registered):
        self.name = name
        self.country = country
        self.infractions = infractions
        self.registered = registered
        self.sidekick = False
    def risk_level(self):
        if self.registered == False:
            status = f'{self.name} Designated \n Terrorist threat level {round((self.infractions + (1 if self.sidekick else 10)) * 22 /7)}'
        else:
            status = f"{self.name} Designated: Patriot"

        return status

class Sidekick(Hero):
    def __init__(self, name, country, infractions, registered):
        super().__init__(name, country, infractions, registered)
        self.sidekick = True
    pass

sidekick = Sidekick('robin','US',7,False)
hero = Hero('batman','US',1,False)

print(sidekick.risk_level())
print(hero.risk_level())