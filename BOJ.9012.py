repeat = int(input())

for i in range(repeat):
    alpha = input()
    str_binary = ''.join(list(map(lambda x: "0" if x == "(" else "1", list(alpha))))
    str_binary_c = str_binary
    if str_binary_c[0] == "0" and str_binary_c[-1] == "1":
        while True:
            if str_binary_c == '':
                print("YES")
                break

            # 조건: () => 01이 있으면 제거
            elif '01' in str_binary_c:
                index_01 = str_binary_c.index('01')
                str_binary_c = str_binary_c[:index_01] + str_binary_c[(index_01 + 2):]

            else:
                print("NO".format(''.join(list(map(lambda x: "(" if x == '0' else ")", list(str_binary))))))
                break
    else:
        print("NO".format(''.join(list(map(lambda x: "(" if x == '0' else ")", list(str_binary))))))