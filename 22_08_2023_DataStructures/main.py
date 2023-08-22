class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        node = Node(data)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node

    def insert(self, data, index):
        node = Node(data)

        if index == 0:
            node.next = self.head
            self.head = node
            return

        current = self.head
        prev = self.head
        current_index = 0

        while current:
            if current_index == index:
                prev.next = node
                node.next = current
                return

            prev = current
            current = current.next
            current_index += 1

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def __len__(self):
        count = 0
        for _ in self:
            count += 1
        return count


sll = SinglyLinkedList()
sll.append("1")
sll.append("2")
sll.append("3")

for i in sll:
    print(i)

print('____')

sll.insert("INSERTED", 0)

for i in sll:
    print(i)

print("Len:", len(sll))



