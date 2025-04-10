while True:
    alpha = input()
    if alpha == '.':
        break
    str_binary = ''.join(list(map(lambda x: "0" if x == "(" else ("1" if x == ")" else ("2" if x == "[" else "3" if x == "]" else '')), list(alpha))))
    str_binary_c = str_binary
    if str_binary_c == '' or (str_binary_c[0] == "0" and str_binary_c[-1] == "1") or (str_binary_c[0] == "2" and str_binary_c[-1] == "3") or (str_binary_c[0] == "0" and str_binary_c[-1] == "3") or (str_binary_c[0] == "2" and str_binary_c[-1] == "1"):
        while True:
            if str_binary_c == '':
                print("yes")
                break

            # 조건: () => 01이 있으면 제거
            elif '01' in str_binary_c:
                index_01 = str_binary_c.index('01')
                str_binary_c = str_binary_c[:index_01] + str_binary_c[(index_01 + 2):]

            elif '23' in str_binary_c:
                index_01 = str_binary_c.index('23')
                str_binary_c = str_binary_c[:index_01] + str_binary_c[(index_01 + 2):]

            else:
                print("no")
                break
    else:
        print("no")