L = []
num_ind = []
for i in range(3):
    R = input()
    if R.isdecimal():
        R = int(R)
        num_ind.append(i)

    L.append(R)

if num_ind[-1] == 2:
    out_int = L[-1] + 1
elif num_ind[-1] == 1:
    out_int = L[-2] + 2
elif num_ind[-1] == 0:
    out_int = L[-3] + 3

if out_int % 15 == 0:
    print('FizzBuzz')
elif out_int % 3 == 0:
    print('Fizz')
elif out_int % 5 == 0:
    print('Buzz')
else:
    print(out_int)