T = int(input())
l = []
for i in range(T):
    main = int(input())
    if main != 0:
        l.append(main)
    else:
        l.pop(-1)

print(sum(l))
