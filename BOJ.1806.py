N, S = map(int, input().split())
L = list(map(int, input().split()))
if sum(L) < S:
    print(0)
else:
    if sum(L) - S > S:
