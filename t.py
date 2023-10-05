def byky_ta_korovy():

    from random import randint
    number = []
    for i in range(4):
        number.append(randint(1, 9))

    counter = 0

    while True:
        a = int(input('Write number 1: '))
        b = int(input('Write number 2: '))
        c = int(input('Write number 3: '))
        d = int(input('Write number 4: '))
        counter += 1
        num = [a, b, c, d]

        print(number)
        byky = 0
        korovy = 0
        for i in range(4):
            if num[i] == number[i]:
                byky += 1
            elif num[i] in number:
                korovy += 1
        print(f'BYKY: {byky}; KOROVY: {korovy}.')
        if byky == 4:
            print(f"{num} is right number! You WIN! You have {counter} steps.")
            break

byky_ta_korovy()