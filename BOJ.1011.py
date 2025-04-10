import math as m
N = int(input())
for i in range(N):
    x, y = map(int, input().split())
    d = y - x
    k = 1

    # 짝수인 경우
    if d % 2 == 0:
        d_i = 2
        count = 2
        while True:
            if d_i == d:
                break
            else:
                d_i += 2
                j = 1
                while True:
                    j += 1
                    if count - 1 <= 4 * j:
                        count += 1 / j
                        break
    print(count)
