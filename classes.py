class Person:
    species='Homosapien'

    def hello(self):
        print('hello world')

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def hi(self):
        print('hi my name is ' + self.name)

kevaughn=Person('kevaughn', 17)
anna=Person('anna',17)
print(kevaughn.species)
print(kevaughn.age)
print(anna.age)
kevaughn.hello()
kevaughn.hi()