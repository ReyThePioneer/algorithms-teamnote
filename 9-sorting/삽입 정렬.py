# 삽입 정렬(Insertion Sort)
# 처리되지 않은 데이터를 하나씩 골라 '적절한 위치에 삽입'
# 선택 정렬에 비해 구현 난이도가 높지만 일반적으로 더 효율적으로 동작함

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)): # 두 번째 원소부터
  for j in range(i, 0, -1): # 인덱스 i부터 1까지 1씩 감소
    if array[j] < array[j - 1]: # 자신이 왼쪽 원소보다 작다면
      array[j], array[j - 1] = array[j - 1], array[j]
    else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
      break

print(array)