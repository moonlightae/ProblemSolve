def stonegame(f, b, c):
    if c == 1:
        return f
    elif c <= 3:
        return stonegame(b, f, c-1)
    else:
        return stonegame(b, f, c-3)

print(stonegame("SK", "CY", int(input())))