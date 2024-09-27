#class deno :
#    def __init__(self, name , age):
#        self.name = name
#        self.age = age
#    def greet(self):
#        print("hello, my name is",self.name)

#deno1 = deno("wawos",18)

#print(deno)
class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age
#accessing object's attributes 
my_object = MyClass("Alice",30)
print("name:", my_object.name)
print("age:", my_object.age)
