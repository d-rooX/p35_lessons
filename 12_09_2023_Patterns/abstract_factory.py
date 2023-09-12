
class Button:
    def __init__(self, text) -> None:
        self.text = text
    
    def render_html(self):
        return f'<button>{self.text}</button>'
    
    def render_windows(self):
        return f'[Windows]{self.text}[Windows]'
    
    def render_linux(self):
        return f'[Linux]{self.text}[Linux]'
    
    def render_macos(self):
        return f'[MacOS]{self.text}[MacOS]'
        

class Dialog:
    def __init__(self, text) -> None:
        self.text = text
    
    def render_html(self):
        return f'<button>{self.text}</button>'
    
    def render_windows(self):
        return f'[WindowsButton]{self.text}[WindowsButton]'
    
    def render_linux(self):
        return f'[LinuxButton]{self.text}[LinuxButton]'
    
    def render_macos(self):
        return f'[MacOSButton]{self.text}[MacOSButton]'
        


if __name__ == '__main__':
    PLATFORM = 'windows'
    
    dialog = Dialog('Hello!')
    if PLATFORM == 'windows':
        dialog.render_windows()
    elif PLATFORM == 'linux':
        dialog.render_linux()
    ...
    
    
    button = Button('OK')
    if PLATFORM == 'windows':
        button.render_windows()
    elif PLATFORM == 'linux':
        button.render_linux()
    ...
    
    
    
    
    
