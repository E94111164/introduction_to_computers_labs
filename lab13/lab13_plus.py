import matplotlib.pyplot as plt 
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

#讀檔
path = 'oddExperiment.txt'
f = open(path, 'r')
#建立xy空串列
y = list()
x = list()
f.readline()
for line in f.readlines():
    #轉為float, 刪掉換行, 用,去分
    line = list(map(float, line.rstrip("\n").split(" ")))
    #加入xy串列中
    y.append(line[0])
    x.append(line[1])
f.close

#建立圖表
fig = plt.figure()

#建立散佈圖
plt.scatter(x, y, label = 'Data')
#產出一階多項式
fcnone = np.poly1d(np.polyfit(x, y, deg = 1))
#帶入x求一階多項式的y
value_y_1 = fcnone(x)
#求least square error (mean square error)並用成字串
mse_1 = str(round(mean_squared_error(y, value_y_1), 5))
#求 R square error (R2)並用成字串
Rse_1 = str(round(r2_score(y, value_y_1),5))

#產出二階多項式
fcntwo = np.poly1d(np.polyfit(x, y, 2))
value_y_2 = fcntwo(x)
mse_2 = str(round(mean_squared_error(y, value_y_2), 5))
Rse_2 = str(round(r2_score(y, value_y_2), 5))

#畫成線
plt.plot(x, value_y_1, color = '#FFD700', label = "Fit of degree 1, LSE ="+ mse_1)
plt.plot(x, value_y_2, color = '#006400', label = "Fit of degree 2, LSE = "+ mse_2)
plt.plot(x, value_y_1, color = '#FF0000',label="Fit of degree 1, R2 = "+ Rse_1)
plt.plot(x, value_y_2, color = '#7400A1',label="Fit of degree 2, R2 = "+ Rse_2)

plt.title('oddExperiment Data')
plt.legend()
plt.savefig('lab13_plus.png')
plt.show()
