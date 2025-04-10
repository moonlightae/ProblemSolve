N = int(input())
for i in range(N-1):
    print(" " * (N-i-1), end='')
    print("*")

print("*"*N)
for i in range(N-1):
    print(" " * (N-i-2), end='')
    print("*")

