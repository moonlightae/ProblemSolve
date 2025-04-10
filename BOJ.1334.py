# 1. 중간을 자른다. (짝수는 둘다 지우면 됨)
# 2. 왼쪽을 뒤집어서 오른쪽과 비교한다. (방향 중요)
#    Case 1. 왼쪽이 크면 오른쪽을 왼쪽과 같게 하면 팰린드롬이다.
#    Case 2. 오른쪽이 크면 가운데를 +1하고 왼쪽과 같게 하면 팰린드롬이다.
# 여기서 문제: 중간이 9인데 Case 2이면?
# -> 가운데에서 한개 앞쪽 인덱스를 +1, 가운데를 0으로 바꾸고 다시 Case 1을 실행함.
# -> 그런데 가운데부터 앞쪽이 다 9면?
#       -> 그냥 모든 9의 앞을 +1하고 그뒤를 다 0으로 바꿈. 그리고 Case 1하면 끝.
#           -> 9변환을 먼저하고 자르고 비교하면 되겠네
# 1자리일 때와 2자리일 때도 확인 필요.

N = str(int(input()))
L = len(str(N))

if L == 1:
    if N != '9':
        print(int(N) + 1)
    else:
        print(11)
elif L == 2:
    if 99 > int(N):
        if int(N[0]) > int(N[1]):
            print(N[0] + N[0])
        else:
            print(str(int(N[0]) + 1) * 2)
    else:
        print(101)

else:
    if L % 2 == 1:
        mid = N[L//2]
        l = N[:L//2]
        r = N[L//2+1:]
    else:
        mid = N[L//2 - 1] + N[L//2]
        l = N[:L//2 - 1]
        r = N[L//2 + 1:]

    reverse_l = l[::-1]
    if reverse_l > r:
        if len(mid) == 1:
            print(l + mid + reverse_l)
        else:
            maxmid = mid[0] if int(mid[0]) > int(mid[1]) else mid[1]
            if maxmid == mid[0]:
                print(l + maxmid * 2 + reverse_l)
            else:
                print(l + str(int(mid[0]) + 1) * 2 + reverse_l)

    else:
        if mid != '9' and 99 > int(mid):
            if len(mid) == 1:
                print(l + str(int(mid) + 1) + reverse_l)
            else:
                maxmid = mid[0] if int(mid[0]) > int(mid[1]) else str(int(mid[0]) + 1)
                print(l + maxmid * 2 + reverse_l)
        else:
            count_nine = 0
            complement_nine = 0
            while l[-1] == '9':
                count_nine += 1
                l = l[:-1]
                if len(l) == 0:
                    complement_nine = 1
                    break
            if complement_nine == 0:
                l = str(int(l) + 1) + '0' * count_nine
                if mid == '9':
                    print(l + '0' + l[::-1])
                else:
                    print(l + '00' + l[::-1])
            else:
                if mid == '9':
                    print('1' + '0' * (2 * count_nine) + '1')
                else:
                    print('1' + '0' * (2 * count_nine + 1) + '1')