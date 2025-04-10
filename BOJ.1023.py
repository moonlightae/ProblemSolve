N, K = map(int, input().split())

Quantity = 0
if N % 2 == 0:
    C_Table = [1, 2, 5, 14, 42,
               132, 429, 1430, 4862, 16796,
               58786, 208012, 742900, 2674440, 9694845,
               35357670, 129644790, 477638700, 1767263190, 6564120420,
               24466267020, 91482563640, 343059613650, 1289904147324, 4861946401452]
    Ni = (N // 2) - 1
    if len(C_Table) > Ni:
        Quantity = C_Table[Ni]
    else:
        for j in range(Ni):
            if len(C_Table) > j:
                continue
            else:
                C_Table.append(int(C_Table[-1] * 2))
                C_Table[-1] *= (2 * j + 1)
                C_Table[-1] = int(C_Table[-1] // (j+2))
        Quantity = C_Table[-1]

Quantity = (2 ** N) - Quantity
str_number = -1
if Quantity > K:
    while K >= 0:
        str_number += 1
        str_binary = bin(str_number)[2:].rjust(N, "0")
        str_binary_c = str_binary
        if str_binary_c[0] == "0" and str_binary_c[-1] == "1":
            while True:
                if str_binary_c == '':
                    go_continue = 1
                    break

                # 조건: () => 01이 있으면 제거
                elif '01' in str_binary_c:
                    index_01 = str_binary_c.index('01')
                    str_binary_c = str_binary_c[:index_01] + str_binary_c[(index_01+2):]

                else:
                    go_continue = 0
                    break
            if go_continue == 1:
                continue
            else:
                K -= 1
        else:
            K -= 1
    print(''.join(list(map(lambda x: "(" if x == '0' else ")", list(str_binary)))))

else:
    print(-1)