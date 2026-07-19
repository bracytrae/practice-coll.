class Person:

    person_count = 0

    def __init__(self, name, age, city):

        self.name = name
        self.age = age
        self.city = city

        Person.person_count += 1

    # Greets The Person
    def greet(self):
        return f"Hello, I'm {self.name}, and I am {self.age} years old and lives in {self.city}."

    # Lets it be known whether the person has a birthday
    def have_birthday(self):
        self.age += 1
        return f"{self.name} is now {self.age} years old, and lives in {self.city}."

    # Prints out the contents of the user when using the print function
    def __str__(self):
        return  f"Person(name={self.name}, age={self.age}, city={self.city})"

class Student(Person):

    def __init__(self, name, age, city, major, gpa):
        super().__init__(name, age, city)

        self.major = major
        self.gpa = gpa

    # Lets it be known the students major.
    def study(self):
        return f"{self.name} is studying {self.major}!"

    # Lets it be known the updated gpa.
    def update_gpa(self, new_gpa):
        self.gpa = new_gpa
        return f"{self.name}'s GPA is now {self.gpa}."

    # Returns the contents of the student objects created.
    def __str__(self):
        return f"Student(name={self.name}, age={self.age}, city={self.city}, major={self.major}, gpa={self.gpa})"


def main():

    p1 = Person("Bob", 19, "Mounds View")
    p2 = Person("Alex", 22, "Minneapolis")
    p3 = Person("Jordan", 30, "St. Paul")

    print(p1.greet())
    print(p2.greet())
    print(p3.greet())

    print(p1.have_birthday())
    print(p2.have_birthday())
    print(p3.have_birthday())

    print(p1)
    print(p2)
    print(p3)

    s1 = Student("Emily", 20, "Mounds View", "Computer Science", 3.8)
    s2 = Student("Chris", 21, "St. Paul", "Biology", 3.5)
    s3 = Student("Taylor", 23, "Minneapolis", "Math", 3.9)

    print(s1.study())
    print(s2.study())
    print(s3.study())

    print(s1.update_gpa(3.9))
    print(s2.update_gpa(3.8))
    print(s3.update_gpa(3.8))

    print(f"Total person count: {Person.person_count}")

# Runs the main method
if __name__ == "__main__":
    main()
