#利用函式計算輾轉相除法
def gcd(a,b):
  #透過max,min求出兩數中較大值
  m = max(a, b)
  n = min(a, b）
  #兩個都沒有0才可進行輾轉相除法
  if a!= 0 and b != 0 :
    r =  m % n
    #利用迴圈進行輾轉相除法
    while r !=  0 :
      m = n
      n = r
      r = m % n
    #利用n等不等於1來判斷是否互質
    if n != 1 :
      print(a,"和", b, "的gcd=", n)
    else:
      print(a, "和", b, "互質")
  else:
    print("0沒有gcd")

ans1 = gcd(80, 20)
ans2 = gcd(10, 0)
ans3 = gcd(19,20)
