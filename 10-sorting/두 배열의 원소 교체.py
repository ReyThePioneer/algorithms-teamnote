# 핵심 아이디어 : 매번 배열 A에서 가장 작은 원소를 골라서, 배열 B에서 가장 큰 원소와 교체
# A 오름차순 정렬, B 내림차순 정렬
# A의 원소가 B의 원소보다 작을 때에만 교체 수행
# 두 배열의 원소가 최대 100,000개까지 입력될 수 있으므로, 최악의 경우 O(NlogN)을 보장하는 정렬 알고리즘을 이용해야 함

n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort() # 배열 A 오름차순 정렬
b.sort(reverse=True) # 배열 B 내림차순 정렬

# 첫 번째 인덱스부터 확인하며, 두 배열의 원소를 최대 K번 비교
for i in range(k):
  # A의 원소가 B의 원소보다 작은 경우
  if a[i] < b[i]:
    # 두 원소를 교체
    a[i], b[i] = b[i], a[i]
  # A의 원소가 B의 원소보다 크거나 같을 때, 반복문을 탈출
  else:
    break

print(sum(a))