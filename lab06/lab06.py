def gcd(a,b):
  m = max(a, b)
  n = min(a, b)
  if a!= 0 and b != 0 :
    r =  m % n
    while r !=  0 :
      m = n
      n = r
      r = m % n
    if n != 1 :
      print(a,"和", b, "的gcd=", n)
    else:
      print(a, "和", b, "互質")
  else:
    print("0沒有gcd")

ans1 = gcd(80, 20)
ans2 = gcd(10, 0)
ans3 = gcd(19,20)
