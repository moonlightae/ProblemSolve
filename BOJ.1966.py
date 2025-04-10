    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        alpha = input()
        numlist = list(map(int, alpha.split()))
        l = ['0'] * N
        if len(list(alpha.split())) > 1:
            i = 0
            while len(list(alpha.split())) > 1:
                a, alpha = alpha.split(' ', 1)
                l[i] = a + str(i)
                i += 1
            l[-1] = alpha + str(i)
        else:
            l = list(alpha.split())
            l[0] = l[0] + '0'

        l_c = l.copy()
        c = 0
        j = 0
        while True:
            if int(l[0][0]) == max(numlist):
                c += 1
                if l[0][1:] != l_c[M][1:]:
                    l.pop(0)
                    numlist.remove(max(numlist))
                else:
                    print(c)
                    break
            else:
                l.append(l.pop(0))
