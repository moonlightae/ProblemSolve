while True:
    try:
        a = int(input())
        i = 1
        while True:
            alpha = int('1' * i)
            if alpha % a == 0:
                print(i)
                break
            i += 1

    except EOFError:
        break