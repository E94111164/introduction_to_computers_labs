import matplotlib.pyplot as plt
import numpy as np

#每一行的數字
a = []
#每年的串列
years = []
path =  "Temperature.txt"
#開始讀檔
f = open(path, "r")
#讀掉Tainan:這行
f.readline()
#開始讀入數字
for line in f.readlines():
    #轉為float, 刪掉換行, 用,去分
    line = list(map(float, line.rstrip("\n").split(",")))
    #將年份改為整數加入years
    years.append(int(line[0]))
    #將年份刪掉只留溫度
    del line[0]
    a.append(line)
#關檔
f.close

#建立從16到30的串列
Temps = list(range(16, 32, 2))
#建立0到12的月份串列
months = list(range(1,13))

#圖一

# 建立圖表
fig = plt.figure() 
#建立每年的線
for i in range(len(a)):
    plt.plot(months, a[i], label=years[i])
#決定x座標軸
plt.xticks(months)
plt.title('Tainan Monthly Mean Temperature From 2013 To 2021')
plt.xlabel('Months')
plt.ylabel('Temperature in Degree C')
#固定位置
plt.legend(loc = 'lower center')
plt.show()
fig.savefig('lab13_01.png') #儲存圖片

#圖二
#每月溫度平均的串列
ave_m_temp = []
#總溫度加總
alltemp = 0
for i in range(len(months)):
    #每月溫度加總
    sum_month = 0
    for j in a:
        sum_month += j[i]
    alltemp += sum_month
    #計算每月平均小數點到第二位加入串列
    ave_m_temp.append(round(sum_month/len(a), 2))
# 建立圖表
fig = plt.figure() 
#散佈圖
plt.scatter(months, ave_m_temp, color = 'red')
#畫線
plt.plot(months, ave_m_temp) 
#計算年溫度平均到第二位
ave_y_temp = round((alltemp / 108), 2)

#建立年平均線
plt.axhline(y=ave_y_temp, xmin=0, xmax=13, color = 'red', linestyle = "--", label = 'Mean of 9 Years')
#寫上年平均值
plt.text(1, ave_y_temp, ave_y_temp, va = 'bottom', fontsize = 10)
#寫上月平均值
for i, j in zip(months, ave_m_temp):
    plt.text(i, j, j, va = 'bottom', fontsize = 10)
#確立xy座標軸 
plt.xticks(months)
plt.yticks(list(range(16,34,2)))
plt.title('Tainan Monthly Mean Temperature Of 2013 To 2021')
plt.xlabel('Month')
plt.ylabel('Temperature in Degree C')
plt.legend() 
plt.show()
fig.savefig('lab13_02.png')

#合併圖表
fig = plt.figure(figsize=(15,6))
#建立第一張子圖
plt.subplot(1,2,1)
#圖一
for i in range(len(a)):
    plt.plot(months, a[i], label=years[i])
plt.xticks(months)
plt.title('Tainan Monthly Mean Temperature From 2013 To 2021')
plt.xlabel('Months')
plt.ylabel('Temperature in Degree C')
plt.legend(loc = 'lower center')

#建立第二張子圖
plt.subplot(1,2,2)
#圖二
ave_m_temp = []
alltemp = 0
for i in range(len(months)):
    sum_month = 0
    for j in a:
        sum_month += j[i]
    alltemp += sum_month
    ave_m_temp.append(round(sum_month/len(a), 2))
plt.scatter(months, ave_m_temp, color = 'red')
plt.plot(months, ave_m_temp) 
ave_y_temp = round((alltemp / 108), 2)
ave_list = []

plt.axhline(y=ave_y_temp, xmin=0, xmax=13, color = 'red', linestyle = "--", label = 'Mean of 9 Years')
plt.text(1, ave_y_temp, ave_y_temp, va = 'bottom', fontsize = 10)
for i, j in zip(months, ave_m_temp):
    plt.text(i, j, j, va = 'bottom', fontsize = 10)
 
plt.xticks(months)
plt.yticks(list(range(16,34,2)))
plt.title('Tainan Monthly Mean Temperature Of 2013 To 2021')
plt.xlabel('Month')
plt.ylabel('Temperature in Degree C')
plt.legend() 

#繼續合併
plt.tight_layout() #讓子圖之間適當排列不重疊
plt.show()
fig.savefig('lab13_03.png')
