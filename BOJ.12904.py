S = input()
T = input()

for i in range(len(T)-len(S)):
    if T[-1] == "A":
        T = T[0:-1]
    else:
        T = T[0:-1][::-1]

if T == S:
    print(1)
else:
    print(0)
