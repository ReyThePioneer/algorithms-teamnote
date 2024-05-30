#14681 사분면 고르기

x = int(input())
y = int(input())
qud = 0

if x>0 and y>0:
    qud = 1
elif x<0 and y>0:
    qud = 2
elif x<0 and y<0:
    qud = 3
elif x>0 and y<0:
    qud = 4

print(qud)