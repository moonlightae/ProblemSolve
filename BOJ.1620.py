# N, K = map(int, input().split())
# l = [''] * N
# for i in range(N):
#     l[i] = input()
#
# for i in range(K):
#     alpha = input()
#     if alpha.isdigit():
#         print(l[int(alpha)-1])
#     else:
#         print(l.index(alpha) + 1)


a = {0: '1'}
b = {'1': 0}
N, K = map(int, input().split())

for i in range(N):
    alpha = input()
    a[i + 1] = alpha
    b[alpha] = i + 1

for i in range(K):
    alpha = input()
    if alpha.isdigit():
        print(a[int(alpha)])
    else:
        print(b[alpha])
