t = input()


def pal(t):
    if len(t) == 0 or len(t) == 1:
        return True
    else:
        if t[0] == t[-1]:
            return pal(t[1:-1])
        else:
            return False


print(pal(t))