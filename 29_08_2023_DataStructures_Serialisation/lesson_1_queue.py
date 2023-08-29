class Stack:
    def __init__(self):
        self._stack = []

    def push(self, data):
        self._stack.append(data)

    def pop(self):
        self._stack.pop()

    def peek(self):
        return self._stack[-1]


class Queue:
    def __init__(self):
        self._queue = []

    def push(self, data):
        self._queue.append(data)

    def pop(self):
        return self._queue.pop(0)

    def peek(self):
        return self._queue[0]


support_queue = Queue()
support_queue.push("First question!")
support_queue.push("Second question!")

print(support_queue.pop())

support_queue.push("Third question!")
support_queue.push("Fourth question!")
support_queue.push("Fifth question!")


class WebBrowser:
    def __init__(self):
        self.current_page = None

    def open_page(self, url):
        ...

    def previous_page(self):
        ...

    def next_page(self):
        ...


# current_page = None ::::: New Tab page
wb = WebBrowser()
wb.open_page('google.com')
wb.open_page('wikipedia.com')
wb.previous_page()
print(wb.current_page)
wb.next_page()


class WebBrowser:
    def __init__(self):
        self.current_page = 0
        self.pagelist = []

    def open_page(self, url):
        self.pagelist.append(url)
        self.current_page += 1

    def previous_page(self):
        current_page = self.current_page - 1
        return self.pagelist[current_page]

    def next_page(self):
        current_page = self.current_page + 1
        return self.pagelist[current_page]

    def current_page(self):
        return self.pagelist[self.current_page]
