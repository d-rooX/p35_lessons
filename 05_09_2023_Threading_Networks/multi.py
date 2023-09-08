# Multithreading

import random
import time
import threading

# thread - Потік

def timer(end_time):
    while True:
        current_time = time.strftime("%H:%M:%S")
        print(current_time)
        if current_time == end_time:
            print('Timer done!')
            break
        time.sleep(1)

def square(numbers):
    result = []
    for num in numbers:
        time.sleep(0.05)
        result.append(num ** 2)
    # print('Square done!')
    return result

def cube(numbers, result):
    for num in numbers:
        result.append(num ** 3)
    print('Cube done!')


def generate_numbers(count_numbers):
    numbers = []
    for i in range(count_numbers):
        random_number = random.randint(0, 10000)
        numbers.append(random_number)
    return numbers


numbers = generate_numbers(100)
square_result = []
cube_result = []

square_thread = threading.Thread(target=square, args=(numbers, ))
cube_thread = threading.Thread(target=cube, args=(numbers, cube_result))
# timer_thread = threading.Thread(target=timer, args=('19:57:00',))

print('Starting threads...')

square_thread.start()
cube_thread.start()
# timer_thread.start()

# square(numbers, square_result)
# cube(numbers, cube_result)

print(cube_result[:50])

square_thread.join()
print(square_result[:50])

print('Done')



# {
#     'nick': Stepflix(),
#     'nick1': Stepflix(),
#     'nick2': Stepflix(),
#     'nick3': Stepflix(),
# }
