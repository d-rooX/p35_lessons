# Meta - Над


# class CountedClass(Foo, ):

# class ExampleMetaclass(type):
#     # __new__ --> create object/class
#     # __init__ --> fill created object/class with attributes
#     # __call__ --> call object
#
#     def __call__(cls, *args, **kwargs):
#         # x = type.__new__(cls)
#         print(cls)
#         print(args)
#         return super().__call__(*args, **kwargs)


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance

        return cls._instances[cls]


class DBConnection(metaclass=SingletonMeta):
    def __init__(self, conn_params):
        self.conn_params = conn_params

    def save(self, data):
        print(f'Saving data: {data} to db')

# u = User()       # type.__call__(User)
# User.__call__(u)
# u()
# print(u.__dict__)

# u = User("Daniel")
# print(u.name)      # Daniel
#
# u1 = User("Steven")
# print(u1.name)     # Steven
#
#
# print(u is u1)
# print(u)
# print(u1)

db = DBConnection('sqlite://memory')
db1 = DBConnection('postgresql://...')

print(db1.conn_params)
