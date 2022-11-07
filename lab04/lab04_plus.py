A = []
B = []
C = []

print("開始輸入A同學的成績，請依照 國文、英文、數學、自然、社會 的順序輸入:")
#利用迴圈輸入成績
for i in range(0, 5):
  score = input()
  score = int(score)
  A.append(score)
  #用while迴圈防呆
  while score>100 or score<=0:
    print("請輸入1~100: ")
    A.pop()
    score = input()
    score = int(score)
    A.append(score)
    if score <100 and score > 0:
      break
print("A學生成績: ")
print("國文: ", A[0], "、英文: ", A[1], "、數學: ", A[2], "、自然: ", A[3], "、社會: ", A[4])

print(" ")
print("開始輸入B同學的成績，請依照 國文、英文、數學、自然、社會 的順序輸入:")
for i in range(0, 5):
  score = input()
  score = int(score)
  B.append(score)
  #用while迴圈防呆
  while score > 100 or score <= 0:
    print("請輸入1~100: ")
    B.pop()
    score = input()
    score = int(score)
    B.append(score)
    if score < 100 and score > 0:
      break
print("B學生成績: ")
print("國文: ", B[0], "、英文: ", B[1], "、數學: ", B[2], "、自然: ", B[3], "、社會: ", B[4])

print(" ")
print("開始輸入C同學的成績，請依照 國文、英文、數學、自然、社會 的順序輸入:")
for i in range(0, 5):
  score = input()
  score = int(score)
  C.append(score)
  #用while迴圈防呆
  while score>100 or score<=0:
    print("請輸入1~100: ")
    C.pop()
    score = input()
    score = int(score)
    C.append(score)
    if score <100 and score > 0:
      break
print("C學生成績: ")
print("國文: ", C[0], "、英文: ", C[1], "、數學: ", C[2], "、自然: ", C[3], "、社會: ", C[4])

#利用變數計算平均
sumA = 0
sumB = 0
sumC = 0

#利用迴圈計算平均
for i in range(0, 5):
  sumA = sumA + int(A[i])
print("A同學平均成績: ", sumA/5)
