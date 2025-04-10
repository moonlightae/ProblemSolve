N = int(input())
A = set(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))


for i in B:
    print(int(i in A))