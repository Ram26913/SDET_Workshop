class Car:
    def __init__(self,brand,year):
        self.brand= brand
        self.year= year
    def printCar(self):
        print("Brand: ", self.brand)
        print("Year: ", str(self.year))

#Single Inheritance
class Buggati(Car):
    def __init__(self,model,type,name):
        self.model= model
        self.type= type
        self.name= name
    def printBuggati(self):
        print("Model: ", self.model)
        print("Type: ", self.type)
        print("Name: ", self.name)

class Audi:
    def __init__(self,color):
        self.color= color
        
    def printAudi(self):
        print("Color: ",self.color)

#M5 -->Bugatti -->Audi
class M5(Buggati,Audi):
    def __init__(self,engine,model):
        #self.color= color
        self.engine= engine
        self.model= model

    def printM5(self):
        #print("Color: ",self.color)
        print("Engine: ", self.engine)
        print("Model: ", self.model)
    def printAudi(self):
        self.color ="White"
        return super().printAudi()
m5 = M5("V10","Veyron")
m5.printM5()
m5.printAudi()