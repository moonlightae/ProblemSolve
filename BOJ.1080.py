n, m = map(int, input().split())
if n < 3 or m < 3:
    print(-1)
else:
    l = [[] for _ in range(n)]
    r = [[] for _ in range(n)]
    for i in range(n):
        l[i] = list(map(int, list(input())))
    for i in range(n):
        r[i] = list(map(int, list(input())))
    s = [[] for _ in range(n)]
    for i in range(n):
        s[i] = list(map(lambda x, y: 0 if x == y else 1, l[i], r[i]))
    ss = 0
    while True:
        c = 0
        for i in range(n-2):
            for j in range(m-2):
                if s[i][j] == 1:
                    s[i][j] = (s[i][j] + 1) % 2
                    s[i+1][j] = (s[i+1][j] + 1) % 2
                    s[i+2][j] = (s[i+2][j] + 1) % 2
                    s[i][j+1] = (s[i][j+1] + 1) % 2
                    s[i+1][j+1] = (s[i+1][j+1] + 1) % 2
                    s[i+2][j+1] = (s[i+2][j+1] + 1) % 2
                    s[i][j+2] = (s[i][j+2] + 1) % 2
                    s[i+1][j+2] = (s[i+1][j+2] + 1) % 2
                    s[i+2][j+2] = (s[i+2][j+2] + 1) % 2
                    c += 1
        ss += c
        if c == 0:
            print(ss)
            break