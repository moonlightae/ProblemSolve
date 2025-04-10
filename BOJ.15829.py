alphabet = [
    "a", "b", "c", "d", "e",
    "f", "g", "h", "i", "j",
    "k", "l", "m", "n", "o",
    "p", "q", "r", "s", "t",
    "u", "v", "w", "x", "y",
    "z"
]


def power(e):
    if e == 1:
        return 31
    elif e == 0:
        return 1
    a = power(e//2)
    if e % 2 == 0:
        return a * a
    else:
        return a * a * 31


L = int(input())
char = input()
out = 0
for i in range(L):
    out = (out + (((alphabet.index(char[i]) + 1) % 1234567891) * (power(i) % 1234567891)) % 1234567891) % 1234567891

print(out)