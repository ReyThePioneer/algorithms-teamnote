# K가 2 이상이기만 하면, K로 나누는 것이 1을 빼는 것보다 항상 빠르게 N을 줄일 수 있음

n, k = map(int, input().split())
result = 0

while True:
  # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
  target = (n // k) * k # K로 나누어떨어지는 가장 가까운 수
  result += (n - target) # 1을 빼는 연산 횟수
  n = target

  # N이 K보다 작을 때(더이상 나눌 수 없을 때) 반복문 탈출
  if n < k:
    break
  # N을 K로 나누기
  result += 1
  n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n - 1)
print(result)