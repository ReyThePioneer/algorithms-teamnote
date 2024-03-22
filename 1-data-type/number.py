# < 수 자료형 >

# 1. 정수형 : 정수를 다루는 자료형
# 양의 정수
a = 1000
print(a)

# 음의 정수
a = -7
print(a)

# 0
a = 0
print(a)

# 2. 실수형 : 소수점 아래의 데이터를 포함하는 수 자료형
# 양의 실수
a = 157.93
print(a)

# 음의 실수
a = -1837.2
print(a)

# 소수부가 0일 때 0을 생략
a = 5.
print(a)

# 정수부가 0일 때 0을 생략
a = -.7
print(a)

# 3. 지수 표현 방식
# 1,000,000,000
a = 1e9
print(a)
a = int(1e9)
print(a)

# 752.5
a = 75.25e1
print(a)

# 3.954
a = 3954e-3
print(a)

# 4. 실수 표현에서의 오차
a = 0.3 + 0.6
print(a)

if a == 0.9:
  print(True)
else:
  print(False)

# round() 함수 이용
a = 0.3 + 0.6
print(round(a, 4))

if round(a, 4) == 0.9:
  print(True)
else:
  print(False)

# 5. 수 자료형의 연산
a = 7
b = 3

# 나누기
print(a / b)

# 나머지
print(a % b)

# 몫
print(a // b)

# 거듭제곱
print(a ** b)

# 제곱근
print(a ** 0.5)