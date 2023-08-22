from node import Node

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node

    def pop(self):
        if not self.top:
            return None

        node = self.top
        self.top = node.next
        return node.data

    def peek(self):
        if not self.top:
            return None

        return self.top.data


brackets_map = {
    '{': '}',
    '(': ')',
    '[': ']',
    '<': '>',
}

def are_brackets_balanced(text):
    stack = Stack()

    for char in text:
        if char in brackets_map:
            stack.push(char)

        elif char in brackets_map.values():
            last_bracket = stack.pop()
            if last_bracket is None:
                return False

            closing_bracket = brackets_map[last_bracket]
            if last_bracket is None or closing_bracket != char:
                return False

    return stack.peek() is None


if are_brackets_balanced('Hello (by the way)} my dear!'):
    print('YES')
else:
    print('NO')
