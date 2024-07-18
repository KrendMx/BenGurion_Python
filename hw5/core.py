from random import *
from time import time

class Animals:
    
    def __init__(self, hunter, male, fullness = 100, oldest = 1, id = ''.join(str((time() * 1000)).split('.'))[::-1][0:8]):
        self.fullness = fullness
        self.oldest = oldest
        self.hunter = hunter
        self.male = male == 1
        self.id = id
    
    def increase_age(self):
        self.age += 1
    
    def eat(self, enoth):
        if (self.hunter):
            if (enoth):
                if randint(0,1) == 1:
                    self.fullness = self.fullness * 1.26
                    return True
                else:
                    self.fullness -= self.fullness * 0.09
                    return False
        else:
            self.fullness += 26
            return True
    

class Nature: 
    def __init__(self):
        self.airHunt = []
        self.waterHunt = []
        self.earthHunt = []
        self.airGrace = []
        self.waterGrace = []
        self.earthGrace = []
        self.generate_start_animal()
        self.food = 10*12
    
    def create_animal(self, type, age, fullness, male, hunter):
        
        newId = ''.join(str((time() * 1000)).split('.'))[::-1][0:8]
        
        def hunt(self, hunt, instanceName, instance):
            if hunt:
                getattr(self, f'{instanceName}Hunt').append(instance)
            else:
                getattr(self, f'{instanceName}Grace').append(instance)
        
        match type:
            case 1:
                a = AirAnimals(hunter, male, fullness, age , newId)
                hunt(self, hunter, 'air', a)
            case 2:
                a = EarthAnimals(hunter, male, fullness, age, newId)
                hunt(self, hunter, 'earth', a)
                
            case 3:
                a = WaterAnimals(hunter, male, fullness, age, newId)
                hunt(self, hunter, 'water', a)
                
            case _:
                a = AirAnimals(hunter, male, fullness, age, newId)
                hunt(self, hunter, 'air', a)
        
        return newId
        
    def generate_start_animal(self):
        for i in range(12):
            self.create_animal(randint(1,3), 1, 100, randint(1,2), randint(1,2) == 1)
    
    def get_all_animals(self):
        return [*self.airGrace, *self.airHunt, *self.earthGrace, *self.earthHunt, *self.waterGrace, *self.waterHunt]
    
    def get_current_animal(self, id):
        a = self.get_all_animals()
        return [x for x in a if x.id == id][0]
    
    def increase_food(self, count):
        self.food += count
    
    def model_inproduction(self, id_animal_1, id_animal_2):
        a = [x for x in self.get_all_animals() if x.id == id_animal_1 or x.id ==id_animal_2]
        if (a[0].male == a[1].male):
            return 'Однополые животные не могут иметь детей'
        if (a[0].hunter != a[1].hunter):
            return 'Охотник ест жертву, а не размножается с ней'
        if(a[0].__class__.__name__ != a[1].__class__.__name__):
            return 'Рыба не спит с птицами'
        match a[0].__class__.__name__:
            case 'AirAnimals':
                if a[0].fullness > 42 and a[1].fullness > 42 and a[0].oldest > 3 and a[1].oldest > 3:
                    for _ in range(4):
                        self.create_animal(1, 1, 64, randint(0,1), a[0].hunter)
                    return 'Животные созданы'
                else:
                    return 'Животные еще не готовы размножаться'
            case 'EarthAnimals':
                if a[0].fullness > 20 and a[1].fullness > 20 and a[0].oldest > 5 and a[1].oldest > 5:
                    for _ in range(2):
                        self.create_animal(2, 1, 73, randint(0,1), a[0].hunter)
                    return 'Животные созданы'
                else:
                    return 'Животные еще не готовы размножаться'
            case 'WaterAnimals':
                if a[0].fullness > 50 and a[1].fullness > 50:
                    for _ in range(20):
                        self.create_animal(3, 1, 36, randint(0,1), a[0].hunter)
                    return 'Животные созданы'
                else:
                    return 'Животные еще не готовы размножаться'

    
    def increase_time(self):
        for animal in self.get_all_animals():
            animal.increase_age()
        
        self.eating()
    
    def eating(self):
        self.eating_grace()
        self.eating_hunter()

    def eating_hunter(self):
        for animal in self.airHunt:
            if (animal.eat(len(self.airGrace) >= 1)):
                self.airGrace.pop(0)
        for animal in self.earthHunt:
            if (animal.eat(len(self.earthGrace) >= 1)):
                self.earthGrace.pop(0)
        for animal in self.waterHunt:
            if (animal.eat(len(self.waterGrace) >= 1)):
                self.waterGrace.pop(0)
    
    def eating_grace(self):
        for animal in self.airGrace:
            if(animal.eat(True)):
                self.food -= 1
        for animal in self.waterGrace:
            if(animal.eat(True)):
                self.food -= 1
        for animal in self.earthGrace:
            if(animal.eat(True)):
                self.food -= 1

        


class AirAnimals(Animals):
    pass

class EarthAnimals(Animals):
    pass

class WaterAnimals(Animals):
    pass