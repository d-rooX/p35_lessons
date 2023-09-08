import requests
import time

# HTTP
# Hypertext Transport Protocol


# Method
#     отримати, надіслати, видалити, змінити
# GET  - отримуємо
# POST - надсилаємо
# PUT  - змінюємо
# DELETE - видаляємо

picture = "https://picsum.photos/1920/1080"

for i in range(10):
    start_time = time.time()
    response = requests.get(picture)
    print(response.status_code)

    # text    ---> str
    # content ---> bytes

    picture_bytes = response.content

    with open(f'pictures/picture_{i}.png', 'wb') as file:
        file.write(picture_bytes)

    print(f'Picture {i} downloaded for {time.time() - start_time} seconds')
