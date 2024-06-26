# Quick Sort - Pythonic Code
# list slicing, list comprehension

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
  # 리스트가 하나 이하의 원소만을 담고 있다면 종료
  if len(array) <= 1:
    return array
  
  pivot = array[0] # 첫 번째 원소를 pivot으로
  tail = array[1:] # pivot을 제외한 리스트를 tail로

  # pivot보다 작은 경우 왼쪽 리스트에 담기
  left_side = [x for x in tail if x <= pivot]
  # pivot보다 큰 경우 오른쪽 리스트에 담기
  right_side = [x for x in tail if x > pivot]

  # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고 전체 리스트 반환
  return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))