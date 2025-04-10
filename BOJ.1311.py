# input and define
N = int(input())
price_list = list()  # 이용 비용 리스트
sum_list = list()  # 이용 비용의 합 리스트
result = 0  #결괏값
for i in range(N):
    alpha_list = list(map(int, input().split()))
    price_list.append(alpha_list)
    sum_list.append(sum(alpha_list))
# 전체 과정을 N번 반복해야 하므로 for문
for i in range(N):
    # step 1. sum_list에서 가장 작은 값 찾기
    sum_list_c = sum_list.copy()
    sum_list_c.sort()
    sum_list_c.reverse()
    minima_sum_index = sum_list.index(sum_list_c[0])
    minima_sum_list = price_list[minima_sum_index].copy()

    # step 2. minima_sum_list에서 가장 작은 값을 리절트에 더함
    minima_sum_list_c = minima_sum_list.copy()
    minima_sum_list_c.sort()
    result += minima_sum_list_c[0]

    # step 3. 가로세로를 10000으로 바꾸고, sum_list에서 이 리스트를 50000으로 바꿈
    # 세로 바꾸기
    # minima_sum_list[0]의 위치를 찾아서 그 줄을 쭉 바꿈
    indexdex = minima_sum_list.index(minima_sum_list_c[0])
    for j in range(N):
        price_list[j][indexdex] = 10000
    # 가로 바꾸기
    price_list[sum_list.index(sum_list_c[0])] = [-1 for _ in range(N)]
    # sum_list 값 수정하기
    sum_list[minima_sum_index] = -1
print(result)
"""
어떻게 할거냐?
이차원 리스트에서 가장 합이 큰 리스트부터 => sum_list에서 가장 작은 값을 찾음
차례로 각 리스트 안에서 가장 작은 값을 리절트에 추가하고
가로세로를 10000으로 바꿈, sum_list 값도 수정
Example:
5
1 2 3 4 5
2 4 6 8 10
3 6 9 12 15
4 8 12 16 20
5 10 15 20 25

원래의 그리디 알고리즘: 1 + 4 + 9 + 16 + 25 = 55
New 알고리즘: 5 + 8 + 9 + 8 + 5 = 35
"""