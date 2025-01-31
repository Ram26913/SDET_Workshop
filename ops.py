
class emp:
    name ="Ram"
    exp= 9
    role = "Test Lead"

    def printEmp(self):
        print("Name: ", self.name)
        print("Experience: ", self.exp)
        print("Role: ", self.role)
emp1 = emp()
emp1.printEmp()

#Constructor
class emp2:
    def __init__(self, name1, exp1, role1):
        self.name1 = name1
        self.exp1 = exp1
        self.role1 = role1
    
    def printEmp1(self):
        print("Name: ", self.name1)
        print("Experience: ", self.exp1)
        print("Role: ", self.role1)

emp3 = emp2("Rithika", 5, "Test Lead")

emp3.printEmp1()
