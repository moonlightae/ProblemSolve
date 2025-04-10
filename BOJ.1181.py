def merge_sort(l):
    if len(l) == 1:
        return l
    elif len(l) == 0:
        return []
    else:
        mid = len(l) // 2
        l1 = merge_sort(l[:mid])
        l2 = merge_sort(l[mid:])
        out = []
        while len(l1) + len(l2) > 0:
            if len(l1) == 0:
                out += l2
                break
            elif len(l2) == 0:
                out += l1
                break
            else:
                if len(l1[0]) < len(l2[0]):
                    out.append(l1.pop(0))
                elif len(l2[0]) < len(l1[0]):
                    out.append(l2.pop(0))
                else:
                    if l1[0] == l2[0]:
                        out.append(l1.pop(0))
                    else:
                        for _ in range(len(l1[0]) + len(l2[0])):
                            if ord(l1[0][_]) < ord(l2[0][_]):
                                out.append(l1.pop(0))
                                break
                            elif ord(l1[0][_]) > ord(l2[0][_]):
                                out.append(l2.pop(0))
                                break
        return out


n = int(input())
alpha = list()
for i in range(n):
    alpha.append(input())
alpha = list(set(alpha))
for i in merge_sort(alpha):
    print(i)