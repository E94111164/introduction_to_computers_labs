import os
#找到路徑但為字串
a = os.path.abspath(os.getcwd())
#將其用split分開成list
b = a.split("/")
#把一開始的空格delete掉
del b[0]
#輸出list
print(b)
#讀取 ‘/home/學號’ 目錄下所有檔案和資料夾
c = os.listdir("/home/e94111164")
print(c)

#取得兩串列長度
ran1 = len(b)
ran2 = len(c)

path = 'e94111164.txt'

#開檔、寫檔
lab08 = open(path, 'w')
#用for迴圈一行一行寫入
for i in range (ran1):
    lab08.write(b[i]+os.linesep)
#用linesep換行
lab08.write(os.linesep)
#用for迴圈一行一行寫入
for i in range (ran2):
    lab08.write(c[i]+os.linesep)
#關閉檔案
lab08.close()
#讀檔
f = open(path, 'r')
fi = f.readlines()
#一行一行讀檔並輸出
for line in fi:
  print(line.strip())
#關閉檔案
f.close()

