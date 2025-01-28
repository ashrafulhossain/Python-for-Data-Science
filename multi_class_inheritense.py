class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def display_info(self):
        print("The name of employee:", self.name)
        print("The id of Employee:", self.emp_id)


class Manager(Employee):
    def display_department(self, dept_name):
        print("The name of department:", dept_name)


class Developer(Manager):
    def display_expert(self, lang_name):
        print("The expert language:", lang_name)


# Create objects
manager = Manager('Salman', 101)
dev = Developer('Ashraful', 102)

# Call methods
manager.display_info()
manager.display_department('Engineering')

dev.display_info()
dev.display_department('Engineering')
dev.display_expert('Python')