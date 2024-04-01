a, b = map(int, input().split(' '))
a = bool(a) # bool()은 map()에 사용 불가?
b = bool(b)

if ((a and not b) or (not a and b)): print(True)
else: print(False)