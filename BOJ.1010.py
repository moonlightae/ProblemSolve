T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    n, m = 2, 1
    Table = [[0] for _ in range(N)]
    Table.insert(0, [1 for _ in range(M+1)])
    Table[1] = [_ for _ in range(M+1)]
    if N != 1:
        while True:
            Table[n].append(0)
            if n < m:
                Table[n][m] = Table[n-1][m-1] + Table[n][m-1]
            elif n == m:
                Table[n][m] = 1
            elif n > m:
                Table[n][m] = 0
            m += 1
            if M < m:
                if n == N:
                    break
                n += 1
                m = 1
        print(Table[N][M])
    else:
        print(M)
