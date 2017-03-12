class Employee:
    emCount = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.emCount += 1
    def displayCount(self):
        print "Total employee count is %d" % Employee.emCount

    def displayEmployee(self):
        print "name:", self.name,"salary:", self.salary

employee1 = Employee("one", 10000)
employee1.displayCount()
employee1.displayEmployee()

employee2 = Employee("two", 20000)
employee2.displayCount()
employee2.displayEmployee()

print Employee.__name__
print Employee.__dict__
print Employee.__module__
print Employee.__bases__



