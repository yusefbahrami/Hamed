class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


class SLL:
    def __init__(self) -> None:
        self.first = None

    def insert(self, newNode: Node):
        # insert node at first of SLL
        if self.first is None:
            self.first = newNode
        else:
            newNode.next = self.first
            self.first = newNode

    def search(self, callback: function, key):
        temp = self.first
        while temp:
            if callback(key):
                return True
            temp = temp.next
        return False
