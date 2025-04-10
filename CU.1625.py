k = int(input())
sum = 0

def summer(intext):
    alpha = 0
    if type(intext) != type(list()):
        intext = list(str(intext))
    tex = list(map(int, intext))
    tex.sort()
    for i in range(1, tex[-1]+1):
        a = tex.count(i)
        alpha += a * i
    return alpha

for x in range(0, k):
    text = list(input())
    sum = summer(text)
    while sum > 9:
        sum = summer(sum)

    print(sum)