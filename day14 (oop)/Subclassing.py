
#  Python code to demonstrate how parent constructors
# are called.

# parent class

class Person():

     # __init__ is  constructor
     def __init__(self, name, study, job):
          self.name = name
          self.study = study
          self.job = job

class Employee(Person):
            def __init__(self, name, study, job, salary , post):
                       self.salary = salary
                       self.post = post

                       # Invoking the init of parent class
                       super().__init__(name, study, job)


            def PrintDetail(self):
                       print(f"I am {self.name} and i study {self.study}. Currently i am pursing my journey on {self.job}  and i make a {self.salary} as my monthly salary. I am working as  {self.post} at xxx Company.")

emp = Employee("Samir", "BCA", "QA", 20000, "Intern")

emp.PrintDetail()