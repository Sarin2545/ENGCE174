class Employee: #main class
    def __init__(self, name, salary): 
        self.name = name
        self.salary = salary
    
    def annual_salary(self):
        return self.salary * 12
    
class Manager(Employee): # คลาสย่อยของ main class
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus
        
    def annual_salary(self):
        return (self.salary * 12) + self.bonus
    
class Developer(Employee):# คลาสย่อยของ main class
    def __init__(self, name, salary, projects):
        super().__init__(name, salary) 
        self.projects = projects
        
    def annual_salary(self):
        base_salary = self.salary * 12
        return base_salary + (self.projects * 1000)
    
manager = Manager("Alice", 6000, 5000)# (6000*12)+5000
developer = Developer("Bob", 5000, 3)# (5000*12)+(3*1000)

total_annual_salary = manager.annual_salary() + developer.annual_salary()
print(total_annual_salary)