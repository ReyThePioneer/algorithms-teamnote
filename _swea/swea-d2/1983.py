#1983 조교의 성적 매기기

T = int(input())
grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

for tc in range(T):
  N, K = map(int, input().split())
  score_total = []

  for _ in range(N):
    mid, fin, hw = map(int, input().split())
    score = (mid * 0.35) + (fin * 0.45) + (hw * 0.2)
    score_total.append(score)
  
  score_k = score_total[K - 1]
  score_total.sort(reverse=True)
  div = N // 10
  grade_k = score_total.index(score_k) // div

  print(f"#{tc + 1} {grade[grade_k]}")