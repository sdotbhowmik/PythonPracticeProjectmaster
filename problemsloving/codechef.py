import math

for _ in range(int(input())):
    x, y, r = map(int,input().split())
    extra_sticks = r/30
    total_sticks = x + extra_sticks
    plates = total_sticks / y
    print(math.ceil(plates))