"""
10의 9승부터 시작해서 하강하면서 999...로 쪼개서 모든 수를 같은 개수로 늘리는 방식으로 가면 될 듯
"""


N = int(input())
Quan = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
while N > 0:
    if N >= 10:
        ten_quan = int(str(N)[-1]) + 1
        ten_item = int(str(N)[-2])
        N -= 10
        Quan[ten_item] += ten_quan
        for i in range(10):
            Quan[i] += 1
    else:
        alpha = int(str(N)[-1])
        N -= 1
        Quan[alpha] += 1

print(Quan)



"""
79
78 77 76 75 74 73 72 71 70 69

"""