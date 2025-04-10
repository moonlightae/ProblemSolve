asdfghjkln = input()
N = list(map(int, input().split()))
eng = 0
k = 1
point = [0, len(N)]
ran = []

for i in range(1, len(N)-1):
    if (N[i-1] > N[i] and N[i] < N[i+1]) or N[i-1] == N[i] or N[i+1] == N[i]:
        point.append(i)

point.sort()
for i in range(len(point)-1):
    ran.append(N[point[i]:point[i+1]+1] if max(N[point[i]:point[i+1]+1]) != min(N[point[i]:point[i+1]+1]) else [0])

print(max(list(map(lambda x: len(x), ran))))
