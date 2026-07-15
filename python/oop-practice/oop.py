class Person:

    person_count = 0

    def __init__(self, name, age, city):

        self.name = name
        self.age = age
        self.city = city

        Person.person_count += 1

    # Greets The Person
    def greet(self):
        return f"Hello, I'm {self.name}, and I am {self.age} years old and I live in {self.city}."

    # Lets it be known whether the person has a birthday
    def have_birthday(self):
        self.age += 1
        return f"{self.name} is now {self.age} years old, and lives in {self.city}."

    # Prints out the contents of the user when using the print function
    def __str__(self):
        return  f"Person(name={self.name}, age={self.age}, city={self.city})"

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

    print(f"Total person count: {Person.person_count}")

# Runs the main method
if __name__ == "__main__":
    main()
