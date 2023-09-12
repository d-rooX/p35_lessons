from abc import ABC, abstractmethod


# Command interface
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


# Receiver class: TextEditor
class TextEditor:
    def __init__(self):
        self.text = ""

    def insert_text(self, text_to_insert):
        self.text += text_to_insert

    def delete_text(self, start, end):
        self.text = self.text[:start] + self.text[end:]

    def get_text(self):
        return self.text


# Concrete command classes
class InsertCommand(Command):
    def __init__(self, editor, text_to_insert):
        self.editor = editor
        self.text_to_insert = text_to_insert

    def execute(self):
        self.editor.insert_text(self.text_to_insert)


class DeleteCommand(Command):
    def __init__(self, editor, start, end):
        self.editor = editor
        self.start = start
        self.end = end

    def execute(self):
        self.editor.delete_text(self.start, self.end)


# Invoker class: Button
class Button:
    def __init__(self, command):
        self.command = command

    def click(self):
        self.command.execute()


if __name__ == "__main__":
    # Client code

    # Create a TextEditor (Receiver)
    text_editor = TextEditor()

    # Create concrete command objects
    insert_command = InsertCommand(text_editor, "Hello, World")
    delete_command = DeleteCommand(text_editor, 0, 5)  # Delete "Hello"

    # Create buttons (Invoker) and associate them with commands
    insert_button = Button(insert_command)
    delete_button = Button(delete_command)

    # Click the buttons to execute the commands
    insert_button.click()
    delete_button.click()

    # Check the text in the editor
    edited_text = text_editor.get_text()
    print("Edited Text:", edited_text)  # Output: "Edited Text: , "
