from Employee import Employee
class FullTimeEmployee(Employee):
    def __init__(self, name, family, salary, department):  #defining the default constructor for the child class
        Employee.__init__(self, name, family, salary, department) #Referencing the base class constructor
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department

    def raise_sal(self, raise_percent):
        raise_val = self.salary + (self.salary * raise_percent)/100
        print("salary of {} after raise is {}".format(self.name, raise_val))
        print("The dependents of {} are: ".format(self.name))
        print("The dependents are: ")
        for k,v in self.family.items():
            print("{} - {}" .format(k,v))



if __name__ == "__main__":
    e = Employee('Jack','family',10000,'Accounts') #creating an object for the base class
    e.avg_sal() #calling the base class method to calculate average salary
    f = FullTimeEmployee('Jill', {'wife': 'Jerry', 'child': 'Jade'}, 2000, 'HR') #creating an object method for child class itself
    f.raise_sal(10) #calling the method of child class itself
