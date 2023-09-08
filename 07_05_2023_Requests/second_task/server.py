weather = {
    'Kyiv': '25C 5m/s Rainy',
    'Mykolaiv': '23C 1m/s Sunny',
    'Kharkiv': '25C 5m/s Rainy',
    'Odessa': '25C 5m/s Rainy',
}

def listen_client():
    while True:
        city = ...  # recv
        weather_in_city = weather[city]
        ...  # send
