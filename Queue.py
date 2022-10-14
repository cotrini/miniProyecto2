class Queue:

    def __init__(self):
        self.items = []

    def isEmpty(self): #False when this queue have any element
        return not bool(self.items)

    def enQueue(self, item):
        self.items.insert(0,item)

    def deQueue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def toString(self):
        print(self.items)

