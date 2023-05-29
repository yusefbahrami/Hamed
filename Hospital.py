from Doctor import Doctor
from Patients import Patients
from Hash import HashTable


class Hospital:
    def __init__(self) -> None:
        self.doctor_DS = HashTable()
        self.patients_DS = HashTable()

    def insert(self, node, DS: HashTable):
        DS.insert(node)
