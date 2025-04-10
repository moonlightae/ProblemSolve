N, r, c = map(int, input().split())
value = 0
for i in range(N):
    size = 2 ** N
    if c > (size - 1) // 2:
        c -= size // 2

        if r > (size - 1) // 2:
            r -= size // 2
            locate = 3

        else:
            locate = 1

    else:
        if r > (size - 1) // 2:
            r -= size // 2
            locate = 2
        else:
            locate = 0
    value += locate * (2 ** ((N - 1) * 2))
    N -= 1
print(value)
