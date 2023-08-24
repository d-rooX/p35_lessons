## lesson:
### decorator
### generator


#######################
# decorator

# def say_name_and_age(name, age):
#     print(name, age)
#
#
# data = [
#     ["Steven", 20],
#     ["Daniel", 25],
#     ["John", 23],
#     ["Steven", 24],
# ]
#
# kwargs = {
#     'name': 'Daniel',
#     'age': 20,
# }
# for row in data:
# say_name_and_age(**kwargs,  name='Daniel')


# counter = 0
#
# def count_calls(func):
#     global counter
#
#     def wrapper(*args, **kwargs):
#         global counter
#         result = func(*args, **kwargs)
#
#         # counter += 1
#
#         return result
#
#     counter += 1
#
#     return wrapper
#
#
# @count_calls
# def foo(name):
#     a = 10
#     b = 15
#     c = (a + b) ** a
#     print(f'Hello, {name}! {c}')
#     return c
#
# @count_calls
# def foo1():
#     pass


# foo = count_calls(foo)
#
#
# a = foo("Steven")
# print(foo("Name1") + foo("Name2"))
# print(a)
#
# print(counter)



####### generator

#        [......]
# for i in range(1000):
#     print(i)

# print(type(range(1000)))
# print(*range(1000))
# print(0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# current_line = 10
#
# def generator(limit):
#     c = 0
#     while c < limit:
#         yield c
#         c += 1

# def multiple_yields():
#     c = 0
#     while True:
#         yield 0
#         yield 1
#         yield 2
#        c += 1


# for value in infinity_generator():
#     print(value)

# inf = infinity_generator()
#
# print(next(inf))
# print(next(inf))
# inf1 = infinity_generator()
#
# print(next(inf))
# print(next(inf1))

# a = (i for i in [1, 2, 3, 4])
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
#
# for i in a:
#     print(i)

# def foo():
#     g = generator(100)
#     while True:
#         yield from g
#
#
# for i in foo():
#     print(i)
