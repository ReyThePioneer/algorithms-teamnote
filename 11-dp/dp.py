# 다이나믹 프로그래밍 
# 메모리를 적절히 사용하여 수행 시간 효율성을 비약적으로 향상시키는 방법
# 이미 계산된 결과(작은 문제)는 별도의 메모리 영역에 저장하여 다시 계산 X
# 일반적으로 top-down과 bottom-up 두 가지 방식

# 다이나믹 프로그래밍 (=동적 계획법)
# 자료구조에서 동적 할당(Dynamic Allocation) : 프로그램이 실행되는 도중에 실행에 필요한 메모리를 할당하는 기법
# 다이나믹 프로그래밍에서의 '다이나믹' : 별다른 의미 없이 사용된 단어

# 다이나믹 프로그래밍의 조건
# 1. 최적 부문 구조(Optimal Substructure) : 큰 문제를 작은 문제로 나눌 수 있으며 이 작은 문제의 답을 모아서 큰 문제를 해결
# 2. 중복되는 부분 문제(Overlapping Subproblem) : 동일한 작은 문제를 반복적으로 해결

# 피보나치 수열
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# 점화식 : 인접한 항들 사이의 관계식
# a(n) = a(n-1) + a(n-2), a(1)=1, a(2)=1
# 수열을 배열이나 리스트를 이용해 표현(table)