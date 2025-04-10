P = [True] * 1000001
P[0] = False
P[1] = False
i = 2
while i < 1002:
    if P[i]:
        j = i ** 2
        while j < 1000001:
            P[j] = False
            j += i
    i += 1

while True:
    N = int(input())
    if N == 0:
        break
    else:
        for i in range(2, N//2 + 1):
            if P[i] and P[N-i]:
                print(f"{N} = {i} + {N-i}")
                break