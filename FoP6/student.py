class Student:

    # constructor
    def __init__(self, name, age):
        self._name = name
        self._age = age
        self._learning = False

    # accessors
    def name(self, n=None):  # getter-setter for name
        if n is not None: self._name = n
        return self._name

    def age(self, n=None):  # getter-setter for age
        if n is not None: self._age = n
        return self._age

    def learning(self, n=None):  # getter-setter for learning
        if n is not None: self._learning = n
        return self._learning

    # other methods
    def study(self):
        self.learning(not self.learning())
