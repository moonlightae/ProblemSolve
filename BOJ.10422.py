C_Table = [1]
T = int(input())
for i in range(T):
    N = int(input())
    if N % 2 == 0:
        N = (N // 2)
        if len(C_Table) > N:
            print(C_Table[N])
            continue
        else:
            for j in range(N):
                if len(C_Table) > j:
                    continue
                else:
                    C_Table.append(int(C_Table[-1] * 2))
                    C_Table[-1] *= (2 * j + 1)
                    C_Table[-1] = int(C_Table[-1] // (j+2))
            print(C_Table[-1])
    else:
        print(0)