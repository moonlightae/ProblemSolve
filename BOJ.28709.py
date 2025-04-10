T = int(input())
for _ in range(T):
    alpha = input()
    while True:
        if alpha.find('()') != -1:
            alpha = alpha[:alpha.find('()')] + alpha[alpha.find('()') + 2:]
        else:
            break

    while True:
        if alpha.find('(') != -1:
            if alpha[alpha.find('('):].find(')') != -1:
                alpha = alpha[:alpha.find('(')] + alpha[alpha.find('(') + 1: (alpha.find('(') + alpha[alpha.find('('):].find(')'))] + alpha[alpha.find('(') + alpha[alpha.find('('):].find(')') + 1:]
            else:
                break
        else:
            break
    while True:
        if alpha.find('((') != -1:
            alpha = alpha[:alpha.find('((')] + '(' + alpha[alpha.find('((') + 2:]
        else:
            break
    while True:
        if alpha.find('))') != -1:
            alpha = alpha[:alpha.find('))')] + ')' + alpha[alpha.find('))') + 2:]
        else:
            break
    while True:
        if alpha.find('(*') != -1:
            alpha = alpha[:alpha.find('(*')] + '*' + alpha[alpha.find('(*') + 2:]
        elif alpha.find('*)') != -1:
            alpha = alpha[:alpha.find('*)')] + '*' + alpha[alpha.find('*)') + 2:]
        elif alpha.find('(?') != -1:
            alpha = alpha[:alpha.find('(?')] + alpha[alpha.find('(?') + 2:]
        elif alpha.find('?)') != -1:
            alpha = alpha[:alpha.find('?)')] + alpha[alpha.find('?)') + 2:]
        else:
            break

    if alpha.find(')') * alpha.find('(') == 1:
        if alpha.find('*') == -1:
            print('NO')
        print("YES")
    else:
        print("NO")