# Component: The base class for all objects in the hierarchy
class FileSystemComponent:
    def __init__(self, name):
        self.name = name

    def display(self, indent=""):
        pass


# Leaf: Represents a file
class File(FileSystemComponent):
    def __init__(self, name):
        super().__init__(name)

    def display(self, indent=""):
        print(indent + self.name)


# Composite: Represents a directory containing files and subdirectories
class Directory(FileSystemComponent):
    def __init__(self, name):
        super().__init__(name)
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def display(self, indent=""):
        print(indent + self.name + " (Directory)")
        for child in self.children:
            child.display(indent + "  ")


# Usage example
if __name__ == "__main__":
    # Create files
    file1 = File("file1.txt")
    file2 = File("file2.txt")
    file3 = File("photo.jpg")

    d = Directory('files')
    d.add_child(file1)
    d.add_child(file2)
    d.add_child(file3)

    d1 = Directory('another stuff')
    d1.add_child(File('some_trash.txt'))
    d1.add_child(File('pic.jpg'))

    d.add_child(d1)
    d.display()


    # # Create directories and add files to them
    # directory1 = Directory("Documents")
    # directory1.add_child(file1)
    # directory1.add_child(file2)
    #
    # directory2 = Directory("Pictures")
    # directory2.add_child(file3)
    #
    # # Create the root directory and add directories to it
    # root_directory = Directory("Root")
    # root_directory.add_child(directory1)
    # root_directory.add_child(directory2)
    #
    # # Display the entire file system hierarchy
    # root_directory.display()
    # print()
    #
    # # Display separate file
    # file1.display()
