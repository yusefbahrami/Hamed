# from SLL_DS import Node, SLL
from BST_DS import Node, BST
from Person import Person


class HashTable:
    def __init__(self, capacity=10) -> None:
        self.capacity = capacity
        self.size = 0
        self.table = [None]*self.capacity

    def hashFuntion(self, data: int) -> int:
        return data % self.capacity

    def insert(self, node: Person) -> None:
        index = self.hashFuntion(node.code)
        if not self.search(node, index):
            newNode = Node(node)
            if self.table[index] == None:
                newDS = BST()
                newDS.insert(newNode)
                self.table[index] = newDS
            else:
                DS: BST = self.table[index]
                DS.insert(newNode)
            self.size += 1
        else:
            print(
                f"name: {node.name} {node.lastName}, code:{node.code}, is exist")

    def search(self, data: Person, hashIndex) -> bool:
        if self.table[hashIndex] == None:
            return False
        node = Node(data)
        DS: BST = self.table[hashIndex]
        return DS.find(node)


if __name__ == "__main__":
    h = HashTable()
    p1 = Person('ali', 'reza', 45)
    p2 = Person('ahmad', 'reza', 74)
    p3 = Person('amir', 'mamad', 16)
    p4 = Person('amir', 'mamad', 16)
    h.insert(p1)
    h.insert(p2)
    h.insert(p3)
    h.insert(p4)
    print(h.table)
