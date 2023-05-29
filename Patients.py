from Person import Person


class Patients(Person):
    def __init__(self, name, lastName, age, code) -> None:
        super().__init__(name, lastName, age, code)
        self.visitedBy = None
