#2309 일곱 난쟁이

# 9명의 난쟁이 키를 입력 받아서 리스트에 넣는다.
heights = []

for _ in range(9):
    heights.append(int(input()))

# 가짜 난쟁이 두 명을 찾아 리스트에서 제거한다.
found = False
fake_dwarf = []

for i in range(9):
    if found == True:
        break
    for j in range(9):
        if i != j and sum(heights) - (heights[i] + heights[j]) == 100:
            fake_dwarf.append(heights[i])
            fake_dwarf.append(heights[j])
            found = True
            break

heights.remove(fake_dwarf[0])
heights.remove(fake_dwarf[1])

# 리스트를 오름차순으로 정렬한다.
heights.sort()

# 정렬된 리스트의 원소를 한 줄에 하나씩 출력한다.
for height in heights:
    print(height)