from Person import Person


class Node:
    def __init__(self, data: Person) -> None:
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self) -> None:
        self.root = None

    def insert(self, node: Node):
        temp = self.root
        while True:
            if temp == None:
                self.root = node
                break
            elif node.data.code > temp.data.code:
                if temp.right == None:
                    temp.right = node
                    break
                else:
                    temp = temp.right
            elif node.data.code < temp.data.code:
                if temp.left == None:
                    temp.left = node
                    break
                else:
                    temp = temp.left

    def find(self, node: Node):
        temp = self.root
        while temp:
            if node.data.code == temp.data.code:
                return temp
            elif node.data.code > temp.data.code:
                temp = temp.right
            else:
                temp = temp.left
        return None

    def inOrder(self, node: Node):
        if node:
            print(node.data.code)
            self.inOrder(node.left)
            self.inOrder(node.right)
