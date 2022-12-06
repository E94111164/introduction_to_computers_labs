from flask import Flask, request
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
#建立全域字典
global_dic ={}
# web server 路由設定
# 若有get request傳送到 / ，就會執行他下面的這個function，function名稱隨意，但不可重複
@app.route('/',methods=['GET'])
def first():
    return 'ok' # 發送response body 為 ok

@app.route('/set',methods=['POST'])
def second():
  #資料轉成字典
  data = request.form.to_dict()
  #將他的value用成list
  b = list(data.values())
  #檢查其是否在全域字典中
  if b[0] in list(global_dic.keys()):
    return 'key exist'
  #不再的話要將b[0]作為key,b[1]作為value帶入全域字典
  else:
    global_dic[b[0]] = b[1]
    return 'set success'
@app.route('/key_list',methods=['GET'])
def third():
  #將全域字典的key轉為list
  a = list(global_dic.keys())
  #用字串傳回去
  return str(a)
@app.route('/get_value/<key>',methods=['GET'])
def forth(key):
  #檢查key是否在全域字典中
  if key in list(global_dic.keys()):
    return global_dic.get(key)
    #回傳key的值 
  else:
    return 'key not found'
@app.route('/update_value',methods=['POST'])
def fifth():
  data = request.form.to_dict()
  b = list(data.values())
  #檢查是否在字典中
  if b[0] in list(global_dic.keys()):
    #更新字典
    global_dic[b[0]] = b[1]
    return 'update success'
  else:
    return 'key does not exist'
@app.route('/delete/<key>',methods=['GET'])
def sixth(key):
  if key in list(global_dic.keys()):
    #刪除此key和value
    del global_dic[key]
    return 'delete success'
  else:
    return 'key not found'
# 將webserver執行，監聽任意來源ip，port開在3000，開啟debug模式
# debug模式代表，每次檔案更新後，webserver會自動重啟，不需要手動重啟
app.run(host="0.0.0.0", port=3000, debug=True)
