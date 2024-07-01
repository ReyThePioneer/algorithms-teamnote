#2578 빙고

import sys

# 5 x 5 빙고판 정보 입력받기
board = []
for _ in range(5):
    board.append(list(map(int, sys.stdin.readline().split())))

# 사회자가 부르는 수 차례대로 입력받기
erase = []
for _ in range(5):
    erase.append(list(map(int, sys.stdin.readline().split())))

# 숫자를 빠르게 찾기 위해 Dictionary 사용
pos = {}
for i in range(5):
    for j in range(5):
        pos[board[i][j]] = (i, j)

# 빙고판 상태를 나타내는 2차원 리스트
marked = [[0] * 5 for _ in range(5)]

# 현재 몇 빙고인지 검사하는 함수
def check_bingo():
    bingo_cnt = 0

    # 가로 빙고
    for row in marked:
        if sum(row) == 5:
            bingo_cnt += 1
    
    # 세로 빙고
    for col in range(5):
        if sum(marked[row][col] for row in range(5)) == 5:
            bingo_cnt += 1
    
    # 대각선 빙고
    # 왼쪽 위 -> 오른쪽 아래 방향
    if sum(marked[i][i] for i in range(5)) == 5:
        bingo_cnt += 1
    # 오른쪽 위 -> 왼쪽 아래 방향
    if sum(marked[i][4-i] for i in range(5)) == 5:
        bingo_cnt += 1
    
    # 총 몇 빙고인지 리턴
    return bingo_cnt

# 사회자가 부른 숫자를 하나씩 지우고 몇 빙고인지 검사
erase_cnt = 0
three_bingo = False

for row in erase:
    # 사회자가 부른 숫자가 보드의 어느 위치에 있는지 가져오고 숫자 지우기(1로 표시)
    for num in row:
        if num in pos:
            x, y = pos[num]
            marked[x][y] = 1
            erase_cnt += 1
            
            # 3빙고 완성 시
            if check_bingo() >= 3:
                three_bingo = True
                print(erase_cnt)
                break
                
    if three_bingo:
        break