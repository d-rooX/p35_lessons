# Data Structures

# list, dict, set, tuple

a = []
# index... slice

b = {}
# key: value, ....

#           0               1                   INDEX
# user = ["Daniel", 20, "Python Developer"]


# KEY
# user = {
#     'name': 'Daniel',
#     'age': 20
# }

# websites = {
#     'one': 'google.com',
#     'two': 'notion.so',
# }

# O(n)  Big-O notation


# def foo():
    # O(1)
    #
    # print("Hello!")    # 1
    # a = 10             # 1
    # c = a + 200        # 1
    # print(a)           # 1

    # O(1 + 1 + 1 + 1) = O(4)
    # O(1)

# def prepare(guests):        # n
#     for guest in guests:    # n
#         prepare_seats()     # 1
#         prepare_food()      # 1
#
    # 1 + 1 + n = O(2 + n) = O(n)

# O(n^2)
# def prepare(guests):
#     for guest in guests:
#         for guest_friend in guests:
#             print(guest, 'said hello to', guest_friend)

# prepare(['Daniel', 'Steve', 'John', 'William'])


# List      -  1, 2, 3, 4, 5
# Stack     -  [0], 1, 2, 3, 4
#
#           ___
#           ___
#           ___
#
# Queue     -
# Tree


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        node = Node(data)

        if self.head is None:
            self.head = node
            return

        current = self.head
        while current is not None:
            if current.next is None:
                current.next = node
                return
            current = current.next

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current.data
            current = current.next


sll = SinglyLinkedList()
sll.append("one")
sll.append("two")
sll.append("three")

for i in sll:
    print(i)







