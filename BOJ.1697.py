# # DFS
# N, M = map(int, input().split())
# s = [(N, 0)]
# v = [False] * (M * 2)
# m = M - N + 1
# v[N] = True
# while len(s) > 0:
#     x, d = s.pop()
#     if d < m:
#         if x == M:
#             m = d
#         elif x < M:
#             if 0 < x-1 < M * 2 and v[x-1] == False:
#                 v[x-1] =True
#                 s.append((x-1, d+1))
#             if 0 <= x+1 < M * 2 and v[x+1] == False:
#                 v[x+1] =True
#                 s.append((x+1, d+1))
#             if 0 < 2*x < M * 2 and v[2*x] == False:
#                 v[2*x] = True
#                 s.append((x*2, d+1))
#         else:
#             if 0 < x-1 < M * 2 and v[x-1] == False:
#                 v[x-1] =True
#                 s.append((x-1, d+1))
#     else:
#         continue
# print(m)

# BFS
from collections import deque
N, M = map(int, input().split())
m = M - N + 1
if N >= M:
    print(N-M)
else:
    s = deque([(N, 0)])
    v = [(False, m) for _ in range(M * 2)]
    v[N] = (True, 0)
    while len(s) > 0:
        x, d = s.popleft()
        if d < m:
            if x == M:
                m = d
            elif x < M:
                if 0 <= x-1 < M * 2 and (v[x-1][0] == False or v[x-1][1] > d):
                    v[x-1] = (True, d)
                    s.append((x-1, d+1))
                if 0 <= x+1 < M * 2 and (v[x+1][0] == False or v[x+1][1] > d):
                    v[x+1] = (True, d)
                    s.append((x+1, d+1))
                if 0 <= 2*x < M * 2 and (v[2*x][0] == False or v[2*x][1] > d):
                    v[2*x] = (True, d)
                    s.append((x*2, d+1))
            else:
                if 0 <= x-1 < M * 2 and (v[x-1][0] == False or v[x-1][1] > d):
                    v[x-1] = (True, d)
                    s.append((x-1, d+1))
        else:
            continue
    print(m)