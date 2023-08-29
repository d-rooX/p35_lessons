import os

class TreeNode:
    def __init__(self, name, is_file=False):
        self.name = name
        self.is_file = is_file
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def print_branch(self, indent=""):
        print(indent + self.name + (" (File)" if self.is_file else " (Folder)"))
        for child in self.children:
            child.print_branch(indent + "   ")


def build_file_tree(path, ignore_prefix=None):
    name = path.split('/')[-1]
    node = TreeNode(name)

    if ignore_prefix is not None:
        for prefix in ignore_prefix:
            if name.startswith(prefix):
                return None

    if os.path.isfile(path):
        node.is_file = True
    else:
        for child_name in os.listdir(path):
            child_path = os.path.join(path, child_name)
            child_node = build_file_tree(child_path, ignore_prefix=ignore_prefix)
            if child_node is not None:
                node.add_child(child_node)

    return node


root = build_file_tree('/home/droox/step_lessons', ignore_prefix=['.', '__'])
root.print_branch()
