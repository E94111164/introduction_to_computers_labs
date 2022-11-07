#建立dictionary存取
dict0 = {
  "index":['國文', '英文', '數學', '自然', '社會'], "StuA":[50, 60, 70, 80, 90], "StuB":[57, 86, 73, 82, 43], "StuC":[97, 96, 86, 97, 83]
}
#印出整個dictionary
print(dict0)
#取名方便
stu_name = ['A', 'B', 'c']
#dict_values以list轉換成串列，才可使用索引方式取得元素值
sc = list(dict0.values())
#用迴圈得分數
#二維表格
#國文 英文 數學 自然 社會
# 50  60  70  80   90...
for i in range(1,4):
  total = sum(sc[i])/5
  print(stu_name[i-1], "學生平均成績: ", total)
for j in range(0,5):
  ave = (sc[1][j]+sc[2][j]+sc[3][j])/3
  print(sc[0][j], "的平均分數: ", ave)
 
