class TaskModel:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def get_tasks(self):
        return self.tasks


class TaskView:
    def show_tasks(self, tasks):
        for task in tasks:
            print(task)

    def prompt_new_task(self):
        return input("Введіть нове завдання: ")


class TaskController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_task(self, task):
        self.model.add_task(task)

    def show_tasks(self):
        tasks = self.model.get_tasks()
        self.view.show_tasks(tasks)

    def run(self):
        while True:
            choice = input("Оберіть опцію: \n"
                           "1 - Додати завдання\n"
                           "2 - Показати завдання\n"
                           "q - Вийти\n:")
            if choice == '1':
                task = self.view.prompt_new_task()
                self.add_task(task)
            elif choice == '2':
                self.show_tasks()
            elif choice == 'q':
                break


if __name__ == '__main__':
    view = TaskView()
    model = TaskModel()
    controller = TaskController(model, view)
    controller.run()


# PRACTICE
# Model Movie
#   name
#   genre
#
#   producer
#   year
#   duration
#   studio
#   actors : list[str]















