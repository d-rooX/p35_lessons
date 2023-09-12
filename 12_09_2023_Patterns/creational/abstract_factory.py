from abc import ABC, abstractmethod


########### ABSTRACT
class Button(ABC):
    def __init__(self, text):
        self.text = text

    @abstractmethod
    def render(self):
        pass


class Dialog(ABC):
    def __init__(self, text):
        self.text = text

    @abstractmethod
    def render(self):
        pass


class GuiFactory(ABC):
    @abstractmethod
    def create_button(self, text) -> Button:
        pass

    @abstractmethod
    def create_dialog(self, text) -> Dialog:
        pass

############ CONCRETE #########################

class WindowsButton(Button):
    def render(self):
        return f'[WindowsButton]{self.text}[WindowsButton]'


class WindowsDialog(Dialog):
    def render(self):
        return f'[WindowsDialog]{self.text}[WindowsDialog]'


class LinuxButton(Button):
    def render(self):
        return f'[LinuxButton]{self.text}[LinuxButton]'

class LinuxDialog(Dialog):
    def render(self):
        return f'[LinuxDialog]{self.text}[LinuxDialog]'


class WindowsGuiFactory(GuiFactory):
    def create_button(self, text) -> Button:
        return WindowsButton(text)

    def create_dialog(self, text) -> Dialog:
        return WindowsDialog(text)


class LinuxGuiFactory(GuiFactory):
    def create_button(self, text) -> Button:
        return LinuxButton(text)

    def create_dialog(self, text) -> Dialog:
        return LinuxDialog(text)


if __name__ == '__main__':
    PLATFORM = 'linux'
    GUI_FACTORIES = {
        'windows': WindowsGuiFactory(),
        'linux': LinuxGuiFactory(),
    }
    factory = GUI_FACTORIES.get(PLATFORM)
    if not factory:
        raise SystemError("Not supported platform")

    button = factory.create_button('OK')
    dialog = factory.create_dialog('Hello how are you?')

    print(button.render())
    print(dialog.render())
