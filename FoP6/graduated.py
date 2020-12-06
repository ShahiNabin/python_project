from FoP6.student import Student


class Graduated(Student):

    # constructor
    def __init__(self, name, age):
        super().__init__(name, age)

    # accessors
    def age(self, n=None):  # getter-setter for age
        if n is not None: self._age = n
        return self._age

    # other methods
    def birthday(self):
        self.age(self.age() + 1)
