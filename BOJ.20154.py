L = [3, 2, 1, 2, 3,3,3,3,1,1,3,1,3,3,1,2,2,2,1,2,1,1,2,2,2,1]
text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

t = input()
s = 0
for i in range(len(t)):
    s += L[text.index(t[i])]

print("I'm a winner!" if s%2 == 1 else "You're the winner?")