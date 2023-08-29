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
        self.size = 0

    def clear(self):
        self.__init__()

    def append(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            self.tail = node
            self.size += 1
            return

        self.tail.next = node
        self.tail = node
        self.size += 1

    def insert(self, index, data):
        node = Node(data)

        if index == 0:
            node.next = self.head
            self.head = node
            self.size += 1
            return

        if index >= self.size:
            self.append(data)
            return

        current_index = 1
        previous = self.head
        current = self.head.next
        while current:
            if current_index == index:
                previous.next = node
                node.next = current
                self.size += 1
                return
            previous = current
            current = current.next
            current_index += 1

    def pop(self, index=None):
        if index is None:
            index = self.size - 1

        if self.size == 0:
            raise IndexError("pop from empty list")

        if index == 0:
            node = self.head
            self.head = self.head.next
            self.size -= 1
            return node.data

        current_index = 1
        previous = self.head
        current = self.head.next
        while current:
            if current_index == index:
                previous.next = current.next
                if index == self.size - 1:
                    self.tail = current.n
                
                self.size -= 1
                return current.data
            previous = current
            current = current.next
            current_index += 1

    def __str__(self):
        text = '['
        for i in self:
            text += str(i) + ', '

        text = text.removesuffix(', ')
        text += ']'

        return text

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.data
            current = current.next

    def __len__(self):
        return self.size

    def __getitem__(self, index):
        if type(index) is not int:
            raise IndexError(f"List is using indexes, not {type(index)}")

        if index > self.size - 1:
            raise IndexError(f"Out of range")

        if index == self.size - 1:
            return self.tail.data

        current_index = 0
        current = self.head
        while current:
            if current_index == index:
                return current.data

            current = current.next
            current_index += 1


# sll.append("one")
# sll.append("two")
# sll.append("three")
# sll.append("4")
# sll.append("5")
# sll.append("6")
#
# # for i in sll:
# #     print(i)
#
# print(sll)

import time

sll = SinglyLinkedList()
# sll = []

# start_time = time.time()
# for i in range(100000):
#     sll.append(i)
#
# print(time.time() - start_time)

# a = [0, 1, 2, 3]
# print(a)
# a.insert(1, "HELLO")
# print(a)


sll.append(1)
sll.append(2)
sll.append(3)
sll.append(4)
sll.append(5)

print(sll)
sll.insert(5, "HELLO")
print(sll)
# print(sll[1])
# print(sll[5])

sll1 = SinglyLinkedList()
sll1.append(1)
sll1.append(2)
sll1.append(3)

print(sll + sll1)   ######### todo __add__

# print(len(sll))
#
# sll.clear()
# print(sll)

# Stack
# Queue

# '{1123123{{{{}'  False
# '((({<>})))'     True



