# list_types = {list, tuple, SinglyLinkedList}

#                           2
data = [1, 2, 3, True, "Hello!", 2.3343, [4, 5, 6, "hello", [2.333]], 7, 8]
#  [1, 2, 3, True, "Hello!' .... 4, 5, 6, 7, 8]

# for i in data:
#     print(i)

# def list_depth(data) -> int:
#     ...

# def list_flat(data) -> list:
#     ...

# flat_list = list_flat(data)
# print(flat_list)


lst1 = [1, 2, 3, 4, 5, 6, 7, 8, 9,
        [1, 2], [1, 3],
        [1, 4,
         [1, 5, [],
          [1, 2, 3,
           [4, []]
           ]
          ]
         ]
        ]
types = (list, tuple)


# def list_depth(lst: list) -> int:
#     depths = []
#     for i in lst:
#         if isinstance(i, types):
#             depths.append(1 + list_depth(i))
#
#     if depths:
#         return max(depths)
#     else:
#         return 0
#
def flat_list(input_list):
    f_list = []
    for item in input_list:
        if isinstance(item, list):
            f_list.extend(flat_list(item))
        else:
            f_list.append(item)
    return f_list


#

flat_l = flat_list(data)
print(flat_l)


# data = [1, 2, 3, True, 'Hello!', 2.3343, 4, 5, 6, 'hello', 2.333, 7, 8]
# chunk_size = 3

# [
#   [1, 2, 3],
#   [True, 'Hello!', 2.3343],
#   [4, 5, 6],
#   ['hello', 2.333, 7],
#   [8]
# ]

def split_chunks(data: list, chunk_size: int) -> list:
    ...


#  G  Guanine
#  C  Cytosine
#  T  Thymine
#  A  Adenine


#  G -> C
#  C -> G
#  T -> A
#  A -> U

# dict['G'] --> 'C'


dna = "GCTAGCTAGCTAGCTAGCTAGCTAGCTA"

#  CGAUCGAUCGAUCGAUCGAUCGAUCGAU
# "GCTAGCTAGCTAGCTAGCTAGCTAGCTA"

# def transcribe(dna):
#     ...


numbers = list(range(1, 50))

# new_numbers = []
# for num in numbers:
#     new_numbers.append(num ** 2)

new_numbers = map(lambda x: x ** 2, numbers)
even_numbers = filter(lambda x: x % 2 == 0, numbers)
# True False


# for i in even_numbers:
#     print(i)



is_authorised = True
is_admin = True
permissions = ['read', 'write']

# any()
# if is_authorised or is_admin or 'write' in permissions:

# all()
# ... and ... and ...
# if all([is_authorised, is_admin, 'write' in permissions]):
#     print('OK')
# else:
#     print('NOT OK')


# names = ['daniel', 'steven', 'eugene', 'artem']
# for index, name in enumerate(names):
#     print(f'Number of {name} = {index}')


days = [
    'monday',
    'tuesday',
    'wednesday',
    'thursday',
    'friday'
]

tasks = [
    'Do some work',
    'practice english',
    '',
    'Meet friends',
    ''
]

numbers = [
    0,
    1,
    2,
    3,
    4
]

# index = 0
# for day in days:
#     task = tasks[index]
#     print(f'{day} = {task}')
#     index += 1
# for day, task, number in zip(days, tasks, numbers):
#     print(day, '=', task, number)


# ASCII
# ord()
# chr()



# name = 'Daniel'
# eval("print('My name is', name)")

# +rep
print(('зима','весна','лето','осень')[(int(input('Enter month->'))%12//3)])


# class A:
#     def __init__(self, ..., ...):
#
#
#     def load_via_pickle_v2(self, filename):
#         with open(filename, "rb") as f:
#             data = pickle.load(f)
#             #так как закоментарено не работает. Почему?
#               # self.__init__(self, data.model, data.year, data.manufacturer, data.v_engine, data.color, data.price)
#             #ниже работает
#             self.__init__(data, data.model, data.year, data.manufacturer, data.v_engine, data.color, data.price)
#             print(f"Данные авто {self.manufacturer} {self.model} загружены из файла {filename}.")
#             return
#
#     def foo(self):
#         pass

# a = A()
# # a.foo()
# A.foo(a)
# A.__init__(a, )
