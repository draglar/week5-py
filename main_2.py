'''
Activity 2: Polymorphism Challenge! 🎭

Create a program that includes animals or vehicles with the same action (like move()). However, make each class define move() differently (for example, Car.move() prints "Driving" 🚗, while Plane.move() prints "Flying" ✈️).
'''
class Cat:
    def __init__(self) -> None:
        self.movement = 'Walking'
        pass
    def move(self):
        return self.movement

class Fish:
    def __init__(self) -> None:
        self.movement = 'Flying'
        pass
    def move(self):
        return self.movement
class Bird:
    def __init__(self) -> None:
        self.movement = 'Flying'
        pass
    def move(self):
        return self.movement

for animal in[Cat(),Fish(),Bird()]:
    print('movement by ',animal.move())