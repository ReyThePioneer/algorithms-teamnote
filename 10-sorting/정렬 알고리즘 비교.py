# 선택 정렬
# 평균 시간 복잡도: O(N^2), 공간 복잡도 : O(N)
# 특징 : 아이디어가 매우 간단함

# 삽입 정렬
# 평균 시간 복잡도: O(N^2), 공간 복잡도 : O(N)
# 특징 : 데이터가 거의 정렬되어 있을 때는 O(N)으로 가장 빠름

# 퀵 정렬
# 평균 시간 복잡도: O(NlogN), 공간 복잡도 : O(N)
# 대부분의 경우에 가장 적합하며, 충분히 빠름
# 최악의 경우 시간 복잡도 : O(N^2)

# 계수 정렬
# 평균 시간 복잡도: O(N + K), 공간 복잡도 : O(N + K)
# 특징 : 데이터의 크기가 한정되어 있는 경우에만 사용이 가능하지만 매우 빠르게 동작함

# +) 대부분의 프로그래밍 언어에서 지원하는 표준 정렬 라이브러리는
# 최악의 경우에도 O(NlogN)을 보장하도록 설계되어 있음

# 선택 정렬과 기본 정렬 라이브러리 수행 시간 비교
from random import randint
import time

# 배열에 10,000개의 정수를 삽입
array = []
for _ in range(10000):
  # 1부터 100 사이의 랜덤한 정수
  array.append(randint(1, 100))

# 선택 정렬 프로그램 성능 측정
start_time = time.time()

# 선택 정렬 프로그램 소스코드
for i in range(len(array)):
  min_index = i # 가장 작은 원소의 인덱스
  for j in range(i + 1, len(array)):
    if array[min_index] > array[j]:
      min_index = j
  array[i], array[min_index] = array[min_index], array[i]

# 측정 종료
end_time = time.time()

# 수행 시간 출력
print("선택 정렬 성능 측정:", end_time - start_time)

# 배열을 다시 무작위 데이터로 초기화
array = []
for _ in range(10000):
  # 1부터 100 사이의 랜덤한 정수
  array.append(randint(1, 100))

# 기본 정렬 라이브러리 성능 측정
start_time = time.time()

# 기본 정렬 라이브러리 사용
array.sort()

# 측정 종료
end_time = time.time()

# 수행 시간 출력
print("기본 정렬 라이브러리 성능 측정:", end_time - start_time)