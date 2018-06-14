class Employee(object):

    employee_count = 30  #total count of the employees
    def __init__(self, name, family, salary, department): #defining default constructor and passing the object
        self._n = name
        self._f = family
        self._s = salary
        self._d = department



    def avg_sal(self):  #to calculate average salary of a particular employee
        average_sal = self._s / self.employee_count  #calculating with the default values
        print("Average salary of {} is {}".format(self._n, average_sal))


if __name__ == "__main__":
    e = Employee('jack',{'Brother':'Nathan', 'Sister':'Amy'},10000,'Administrative') #Creating an object for Employee with its values
    e.avg_sal() #calling the local method of the class