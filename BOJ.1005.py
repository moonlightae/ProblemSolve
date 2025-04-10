T_Quan = int(input())
for _ in range(T_Quan):
    Struc_Quan, Rule_Quan = map(int, input().split())
    Rule_list = list()
    for __ in range(Rule_Quan):
        Rule_list.append(tuple(map(int, input().split())))
    aim = int(input())

    process_list = [0 for x in range(Rule_Quan)]
    for i in range(Rule_Quan):
        if aim in Rule_list[i]:
            process_list[0] = (Rule_list[i][0])

