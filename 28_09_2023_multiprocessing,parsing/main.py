import os
import time
import string

# GIL Global Interpreter Lock


# Threading
# <APP>
#    - Thread
#    - Thread
#    - Thread
#    - Thread
#    - Thread


# Multiprocessing
# <APP>
# |   - Thread
# |
# <Subprocess>
#     - Thread
#     - Thread
#     - 
##########
from multiprocessing import Pool, Pipe, Process, Lock
import requests
import random


def print_some_info(l, text):
    time.sleep(random.randint(1, 2))

    l.acquire()
    try:
        print("Hello world!", text)
    finally:
        l.release()


def square(conn, x):
    conn.send(x ** 2)
    time.sleep(1)
    print(conn.recv())
    conn.close()


def get_picture(url):
    response = requests.get(url)
    pic_bytes = response.content

    chars = string.ascii_letters
    suffix = "".join(random.sample(chars, 5))
    id = random.randint(0, 10000)
    filename = f'./{id}_{suffix}.jpg'
    with open(filename, 'wb') as file:
        file.write(pic_bytes)

    return filename


def find_filename_in_directory(path):
    filename = 'file'
    found_filenames = []

    for cur_path, _, filenames in os.walk(path):
        if filename in filenames:
            found_filenames.append(os.path.join(cur_path, filename))

    return found_filenames


if __name__ == '__main__':
    ### Pool
    # urls = ['https://picsum.photos/500/500' for i in range(50)]

    # start_time = time.time()

    # for url in urls:
    #     get_picture(url)

    # with Pool(10) as p:
    #     print(p.map(get_picture, urls))

    # print(f"Elapsed time: {time.time() - start_time}")

    ### Pipe
    # parent_con, child_conn = Pipe()
    # p = Process(target=square, args=(child_conn, 6005543433))
    # p.start()
    # print(parent_con.recv())
    # parent_con.send("Hello world!")
    # p.join()

    ### Lock
    # lock = Lock()
    # for num in range(20):
    #     Process(target=print_some_info, args=(lock, num)).start()
    #     print('added some process')

    paths = ['/usr/bin', '/usr/share', '/']

    with Pool(3) as p:
        result = p.map(find_filename_in_directory, paths)
    print(result)
