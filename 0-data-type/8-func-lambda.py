# < 함수와 람다 표현식 >

# 함수(Function)
  # 함수: 특정한 작업을 하나의 단위로 묶어놓은 것
  # 함수를 사용하면 불필요한 소스코드의 반복을 줄일 수 있음

# 함수의 종류
  # 내장 함수: 파이썬이 기본적으로 제공하는 함수
  # 사용자 정의 함수: 개발자가 직접 정의하여 사용할 수 있는 함수

# 함수 정의하기
  # 프로그램에는 똑같은 코드가 반복적으로 사용될 때가 많음
  # 함수를 사용하면 소스코드의 길이를 줄일 수 있음
  # 매개변수: 함수 내부에서 사용할 변수
  # 반환 값: 함수에서 처리된 결과를 반환

# 더하기 함수 예시 (1)
def add(a, b):
  return a + b

def subtract(a, b):
  return a - b

result = add(3, 7)
print(result)

result = subtract(3, 7)
print(result)

# 더하기 함수 예시 (2)
  # 파라미터의 변수 직접 지정하기(매개변수 순서 달라도 상관X)
def add(a, b):
  print("함수의 결과: ", a + b)

add(3, 7)
add(b = 3, a = 7)

# global 키워드 (Scope)
  # global 키워드로 변수를 지정하면, 해당 함수에서는 지역변수를 만들지 않고, 함수 바깥에 선언된 변수를 바로 참조
a = 0

def func():
  global a # 바깥 쪽에 있는 a = 0을 참조
  a += 1

for i in range(10):
  func()

print(a)

# 전역변수로 선언된 list 객체의 method 호출은 오류 없이 수행 가능
# 함수 안에 전역변수와 동일한 이름의 지역변수 리스트가 선언된다면, 함수 안에서는 지역변수가 우선으로 참조됨
array = [1, 2, 3, 4, 5]

def func():
  global array
  array = [3, 4, 5] # 여기 말고 바깥 쪽에 있는 array 참조
  array.append(6)
  print(array)

func()

# 파이썬 함수는 여러 개의 반환 값을 가질 수 있음 (Packing, Unpacking)
def operator(a, b):
  add_var = a + b
  subtract_var = a - b
  multiply_var = a * b
  divide_var = a / b
  return add_var, subtract_var, multiply_var, divide_var

a, b, c, d = operator(7, 3)
print(a, b, c, d)

# < 람다 표현식 >
  # 함수를 간단하게 작성할 수 있음
  # 특정한 기능을 수행하는 함수를 한 줄에 작성할 수 있음

# 일반적인 add() 메서드
def add(a, b):
  return a + b

print(add(3, 7))

# 람다 표현식으로 구현한 add() 메서드
print((lambda a, b: a + b)(3, 7))

# 내장 함수에서 자주 사용되는 람다 함수
array = [('홍길동', 50), ('이순신', 32), ('아무개', 74)]

def my_key(x):
  return x[1] # 두 번째 원소 기준으로 정렬하기 위함

print(sorted(array, key=my_key))
print(sorted(array, key=lambda x: x[1])) # 한 줄로!

# 여러 개의 리스트에 적용
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

result = map(lambda a, b: a + b, list1, list2)

print(list(result))