n = int(input())

if (n < 0): # 음수 
  if (n % 2 == 0): # 짝수
    print('A')
  else: # 홀수
    print('B')
else: # 양수
  if (n % 2 == 0): # 짝수
    print('C')
  else: # 홀수
    print('D')
