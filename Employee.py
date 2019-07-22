#Python Object-Oriented Programming

class Employee:
    
    raise_amt = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname (self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):
    raise_amt = 1.1
    
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang
        
        
class Manager(Employee):
    def __init__(self, first, last, pay, emp_list=None):
        super().__init__(first, last, pay)
        if emp_list == None:
            self.emp_list = []
        else:
            self.emp_list = emp_list
            
    def add_emp(self, emp):
        if emp not in self.emp_list:
            self.emp_list.append(emp)
    
    def remove_emp(self, emp):
        if emp in self.emp_list:
            self.emp_list.remove(emp)
            
    def print_emp(self):
        for x in self.emp_list:
            print ('>>> ', x.fullname())
            
        
dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'User', 60000, 'Java')

mgr_1 = Manager('Sue', 'Shame', 90000, [dev_1])

mgr_1.add_emp(dev_2)
mgr_1.print_emp()

mgr_1.remove_emp(dev_1)
mgr_1.print_emp()

#
#print(dev_1.prog_lang)
#
#dev_1.apply_raise()
#
#print(dev_1.pay)


        