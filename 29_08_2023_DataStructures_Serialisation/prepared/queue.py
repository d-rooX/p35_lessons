class Queue:
    def __init__(self):
        self._queue = []
    
    def push(self, data):
        self._queue.append(data)
    
    def pop(self):
        return self._queue.pop(0)

    @property
    def is_empty(self):
        return len(self._queue) == 0
    
    def __iter__(self):
        for _ in range(len(self._queue)):
            yield self.pop()
    
    def __len__(self):
        return len(self._queue)

    def __str__(self):
        return str(self._queue)
    
q = Queue()

q.push(1)
q.push(2)
q.push(3)
q.push(4)

for i in q:
    print(i)

##########################################

class Movie:
    def __init__(self, title):
        self.title = title
        
    def __repr__(self) -> str:
        return self.__str__()
    
    def __str__(self):
        return f'Movie<{self.title}>'


class Episode:
    def __init__(self, title, series):
        self.title = title
        self.series = series
    
    def __str__(self) -> str:
        return f'Episode<{self.title}, {len(self.series)} series>'


class Serial:
    def __init__(self, title, episodes):
        self.title = title
        self.episodes = episodes    
    
    def __str__(self) -> str:
        return f'Serial<{self.title}, {len(self.episodes)}>'
    

class Stepflix:
    def __init__(self, username):
        self.username = username
        self.currently_watching = None
        self._watch_queue = Queue()
    
    def next_movie(self):
        ...

    def add_to_watchlist(self, obj: Serial | Episode | Movie):
        ...



mandalorian = Serial(
    "Mandalorian",
    episodes=[
        Episode("Episode 1", series=[
            Movie("New friends"),
            Movie("Returning"),
            Movie("Another troubles"),
        ]),
        Episode("Episode 2", series=[
            Movie("Little more troubles"),
            Movie("Boss fight"),
            Movie("Finally calm"),
            Movie("Some shit again"),
        ]),
        Episode("Episode 3", series=[
            Movie("New episode"),
        ]),
    ]
)

stepflix = Stepflix("droox")
stepflix.add_to_watchlist(mandalorian)
print(stepflix.currently_watching)
stepflix.next_movie()
stepflix.next_movie()
print(stepflix.currently_watching)
