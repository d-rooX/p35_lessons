from typing import Any


class SingletonMeta(type):
    _instances = {}
    
    def __call__(cls, *args: Any, **kwds: Any) -> Any:
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwds)
            cls._instances[cls] = instance
        return cls._instances[cls]


class DBConnection(metaclass=SingletonMeta):
    def __init__(self, login, password) -> None:
        self.login = login
        self.password = password
    
    def get_connection_info(self):
        return f'{self.login}:{self.password} ({id(self)})'
        

connection = DBConnection('droox', '123')
print(connection.get_connection_info())

another_connection = DBConnection('user', '123')
print(another_connection.get_connection_info())






        