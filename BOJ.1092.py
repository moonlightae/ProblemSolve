N = int(input())
ship = list(map(int, input().split()))
M = int(input())
box = list(map(int, input().split()))

ship.sort(reverse=True)
box.sort(reverse=True)
print(ship)
sship = list(set(ship))

