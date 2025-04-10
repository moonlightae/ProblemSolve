N = int(input())
fibo = [1, 1]

for i in range(2, N):
    fibo.append(fibo[i-1] + fibo[i-2])

print(fibo[N-1])
print(1000000000000000000)