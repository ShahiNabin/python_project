from FoP6.student import Student
from FoP6.graduated import Graduated


def main():
    jackey = Student('Jackey', 18)  # Student initialization
    print(jackey.name())
    print(jackey.age())
    print(jackey.learning()) # by default False
    jackey.study() # by call of study() it's switched
    print(jackey.learning()) # switched so now True
    jackey.study()# by call of study() it's switched
    print(jackey.learning()) # switched so now False ...

    print()

    charlie = Graduated('Charlie', 22)  # Graduated initialization
    print(charlie.name())
    print(charlie.age())
    charlie.birthday() # by call of birthday() it's going to increment age
    charlie.birthday() # by call of birthday() it's going to increment age
    charlie.birthday() # by call of birthday() it's going to increment age
    print(charlie.age())

if __name__ == '__main__': main()
