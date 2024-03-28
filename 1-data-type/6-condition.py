# < 조건문 >
# 프로그램의 흐름을 제어하는 문법 (로직 설정)

# 조건문 예제
x = 15

if x >= 10:
  print("x >= 10")

if x >= 0:
  print("x >= 0")

if x >= 30:
  print("x >= 30")

# 들여쓰기
# 파이썬에서는 코드의 블록(Block)을 들여쓰기(Indent)로 지정함
# 탭을 사용하자 vs 공백문자를 사용하자(표준: 4개의 공백문자)
score = 85

if score >= 70:
  print("성적이 70점 이상입니다.")
  if score >= 90:
    print("우수한 성적입니다.")
else:
  print("성적이 70점 미만입니다.")
  print("조금 더 분발하세요.")

print("프로그램을 종료합니다.")

# 조건문의 기본 형태
# if ~ elif ~ else
a = -5

if a >= 0:
  print("a >= 0")
elif a >= -10:
  print("-10 <= a <= 0")
else:
  print("a < -10")

# 성적 구간에 따른 학점 출력 예제
score = 85

if score >= 90:
  print("학점: A")
elif score >= 80:
  print("학점: B")
elif score >= 70:
  print("학점: C")
else:
  print("학점: F")

# 비교 연산자
# 특정 두 값을 비교할 때
# 대입 연산자(=) vs 같음 연산자(==)
# ==, !=, >, <, >=, <=

# 논리 연산자
# 논리 값(True/False) 사이의 연산을 수행할 때
# and, or, not
if True or False:
  print("Yes")

a = 15
if a <= 20 and a >= 0:
  print("Yes")

# 기타 연산자
# in, not in -> True
# 리스트, 튜플, 문자열, 딕셔너리 모두 사용 가능

# 파이썬의 pass 키워드
# 아무것도 처리하고 싶지 않을 때
# 예) 디버깅 과정에서 일단 조건문의 형태만 만들어놓고, 조건문을 처리하는 부분은 비워놓고 싶은 경우
score = 85

if score >= 80:
  pass # 나중에 작성할 소스코드
else:
  print("성적이 80점 미만입니다.")

print("프로그램을 종료합니다.")

# 조건문의 간소화
# 조건문에서 실행될 소스코드가 한 줄인 경우, 굳이 줄바꿈 하지 않고도 간략히 표현 가능
score = 85
if score >= 80: result = "Success"
else: result = "Fail"
print(result)

# 조건부 표현식: if ~ else문은 한 줄에 작성할 수 있게 해줌
# (if가 중간에 들어감, 참일 때 왼쪽, 거짓일 때 오른쪽)
score = 85
result = "Success" if score >= 80 else "Fail"
print(result)

# 파이썬 조건문 내에서의 부등식
# x > 0 and  x < 20, 0 < x < 20 둘 다 가능
x = 15
if x > 0 and x < 20:
  print("x > 0 and x < 20")
if 0 < x < 20:
  print("0 < x < 20")