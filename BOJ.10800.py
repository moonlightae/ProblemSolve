import sys as s

N = int(s.stdin.readline())
ball_list = list()
for i in range(N):
    ball_list.append(tuple(map(int, s.stdin.readline().split())))

ball_list_c = ball_list.copy()
point_list = [0 for i in range(N)]
for i in range(N):
    main_ball = ball_list[i]
    ball_list_c.pop(0)

    for j in range(len(ball_list_c)):
        if main_ball[0] != ball_list_c[j][0]:
            if main_ball[1] > ball_list_c[j][1]:
                point_list[i] += ball_list_c[j][1]
            elif main_ball[1] != ball_list_c[j][1]:
                point_list[i + j + 1] += main_ball[1]
for x in range(len(point_list)):
    s.stdout.write(str(point_list[x]) + '\n')