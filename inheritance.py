#
class Animal:
    def __init__(self,name,alive=True,fed=False):
        self.name = name
        self.alive = alive
        self.fed = fed

    def eat (self,food):
        if food.edible == False:
            print(f'{self.name} не стал есть {food.name}')
            self.alive = False
        else:
            print(f'{self.name} съел {food.name}')
            self.fed = True

class Mammal(Animal):
        pass

class Predator(Animal):
        pass

class Plant:
    def __init__(self,name,edible = False):
        self.name = name
        self.edible = edible
        edible = False

class Flower(Plant):
    pass

class Fruit(Plant):
    pass

a1 = Predator('Волк с Уол-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин',True)
print(a1.name)
print(p1.name)
print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
