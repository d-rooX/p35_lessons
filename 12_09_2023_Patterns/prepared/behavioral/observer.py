from abc import ABC, abstractmethod


# Observer interface
class Observer(ABC):
    @abstractmethod
    def update(self, event):
        pass

class Observable:
    def __init__(self):
        self._observers = []

    def notify(self, event):
        for observer in self._observers:
            observer.update(event)

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

# Subject (Observable) class
class Database(Observable):
    def __init__(self, conn_params):
        super().__init__()
        self.conn_params = conn_params

    @staticmethod
    def notify_after(event):
        def __wrapper(func):
            def _wrapper(self, *args, **kwargs):
                result = func(self, *args, **kwargs)
                self.notify(event)
                return result
            return _wrapper
        return __wrapper

    @notify_after('save')
    def save(self, data):
        print("Saving data to the database:", data)
        # self.notify("on_save", data)

    @notify_after('edit')
    def edit(self, data):
        print("Editing data in the database:", data)
        # self.notify("on_edit", data)

    @notify_after('delete')
    def delete(self, data):
        print("Deleting data from the database:", data)
        # self.notify("on_delete", data)


# Concrete Observer classes
class NotificationService(Observer):
    def update(self, event):
        print(f"Notification Service received event '{event}'")


class LoggingService(Observer):
    def update(self, event):
        print(f"Logging Service logged event '{event}'")


if __name__ == "__main__":
    # Client code

    # Create a database instance (Subject)
    database = Database('url_params')

    # Create concrete observer instances
    notification_service = NotificationService()
    logging_service = LoggingService()

    database.attach(notification_service)
    database.attach(logging_service)

    database.save("Some data")


