from flask import Flask, request
from flask_cors import CORS
import os
#建立路徑到e94111164.txt
path = 'e94111164.txt'
#開啟並讀檔
lab10_plus = open(path, 'r')
app = Flask(__name__)
CORS(app)
global_dic ={}
# web server 路由設定
# 若有get request傳送到 / ，就會執行他下面的這個function，function名稱隨意，但不可重複
@app.route('/',methods=['GET'])
def root():
    return 'ok' # 發送response body 為 ok
@app.route('/set',methods=['POST'])
def second():
  data = request.form.to_dict()
  b = list(data.values())
  if b[0] in list(global_dic.keys()):
    x = 'key exist'
  else:
    global_dic[b[0]] = b[1]
    x = 'set success'
    #開啟讀檔加寫檔
    lab10_plus = open(path,'a')
    #寫入key和value
    lab10_plus.write(b[0] + ' ' + b[1] + ' ' + os.linesep)
    #關閉檔案
    lab10_plus.close() 
  return x
@app.route('/key_list',methods=['GET'])
def third():
  a = list(global_dic.keys())
  return str(a)
@app.route('/get_value/<key>',methods=['GET'])
def forth(key):
  if key in list(global_dic.keys()):
    return global_dic.get(key) 
  else:
    return 'key not found'
@app.route('/update_value',methods=['POST'])
def fifth():
  data = request.form.to_dict()
  b = list(data.values())
  if b[0] in list(global_dic.keys()):
    global_dic[b[0]] = b[1]
    x = 'update success'
    #讀檔
    lab10_plus = open(path,'r')
    #一行一行寫入
    readline = lab10_plus.readlines()
    #寫檔
    lab10_plus = open(path, 'w')
    lab10_plus.write('')
    #寫檔加讀檔
    lab10_plus = open(path, 'a')
    for i in readline:
      #split txt 檔每行的value 和 key
      k = i.split()
      #如果有等於的則改掉
      if k[0] == b[0]:
        k[1] = b[1]
      #沒有就pass
      else:
        pass
      #將k 寫入檔案
      lab10_plus.write(k[0] + ' ' + k[1] + ' ' + os.linesep)
    #關閉檔案
    lab10_plus.close()   
  else:
    x = 'key does not exist'   
  return x
@app.route('/delete/<key>',methods=['GET'])
def sixth(key):
  if key in list(global_dic.keys()):
    del global_dic[key]
    x = 'delete success'
    lab10_plus = open(path,'r')
    readline = lab10_plus.readlines()
    lab10_plus = open(path, 'w')
    lab10_plus.write('')
    lab10_plus = open(path, 'a')
    for i in readline:
      k = i.split()
      #如果一樣的key就跳過
      if k[0] == key:
        pass
      #不一樣則寫入檔案
      else:
        lab10_plus.write(k[0] + ' ' + k[1] + ' ' + os.linesep)
    #關閉檔案
    lab10_plus.close()   
  else:
    x = 'key not found'
  return x
lab10_plus.close()
# 將webserver執行，監聽任意來源ip，port開在3000，開啟debug模式
# debug模式代表，每次檔案更新後，webserver會自動重啟，不需要手動重啟
app.run(host="0.0.0.0", port=3000, debug=True)
