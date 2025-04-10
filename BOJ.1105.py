L, R = map(int, input().split())

A = str(R).count('8')
minE = str(L).count('8')
minE = minE if A > minE else A
l = len(str(L))

for i in range(l):
    if str(L)[i] == '8':
        ind = i
        back = str(L)[ind+1:]
        if len(back) == 0:
            back = 0
        L += 10**(l-ind-1) - int(back)
        if L > R:
            L -= 10**(l-ind-1) - int(back)
        else:
            break

A = str(L).count('8')
minE = A if A < minE else minE
print(minE)