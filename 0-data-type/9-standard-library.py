# < 실전에서 자주 사용하는 유용한 표준 라이브러리 >

# 내장 함수
  # 기본적인 함수들 제공 (기본 입출력, 정렬 함수 등)
  # import 구문 없이 사용 가능
  # 파이썬 프로그램 작성 시 없어서는 안 되는 필수적인 기능 포함

# itertools
  # 파이썬에서 반복되는 형태의 데이터를 처리하기 위한 유용한 기능 제공
  # 순열, 조합 라이브러리: 모든 경우의 수를 고려해야 하는 경우, 완전 탐색

# heapq
  # Heap 자료구조 제공
  # 일반적으로 우선순위 큐 기능 구현 위해 사용 (다익스트라, 최단 경로)

# bisect
  # 이진 탐색(Binary Search) 기능 제공

# collections
  # deque, Counter 등의 유용한 자료구조 포함

# math
  # 필수적인 수학적 기능 제공
  # 팩토리얼, 제곱근, 최대공약수(GCD), 삼각함수 관련 함수, 파이(pi) 같은 상수 포함

# sum()
result = sum([1, 2, 3, 4, 5])
print(result)

# min(), max()
min_result = min(7, 3, 5, 2)
max_result = max(7, 3, 5, 2)
print(min_result, max_result)

# eval()
result = eval("(3+5)*7")
print(result)

# sorted()
result = sorted([9, 1, 8, 5, 4]) # 오름차순
reverse_result = sorted([9, 1, 8, 5, 4], reverse=True) # 내림차순
print(result)
print(reverse_result)

# sorted() with key
array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]
result = sorted(array, key=lambda x: x[1], reverse=True)
print(result)

# 순열과 조합: 모든 경우의 수를 고려해야 할 때 -> itertools 라이브러리 사용

# 순열 nPr : 서로 다른 n개에서 서로 다른 r개를 선택하여 일렬로 나열
# ABC 중 3개 선택해서 나열 (ABC, ACB, BCA, CAB, CBA)
from itertools import permutations

data = ['A', 'B', 'C']

result = list(permutations(data, 3))
print(result)

# 조합 nCr : 서로 다른 n개에서 순서에 상관 없이 서로 다른 r개를 선택
# ABC 중 순서를 고려하지 않고 2개 뽑기 (AB, AC, BC)
from itertools import combinations

data = ['A', 'B', 'C']

result = list(combinations(data, 2))
print(result)

# 중복을 허용하는 순열
from itertools import product

data = ['A', 'B', 'C']

result = list(product(data, repeat=2))
print(result)

# 중복을 허용하는 조합
from itertools import combinations_with_replacement

data = ['A', 'B', 'C']

result = list(combinations_with_replacement(data, 2))
print(result)

# Counter
  # 리스트와 같이 반복 가능한(iterable) 객체가 주어졌을 때
  # 내부의 원소가 며 번씩 등장했는지 세줌
from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue'])
print(counter['green'])
print(dict(counter))

# 최대 공약수, 최소 공배수
import math

def lcm(a, b):
  return a * b // math.gcd(a,b)

a = 21
b = 14

print(math.gcd(21, 14)) # 최대공약수(GCD)
print(lcm(21, 14)) # 최소공배수(LCM)