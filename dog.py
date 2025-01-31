class Dog:
    def __init__(self, name):
        self.name= name
    def bark1(self):
        return f"{self.name} says woof!"
class GoldenRetriever(Dog):
    def __init__(self, name, color):
        self.color = color
        super().__init__(name)
    def bark(self):
        return f"{self.name} says woof! and is {self.color} in color"
myGoldenRetriever = GoldenRetriever("Buddy","Golden")
print(myGoldenRetriever.bark1())
print(myGoldenRetriever.bark())