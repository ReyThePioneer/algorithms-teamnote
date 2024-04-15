n = int(input(), 16) # 16진수 입력

for i in range(1, 16):
  print('%X*%X=%X' %(n, i, n * i)) # 16진수 출력