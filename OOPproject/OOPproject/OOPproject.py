# I am creating a project using OOP concept to store the datas of employee
# Employee has ID, Name , Domain , Salary
# Functions that are used are : Salary, Employee_assigning_department, Print_employee_details
# Create a class Employee and create the objects

class Employee:   #class is created
    def __init__(self, id,name,salary,deparment):  #Constructor with argument passed
        self.id = id
        self.name = name
        self.salary = salary
        self.department = deparment
        

    def Salary(self,salary):
        self.Salary = salary
        
        

    def Assign_Department(self,department):
        self.department=department
        

    def Employee_Details(self):
        print("\nID: ", self.id)
        print("Name: ", self.name)
        print("Salary: ", self.salary)
        print("Department: ", self.department)
        print("-------------------------------------------")
        

Employee1 = Employee("E1234", "RAMESH", 20000, "FINANCE")
Employee2 = Employee("E5678", "SURESH", 30000, "INSURANCE")
Employee3 = Employee("E3423", "MANI", 40000, "SALES")
Employee4 = Employee("E6079", "DINESH", 50000, "MACHINE LEARNING")
Employee5 = Employee("E9536", "VIJAY", 60000, "ANALYTICS")


print("Employee Details : ")

Employee1.Employee_Details()
Employee2.Employee_Details()
Employee3.Employee_Details()
Employee4.Employee_Details()
Employee5.Employee_Details()

#Suppose if we want to change the department for Employee 1 and Employee 4

Employee1.Assign_Department("ARTIFICIAL INTELLIGENCE")
Employee4.Assign_Department("POWERBI")



print("AFTER UPDATING THE DEPARTMENT")
Employee1.Employee_Details()
Employee2.Employee_Details()
Employee3.Employee_Details() 
Employee4.Employee_Details()
Employee5.Employee_Details() 


        

        

