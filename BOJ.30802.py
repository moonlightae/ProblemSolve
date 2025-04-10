N = int(input())
nn = list(map(int, input().split()))
T, P = map(int, input().split())
sum = 0

for i in nn:
    sum += (i // T) + (1 if i % T != 0 else 0)

p_t = N // P
p_p = N % P

print(sum)
print(p_t, p_p)