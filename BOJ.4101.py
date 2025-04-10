while True:
    A, B = map(int, input().split())
    if A + B != 0:
        print("Yes" if A > B else "No")
    else:
        break