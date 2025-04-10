while True:
    N = list(map(int, input().split()))
    if N == [0, 0, 0]:
        break
    elif N.pop(N.index(max(N))) ** 2 == N[0] ** 2 + N[1] ** 2:
        print("right")
    else:
        print("wrong")
