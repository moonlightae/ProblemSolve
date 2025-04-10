N = int(input())
s = [0]
out = []
out.append('+')
r = 1
s.append(r)
no = 0
for i in range(N):
    aim = int(input())
    while aim > s[-1]:
        out.append('+')
        r += 1
        s.append(r)
    if aim == s.pop(-1):
        out.append('-')
    else:
        no = 1
        print("NO")
        break

if no == 0:
    for i in range(len(out)):
        print(out[i])