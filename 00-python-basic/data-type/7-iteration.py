# < 반복문 >
# 특정 소스코드를 반복적으로 실행할 때
# while문, for문

# 1부터 9까지 모든 정수의 합 구하기 (while문)
i = 1
result = 0

while i <= 9: # 참일 때 실행
  result += i
  i += 1

print(result)

# 1부터 9까지 홀수의 합 구하기 (while문)
i = 1
result = 0

while i <= 9:
  if i % 2 == 1:
    result += i
  i += 1

print(result)

# 반복문에서의 무한 루프(Infinite Loop) 조심
# 코딩 테스트에서 무한 루프를 구현할 일은 거의 없으니 유의
# 반복문 작성 뒤에는 항상 반복문을 탈출할 수 있는지 여부 확인하기
x = 10
while x > 5:
  break;
  print(x)

# for문
# for 변수 in 데이터(리스트, 튜플 등):
# 데이터에 포함되어 있는 원소를 차례대로 하나씩 방문
array = [9, 8, 7, 6, 5]
# array = (1, 2, 3, 4, 5)

for x in array:
  print(x)

# range(): for문에서 연속적인 값을 차례대로 순회할 때
# range(시작 값, 끝 값 + 1)
# 인자를 하나만 넣으면 시작 값은 default = 0
result = 0

for i in range(1, 10):
  result += i

print(result)

# 1부터 30까지 모든 정수의 합 구하기 (for문)
result = 0

for i in range(1, 31):
  result += i

print(result)

# 파이썬의 continue 키워드
# 반복문에서 남은 코드의 실행을 건너뛰고, 다음 반복을 진행하고자 할 때

# 1부터 9까지의 홀수 합 구하기
result = 0

for i in range(1, 10):
  if i % 2 == 0: # 짝수일 때
    continue # 건너뛴다
  result += i

print(result)

# 파이썬의 break 키워드
# 반복문을 즉시 탈출하고자 할 때

# 1부터 5까지의 정수를 차례대로 출력하기
i = 1

while True: # 무조건 실행
  print("현재 i의 값: ", i)
  if i == 5: # i가 5에 도달했을 때
    break
  i += 1

# 학생들의 합격 여부 판단 예제 (1): 점수가 80점만 넘으면 합격
scores = [90, 85, 77, 65, 97]

for i in range(5):
  if scores[i] >= 80:
    print(i + 1, "번 학생은 합격입니다.")

# 학생들의 합격 여부 판단 예제 (2): 특정 번호의 학생은 제외하기
scores = [90, 85, 77, 65, 97]
cheating_student_list = {2, 4}

for i in range(5):
  if i + 1 in cheating_student_list:
    continue # 제외해버림
  if scores[i] >= 80:
    print(i + 1, "번 학생은 합격입니다.")

# 중첩된 반복문: 구구단 예제
for i in range(2, 10): # 2~9단
  for j in range(1, 10): # 곱하기 1~9
    print(i, "X", j, "=", i * j)
  print() # 한 단이 끝날 때마다 줄바꿈