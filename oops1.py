#initiate a class
class employee:
    #this is constructor-called special function/dunder method/magic method
    def __init__(self):
        #these are the data/attributes of the class
        self.name="nandhu"
        self.id=123
        self.designation="sde"

    #now lets create an function ie method(function in class is a method)
    def travel(self,destination):
        print(f"now the employee is travelling to {destination}")
#creating an object
nandhu=employee()
print(nandhu.id)
print(nandhu)
#calling a method
nandhu.travel("telangana")