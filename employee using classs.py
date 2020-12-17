class Employee:
    count = 0
    def __init__(self, name, des, salary):
        self.name = name
        self.des = des
        self.salary = salary
        Employee.count = Employee.count + 1
    
    def displayCount(self):
        print("The number of Employess in the organization are: ", self.count)
        
    def displayEmp(self):
        print ("Name of Employee is: ", self.name)
        print ("Designation of Employee: ", self.des)
        print ("Salary of Employee: ", self.salary)
        
e1 = Employee ("Kiran", "Project Manager", 28000)
e2 = Employee ("Sai", "Team Leader", 35000)
e3 = Employee ("Udaya", "Programmer", 15000)
e4 = Employee ("Sai", "Assistant", 3000)

e4.displayCount()

print("Employee Details are:")

e1.displayEmp()
e2.displayEmp()
e3.displayEmp()
e4.displayEmp()
