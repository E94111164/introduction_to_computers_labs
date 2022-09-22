#此步input一個變數number
number = input("1. pleace input a number:")

#轉換變數的資料型態由字串變為整數
n = int(number)

#利用除以二的餘數判別此數的奇偶
if n%2 == 0:
  print("this is even")
else: 
  print("this is odd")

#此步input一個變數capital
capital = input("2. please input your student ID first character:")

#此步input一個變數id
id = input("3. please input your student ID last 8 numbers:")

#轉換變數的資料型態由字串轉為整數
newid = int(id)

#利用除以二的餘數判別此數的奇偶
if newid%2 == 0:
  print("your student ID number is even")
else: 
  print("your student ID number is odd")

#轉換變數的資料型態由整數轉為字串
newnewid = str(newid)

#將兩個同為字串的資料型態相加並輸出
print ("your student ID is:", capital+newnewid)
