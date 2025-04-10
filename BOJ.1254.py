"""
input에 대해 input을 뒤에 0 을 채워서 길이를 두배하고, 중간 문자부터 양쪽이 팰린드롬이 될 수 있는지 확인
"""
text = input()
text_list = list(text)

while True:
    unpal = 0
    for i in range(len(text_list) // 2):
        if text_list[i] == text_list[-i-1] or text_list[i] == 0 or text_list[-i-1] == 0:
            continue
        else:
            unpal = 1
            break
    if unpal == 0:
        print(len(text_list))
        break
    else:
        text_list.append(0)
