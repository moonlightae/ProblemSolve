def d2b(n):
    if n == 0:
        return 0
    else:
        return int(str(d2b(n//2)) + str(n % 2))

print(d2b(int(input())))
