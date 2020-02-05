class Person:
    person_count = 0
    
    def __init__(self, name, gender, dob):
        self.name = name
        self.gender = gender
        self.dob = dob

    def __eq__(self, other):
        """Override the default Equals behavior"""
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Override the default Unequal behavior"""
        return self.__dict__ != other.__dict__          
        
class Company_A(Person):
    def __init__(self, name, gender, dob, job_title):
        super().__init__(name, gender, dob)
        self.job_title = job_title
        self.organization = 'Company_A Pvt Ltd'
        Company_A.person_count += 1

class Company_B(Person): 
    def __init__(self, name, gender, dob, job_title):
        super().__init__(name, gender, dob)
        self.job_title = job_title
        self.organization = 'Company_B Pvt Ltd'
        Company_B.person_count += 1

# Creating instances of Google and Microsoft classes   
emp1 = Company_B('abc', 'male', '10-12-1993', 'Developer')
emp2 = Company_A('abc', 'male', '10-12-1993', 'Developer')
emp3 = Company_B('abc', 'male', '10-12-1993', 'Developer')

# Counting number of employees
print('Total no. of Company_A Employees: ', Company_A.person_count)
print('Total no. of Company_B Employees: ', Company_B.person_count)

# Tracking employees details
print(emp3.__dict__)

# Comparing two instances or instance attributes
print('Same') if emp1 == emp3 else print('Different')
