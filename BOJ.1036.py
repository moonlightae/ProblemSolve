N = int(input())
symbols = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def sszin(a):
    if a < 36:
        return symbols[a]
    else:
        return str(str(sszin(a//36)) + str(sszin(a%36)))


num = [0] * 36
num_in = [''] * 36
num_size = [0] * 36
for i in range(N):
    alpha = input()
    for j in range(len(alpha)):
        num[symbols.find(alpha[j])] += 1
        num_in[symbols.find(alpha[j])] += str((len(alpha)-j-1)).rjust(2, '0')
        num_size[symbols.find(alpha[j])] += symbols.find(alpha[j]) * (36 ** (len(alpha)-j-1))
print(num_size)
sorted_valin = num_size.copy()
sorted_valin.sort()
zero = sorted_valin.count(0)
for i in range(zero):
    sorted_valin.remove(0)

S = sum(num_size)
K = int(input())
for i in range(K):
    main = sorted_valin.pop(0)
    S -= main
    for j in range(num[num_size.index(main)]):
        S += 35 * 36 ** (int(num_in[num_size.index(main)][0:2]))
        print(35 * (36 ** (int(num_in[num_size.index(main)][0:2])))-main)
        num_in[num_size.index(main)] = num_in[num_size.index(main)][2:]
#num_in 인덱스 제대로 다시 넣기
print(sszin(S), S)