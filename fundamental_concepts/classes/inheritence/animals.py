# This script shows off classes with inheritance in Python3
# By: Nick from CoffeeBeforeArch

# 
class Animal():
    def __init__(self, age=0, name=""):
        self.age = age
        self.name = name
    def get_age(self):
        return self.age
    def get_name(self):
        return self.name
    def set_age(self, new_age=0):
        self.age = new_age
    def set_name(self, new_name=""):
        self.new_name

# Cat inherits from Animal
class Cat(Animal):
    def speak(self):
        print("Meow!")
    def __str__(self):
        return "Cat:"+str(self.name)+":"+str(self.age)

class Person(Animal):
    # Call base class init method
    def __init__(self, age, name):
        Animal.__init__(self, age, name)
        # Local data attribute
        self.friends = []
    # Override speak method
    def speak(self):
        print("Hello!")
    # New add_friend method
    def add_friend(self, new_friend):
        self.friends.append(new_friend)
    # New age_diff method
    def age_diff(self, other):
        diff = self.age - other.age
        print(abs(diff), "year difference")
    # Override __str__ method
    def __str__(self):
        return "Person:"+str(self.name)+":"+str(self.age)+":"+str(len(self.friends))

class Student(Person):
    # Call base class init method
    def __init__(self, name, age, major=None):
        Person.__init__(self, age, name)
        # Add new data attribute
        self.major = major
    # New change_major method
    def change_major(self, new_major):
        self.major = new_major
    # Override the speak method (again)
    def speak(self):
        print("Hey there, fella!")
    # Override __str__ method (again)
    def __str__(self):
        return "student:"+str(self.name)+":"+str(self.age)+":"+str(len(self.friends))+":"+str(self.major)

# Make a class using each of our four classes
basic_animal = Animal("Teddy", 3)
cat = Cat("Sprinkles", 7)
person = Person("John von Neumann", 30)
student = Student("Nick", 24, "Computer Engineering")

# Any class can use the set_age method from the base class
basic_animal.set_age(1)
cat.set_age(1)
person.set_age(1)
student.set_age(1)

# Only the Person and Student classes can add friends
person.add_friend("Richard")
student.add_friend("Linus")

# Only the student has a major
student.change_major("Computer Science")

# Print using class specific __str__
print(basic_animal)
print(cat)
print(person)
print(student)
