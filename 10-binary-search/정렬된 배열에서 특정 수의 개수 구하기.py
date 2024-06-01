# <문제> 정렬된 배열에서 특정 수의 개수 구하기
# 단, 시간 복잡도 O(log N)으로 알고리즘을 설계하지 않으면 시간 초과 판정을 받음

# 일반적인 선형 탐색(linear search)로는 시간 초과 판정을 받음
# 데이터가 정렬되어 있기 때문에 이진 탐색을 수행할 수 있음

# 특정 값이 등장하는 첫 번째 위치와 마지막 위치를 찾아서 위치 차이를 계산하여 문제를 해결할 수 있음

from bisect import bisect_left, bisect_right

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

n, x = map(int, input().split())
array = list(map(int, input().split()))

# 값이 [x, x] 범위에 있는 데이터의 개수 계산
count = count_by_range(array, x, x)

# 값이 x인 원소가 존재하지 않는다면
if count == 0:
    print(-1)
# 값이 x인 원소가 존재한다면
else:
    print(count)