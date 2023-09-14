from abc import ABC, abstractmethod


#### ABSTRACT
class Button:
    def __init__(self, text):
        self.text = text
    
    @abstractmethod
    def render(self):
        pass

class Dialog:
    def __init__(self, text):
        self.text = text
    
    @abstractmethod
    def render():
        pass

class GuiFactory(ABC):
    @abstractmethod
    def create_button(text) -> Button:
        pass

    @abstractmethod
    def create_dialog(text) -> Dialog:
        pass


#### CONCRETE
class WindowsButton(Button):        
    def render(self):
        return f'[WindowsButton]{self.text}[WindowsButton]'

class LinuxButton(Button):
    def render(self):
        return f'[LinuxButton]{self.text}[LinuxButton]'

# Another Buttons implementation
# ...


class WindowsDialog(Dialog):
    def render(self):
        return f'[WindowsDialog]{self.text}[WindowsDialog]'
        
class LinuxDialog(Dialog):
    def render(self):
        return f'[LinuxDialog]{self.text}[LinuxDialog]'

# Another Dialogs implementation
# ...


## FACTORIES
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
    factories = {
        'windows': WindowsGuiFactory(),
        'linux': LinuxGuiFactory()
    }
    
    gui_factory: GuiFactory = factories.get(PLATFORM)
    if not gui_factory:
        print("Platform is not available")
        exit()    
    
    
    dialog = gui_factory.create_dialog("Hello!")
    print(dialog.render())
    
    
    button = gui_factory.create_button("Hello!")
    print(button.render())
    