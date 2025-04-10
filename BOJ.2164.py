N = int(input())
L = list(range(1, N+1))
while len(L) > 1:
    il = []
    for i in range(len(L)//2):
        il.append(L[2*i+1])
    if len(L) % 2 == 1:
        il.append(il.pop(0))
    L = il
print(L[0])