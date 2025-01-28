class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def info(self):
        return self.name, self.id


name = 'ashraful'
id = '2345'
student1 = Student(name, id)
st_name, st_id = student1.info()  # Call the method with parentheses
print(st_name, st_id)