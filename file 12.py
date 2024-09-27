#classes- blue print used for the creation of objects
class Person():
    species = 'mamals'

#creating an object out of the class
person1 = Person() 

#accessing the attribute species
print(person1.species)
print(getattr(person1, 'species'))
print(person1.__getattribute__('species'))

#modifying the attribute species
person1.species = 'amphibian'
print(person1.species)
setattr(person1, 'species','reptile')
print(person1. species)
person1.__setattr__('species','mamals')
print(person1. species)

class Person():
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
        self.email = f"{self.name.lower().strip().replace(' ','.')}.{self.gender[0].lower()}@mak.ac.ug"

    def greeting(self, tod = 'good morning'):
        return f'hallo {self.name}, {tod}'  # time of day  

    def __str__(self):
        return self.name    
#to return both name age etc, we use    return f'{self.name} {self.age}'

person2 = Person('david hope', 'male', 30)    
print(person2.__dict__) 
print(person2) 

#modify the name of person2 to daniella
setattr(person2, 'name' ,'daniella')
print(person2.__dict__)
print(person2)

print(person2.greeting()) 
print(person2.greeting('good evening'))

#inheritance
class Programmers(Person):
    def __init__(self,name,gender,age,lang, salary):
        super().__init__(name, gender, age)
        self.lang = lang
        self.salary = salary

    def incrementSalary(self, percentage):
        self.salary = percentage * self.salary
        return f'hi {self.name}, new salary is {self.salary}'

programmer1 = Programmers('monica', 'female', 20,'python',200000) 
print(programmer1.__dict__)
print(programmer1.greeting('good afternoon'))
print(programmer1.incrementSalary(1.1))
print(programmer1)       

class Person():
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def modeOfTransport(self):
        return f'{self.name} moves by foot'

    def __str__(self):
        return self.name

class Programmers(Person):
    def __init__(self,name,gender,age,lang, salary):
        super().__init__(name, gender, age)
        self.lang = lang
        self.salary = salary

    def modeOfTransport(self):
        return f'{self.name} moves by car' 

person1 = Person('monica', 20,'female')
person2 = Programmers('mick', 30,'male','java',20000) 

print(person1.modeOfTransport())
print(person2.modeOfTransport())

#incompl





