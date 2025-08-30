#initiate a class
class employee:
    #static variable
    _user_id=0

    #this is constructor-called special function/dunder method/magic method
    def __init__(self):
        #these are the data/attributes of the class
        self.__uid=employee._user_id
        employee._user_id+=1
        self.__rollno=1234
        self.name="nandhu"
        self.id=123
        self.designation="sde"
    #getter
    def get_rollno(self):
        return self.__rollno
    #setter
    def set_rollno(self,value):
        self.__rollno=value

    #static method
    def get_uid():
        return employee._user_id

    #now lets create an function ie method(function in class is a method)
    def travel(self,destination):
        print(f"now the employee is travelling to {destination}")
#creating an object
nandhu=employee()
#print(nandhu.id)
#print(nandhu)
#calling a method
#nandhu.travel("telangana")
#creating an attribute outside the class
nandhu.name="ram"
#print(nandhu.name)