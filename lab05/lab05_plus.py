#建立dict存取
dict0 = {}
#用迴圈輸入鍵
for n in range(0, 4):
  key = input("Enter key: ")
  value_list = []
  #用迴圈輸入值
  for k in range(0, 5):
    value = input("Enter value: ")
    value_list.append(value)
    dict0[key] = value_list
#印出整個dict
print(dict0)
