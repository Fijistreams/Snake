class Node:
    def __init__(self, data = None):
        self.data = data
        self.nextnode = None

    def changeY(self, amount):
        self.data[1] += amount
