# 퀵 정렬(Quick Sort)
# 기준 데이터를 설정하고, 그 '기준보다 큰 데이터와 작은 데이터의 위치를 서로 바꾸는 방법'
# 일반적인 상황에서 가장 많이 사용되는 정렬 알고리즘 중 하나
# 병합 정렬과 더불어 대부분의 프로그래밍 언어의 정렬 라이브러리의 근간이 되는 알고리즘
# 가장 기본적인 퀵 정렬은 '첫 번째 데이터를 기준 데이터(pivot)로 설정'함

# 위치가 엇갈리는 경우 'pivot'과 '작은 데이터'의 위치를 서로 변경
# pivot을 기준으로 데이터 묶음을 나누는 작업 : 분할(divide, partition)
# 왼쪽 데이터 묶음 정렬, 오른쪽 데이터 묶음 정렬

# 퀵 정렬의 시간 복잡도
# 평균의 경우 : O(NlogN)
# 최악의 경우 : O(N^2)
# 첫 번째 원소를 pivot으로 삼을 때, 이미 정렬된 배열에 대해 퀵 정렬을 수행하면? 오른쪽 부분만 남는 형태로 분할이 이루어짐

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
  if start >= end: # 원소가 1개인 경우 종료
    return

  pivot = start # 첫 번째 원소를 pivot
  left = start + 1 # 가장 왼쪽 원소를 left
  right = end # 가장 오른쪽 원소를 right

  while (left <= right): # 엇갈릴 때까지 반복
    # pivot보다 큰 데이터를 찾을 때까지 반복
    while (left <= end and array[left] <= array[pivot]):
      left += 1 # 오른쪽으로 
    # pivot보다 작은 데이터를 찾을 때까지 반복
    while (right > start and array[right] >= array[pivot]):
      right -= 1 # 왼쪽으로
    
    # 위치가 엇갈렸다면 작은 데이터와 피벗을 교체
    if (left > right):
      array[right], array[pivot] = array[pivot], array[right]
    # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
    else:
      array[left], array[right] = array[right], array[left]
  
  # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 다시 정렬 수행(재귀적으로)
  quick_sort(array, start, right - 1)
  quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)

