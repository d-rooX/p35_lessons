import pickle
import pathlib
from queue import *

if pathlib.Path('./stepflix').exists():
    with open("./stepflix", 'rb') as f:
        stepflix = pickle.load(f)

    print("Loaded!")
else:
    stepflix = Stepflix('droox')
    stepflix.add_to_watchlist(mandalorian)

    with open('./stepflix', 'wb') as f:
        pickle.dump(stepflix, f)

    print("Saved!")


print(stepflix._watch_queue)
print(stepflix.currently_watching)
stepflix.next_movie()
print(stepflix.currently_watching)
stepflix.next_movie()
print(stepflix.currently_watching)
stepflix.next_movie()
print(stepflix.currently_watching)
stepflix.next_movie()
print(stepflix.currently_watching)
stepflix.next_movie()
