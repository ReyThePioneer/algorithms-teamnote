# 정렬(Sorting)
# 데이터를 특정한 기준에 따라 순서대로 나열하는 것
# 문제 상황에 따라서 적절한 정렬 알고리즘이 공식처럼 사용됨

# 선택 정렬(Selection Sort)
# 처리되지 않은 데이터 중 (탐색 범위는 매번 하나씩 줄어들게 됨)
# 가장 '작은' 데이터를 '선택'해서
# 맨 앞에 있는 데이터와 바꾸는 것을 반복

# 선택 정렬의 시간 복잡도
# N번만큼 매번 작은 수를 찾아서 맨 앞으로 보내야 함
# N + (N-1) + (N-2) + ... + 2 = (N^2 + N - 2) / 2
# O(N^2)

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
  min_index = i # 매번 가장 앞쪽 원소의 인덱스

  for j in range(i + 1, len(array)):
    # 현재 가장 작은 원소보다 더 작은 것이 있다면
    if array[min_index] > array[j]:
      min_index = j
    # 가장 앞쪽 원소와 가장 작은 원소 swap
    array[i], array[min_index] = array[min_index], array[i]

print(array)