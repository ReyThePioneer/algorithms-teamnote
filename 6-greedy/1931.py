#1931 회의실 배정

n = int(input())
meetings = []

for _ in range(n):
    meetings.append(list(map(int, input().split())))

# 회의 종료 시간 오름차순 정렬 후, 시작 시간 오름차순 정렬
meetings.sort(key = lambda x: (x[1], x[0]))

cnt = 1
end = meetings[0][1]

for meeting in meetings:
    if meeting[0] > end:
        end = meeting[1]
        cnt += 1
        
print(cnt)