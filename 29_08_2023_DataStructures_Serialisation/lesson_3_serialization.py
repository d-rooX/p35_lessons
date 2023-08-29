#  PROBLEM
# need to save data

# SERIALIZATION
# DESEREALIZATION

# class User:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def say_hello(self):
#         print(f'Im {self.name}, {self.age} y.o')
#
#     def __reduce__(self):
#         return (exec, ('import webbrowser; webbrowser.open("google.com")',))


#####################################################3

# import pickle
# import json
##    JAVASCRIPT OBJECT NOTATION

# import shelve


# user1 = User(name="Steven", age=25)
# shlv = shelve.open('data.pkl')
# shlv['user'] = user1
# print(shlv['user'])

# user1_dict = {
#     'name': "Steven",
#     'age': 25,
#     'is_programmer': True,
#     'skills': ['Python', 'C#', ['one', 'two']]
# }
# # print(user1_dict)
#
# dumped_user = json.dumps(user1_dict)
# print(type(dumped_user))
# user1_undumped = json.loads(dumped_user)
# print(type(user1_undumped))
# print(user1_undumped)

# print(pickle.dumps(user1))

# with open('user1', 'wb') as f:
#     pickle.dump(user1, f)

# with open('user1', 'rb') as f:
#     user1 = pickle.load(f)
#
# print(user1.name)
# user1.say_hello()

# pickle/json.dump()  DUMP ---> file
# pickle/json.load()  LOAD <--- file
# pickle/json.loads()  LOADS <--- string
# pickle/json.dumps()  DUMPS ---> string

# a = open('file.txt', 'w')
# a.write(f'{user1.name}\n{user1.age}')
# a.close()
#
# a = open('file.txt', 'r')
# data = a.read().split('\n')
# a.close()
