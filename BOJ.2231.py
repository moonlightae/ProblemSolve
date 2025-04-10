N = int(input())
asdfghjkl = 0
for i in range(N//2, N):
    if N == i + sum(list(map(int, str(i)))):
        asdfghjkl = 1
        print(i)
        break

if asdfghjkl == 0:
    print(0)