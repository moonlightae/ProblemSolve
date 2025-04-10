N = int(input())
i = 665
r = 0
while True:
    i += 1
    if str(i).find('666') != -1:
        r += 1
    if r >= N:
        print(i)
        break