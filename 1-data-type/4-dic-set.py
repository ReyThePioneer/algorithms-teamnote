# < 사전 자료형 >

# Key와 Value의 쌍을 데이터로 가지는 자료형 (순차적 저장 X)
# 변경 불가능한(immutable) 자료형을 Key로 사용 가능
# Python의 사전 자료형은 Hash Table을 이용하므로, 데이터의 조회 및 수정에 있어 O(1) 시간에 처리 가능
data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

print(data)

if '사과' in data:
  print("'사과'를 키로 가지는 데이터가 존재합니다.")

# keys(): 키 데이터만 뽑아서 리스트로 이용할 때
# values(): 값 데이터만 뽑아서 리스트로 이용할 때
a = dict()
a['홍길동'] = 97
a['이순신'] = 98
print(a)

b = {
  '홍길동': 97,
  '이순신': 98 }
print(b)
print(b['이순신'])

key_list = list(b.keys())
value_list = list(b.values())

print(key_list)
print(value_list)

for key in key_list:
  print(b[key])


# < 집합 자료형 >

# 집합의 특징
  # 중복을 허용하지 않음
  # 순서가 없음
  # -> 특정 데이터 존재 여부 확인할 때 사용하면 좋음
# 집합 초기화
  # 리스트 또는 문자열 이용 (set 함수)
  # 중괄호{} 안에 각 원소를 콤마(,) 기준으로 구분하여 삽입
# 데이터 조회 및 수정: O(1) 시간에 처리 가능
data = set([1, 1, 2, 3, 4, 4, 5])
print(data) # 중복 데이터는 제거됨

data = {1, 1, 2, 3, 4, 4, 5}
print(data)

# 집합 자료형의 연산
a = set([1, 2, 3, 4, 5])
b = set([3, 4, 5, 6, 7])
print(a | b) # 합집합
print(a & b) # 교집합
print(a - b) # 차집합

# 집합 자료형 관련 함수
data = set([1, 2, 3])
print(data)

data.add(4) # 새로운 원소 추가
print(data)

data.update([5, 6]) # 새로운 원소 여러 개 추가
print(data)

data.remove(3) # 특정한 값을 갖는 원소 삭제
print(data)


# < 사전 자료형과 집합 자료형의 특징 >
  # 리스트, 튜플: 순서가 있음 -> 인덱싱으로 값 얻을 수 있음
  # 사전, 집합: 순서가 없음 -> 인덱싱으로 값 얻을 수 없음
  # 사전의 키(Key) 또는 집합의 원소(Element)를 이용 -> O(1)의 시간복잡도로 조회