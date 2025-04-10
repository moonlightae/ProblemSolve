n = int(input())

n = n if n % 2 == 0 else n + 1
print(pow(2, n//2, 16769023))