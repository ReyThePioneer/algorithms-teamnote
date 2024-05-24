# 1. 탐색(Search)
  # 많은 양의 데이터 중 원하는 데이터를 찾는 과정
  # 대표적인 그래프 탐색 알고리즘 : DFS, BFS
  # 코딩 테스트에서 매우 자주 등장! 반드시 숙지!

# 2. 스택 자료구조
  # 먼저 들어온 데이터가 나중에 나가는 형식(선입후출)
  # 입구와 출구가 동일한 형태(프링글스 과자 통처럼)
  # 삽입, 삭제 연산

stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack) # 최하단 원소부터 출력
print(stack[::-1]) # 최상단 원소부터 출력

# 3. 큐 자료구조
  # 먼저 들어온 데이터가 먼저 나가는 형식(선입선출)
  # 입구와 출구가 모두 뚫려있는 터널과 같은 형태
  # 삽입, 삭제 연산

# 큐 구현을 위해 deque 라이브러리 사용
from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 먼저 들어온 순서대로 출력
queue.reverse() # 역순으로 바꾸기
print(queue) # 나중에 들어온 원소부터 출력

# 4. 재귀 함수(Recursive Function)
  # 자기 자신을 다시 호출하는 함수
  # 어느정도 출력하다가 최대 재귀 깊이 초과 메시지가 출력되고 프로그램이 종료됨

def recursive_function():
  print('재귀 함수를 호출합니다.')
  recursive_function()

recursive_function()
