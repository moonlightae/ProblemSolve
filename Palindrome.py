output = ""
text = list(input())
Large = []
for x in range(0, len(text)):
    if ord(text[x]) < 91:
        text[x] = chr(ord(text[x])+32)
        Large.append(1)
    else:
        Large.append(0)
for x in range(0, int(len(text)/2)):
    if text[x] != text[-(x+1)]:
        output = "No"
for x in range(0, len(text)):
    if Large[x] == 1:
        text[x] =chr(ord(text[x])-32)
if output != "No":
    print("Yes")
    print(''.join(text[0:round(len(text)/2+0.1)]))
else:
    print(output)
    print(''.join(text)+''.join(list(text[::-1])))