def f(a, n):
    global F
    if a == 1 or n <= 1:  # 목표 정점이 1이나 0인 경우에는 항상 공백을 반환하도록 처리했다.
        return ''
    z = F[n-2] + 1
    if z < a:
        return 'R' + f(a - 1 - F[n-2], n-1)
    else:
        return 'L' + f(a - 1, n-2)

N, S, E = map(int, input().split())  # 각각 피이보나치 트리의 크기, 시작 정점, 끝 정점이다.
if N > 1:  # if문의 위치를 이동했다.
    F = [0] * (N+1)  # 피보나치 수열을 저장해두는 리스트
    F[0] = 1
    F[1] = 1
    for i in range(2, N+1):  # 피보나치 수열을 구하는 부분
        F[i] = F[i-1] + F[i-2] + 1

    e = f(E, N)  # 피이보나치 트리의 루트에서 E까지 가는 경로를 구한다.
    s = f(S, N)  # 피이보나치 트리의 루트에서 S까지 가는 경로를 구한다.

    while True:
        if len(s) == 0:  # s의 길이가 0인 경우(즉, S가 루트)에는 e를 그대로 출력한다.
            print(e)
            break
        elif len(e) == 0:  # e의 길이가 0인 경우(즉, E가 루트)에는 루트에서 S로 이동하는 경로에서 이동한 횟수만큼 U를 출력하면 된다.
            print('U' * len(s))
            break
        elif s[0] != e[0]:  # s와 e의 길이가 모두 0이 아니면서 겹치는 경로가 더 이상 없는 경우에는 s에만 존재하는 경로만큼 U로 이동한 후에 e로 이동한다.
            print('U' * len(s) + e)
            break
        else:  # s와 e의 길이가 모두 0이 아니고, 겹치는 경로가 존재하면, 가장 첫번째 이동을 삭제한다.
            # 이를 반복하면 반드시 s와 e 사이에 겹치는 경로가 존재하지 않거나 s, e의 길이가 0이 되는 순간이 발생한다.
            s = s[1:]
            e = e[1:]
else:
    print()
