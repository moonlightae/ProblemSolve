N, M = map(int, input().split())  #N이 정점의 개수, M이 간선의 개수이다.
LL = []
for i in range(M):
    S, E, L = map(int, input().split())
    LL.append([S, E, L])

LL.sort(key=lambda x: x[2])
point_list = [0] * N
MST_point = 0

R = []

XL = []

for i in range(M):
    main = LL[i]
    print(point_list, MST_point)
    if i == 0:
        point_list[main[0]-1] += 1
        point_list[main[1]-1] += 1
        MST_point += main[2]
        R.append(main)
        XL.append({main[0], main[1]})

    else:
        imfine = 0
        omg = -1
        for j in range(len(XL)):
            if main[0] not in XL[j] and main[1] not in XL[j]:
                imfine += 1
            elif main[0] in XL[j] and main[1] not in XL[j]:
                omg = j
                alpha = 0
                break
            elif main[1] in XL[j] and main[0] not in XL[j]:
                omg = j
                alpha = 1
                break
        if imfine == len(XL):
            XL.append({main[0], main[1]})
            point_list[main[0]-1] += 1
            point_list[main[1]-1] += 1
            MST_point += main[2]
            R.append(main)
        elif omg != -1:
            XL[omg].add(main[alpha])
            point_list[main[0]-1] += 1
            point_list[main[1]-1] += 1
            MST_point += main[2]
            R.append(main)

        for j in XL:
            XXL = XL.copy()
            XXL.remove(j)
            for k in XXL:
                if len(j & k) > 0:
                    XL.remove(j)
                    XL.remove(k)
                    XL.append(j + k)
                    break



    if point_list.count(0) == 0:
        break


print(LL)
#print(MST_point)
print(R)