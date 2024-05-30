#1330 두 수 비교하기

a, b = map(int, input().split())
result = ''

if a > b:
    result = '>'
elif a < b:
    result = '<'
elif a == b:
    result = '=='

print(result)