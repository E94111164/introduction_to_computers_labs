#建立亂數模組
import random as r
Times = {"One":0, "Two":0, "Three":0, "Four":0, "Five":0, "Six":0}
#建立數值的list
list1 = list(Times.keys())
#建立計算總數的list
list2 = list(Times.values())

#利用迴圈計算1到6出現的次數
for i in range(1000000):
  num = r.randint(1, 6)
  if num == 1:
    list2[0] = list2[0] +1
  elif num == 2:
    list2[1] = list2[1]+1
  elif num == 3:
    list2[2] = list2[2]+1
  elif num == 4:
    list2[3] = list2[3]+1
  elif num == 5:
    list2[4] =list2[4]+1
  else:
    list2[5] =list2[5]+1
#利用迴圈算出機率    
for n in range(6):
  num = round(list2[n]/10000,2)
  print("The probability of", list1[n], "is", num, "%")
