from node import Node


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data):
        node = Node(data)
        if self.tail:
            self.tail.next = node
            self.tail = node
        else:
            self.head = node
            self.tail = node
        self.size += 1

    def insert(self, data, index):
        node = Node(data)

        if index == 0:
            node.next = self.head
            self.head = node
            self.size += 1
            return

        current, prev = self.__getitem_with_prev(index)
        node.next = current
        prev.next = node

    def __getitem_with_prev(self, index):
        current = self.head
        prev = self.head
        current_index = 0

        while current:
            if current_index == index:
                return current, prev
            prev = current
            current = current.next
            current_index += 1

        raise Exception("out of index")

    def __getitem__(self, index):
        node, prev = self.__getitem_with_prev(index)
        return node.data

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

sll.insert("INSERTED", 6)

for i in sll:
    print(i)

print("Len:", len(sll))



