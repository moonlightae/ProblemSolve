A, B = map(int, input().split())
DP = [0] * (B + 1)

for i in range(2, B//2 + 1):
    if DP[i] == 0:
        pointer = 2 * i
        while pointer <= B:
            DP[pointer] += 1
            # 같은 소인수가 여러번 포함되는 경우의 확인
            sj = pointer
            while (sj // i) % i == 0:
                DP[pointer] += 1
                sj //= i
            pointer += i

# underprime 판별
s = 0
for i in range(B+1):
    if DP[i] != 0 and DP[DP[i]] == 0 and i >= A:
        s += 1

print(s)