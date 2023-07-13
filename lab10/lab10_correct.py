from flask import Flask, request
from flask_cors import CORS
import os
#建立路徑到e94111164.txt
path = 'e94111164.txt'
#檢查檔案是否存在
if not os.path.exists(path):
    #在 Python 中建立 touch 檔案
    os.system('touch '+path)
app = Flask(__name__)
CORS(app)

@app.route('/',methods=['GET'])
def first():
    return 'ok'
  
@app.route('/set',methods=['POST'])
def second():
    data = request.form.to_dict()
    #讀檔並寫入txt檔中
    with open(path, 'r') as f:
        #逐條讀檔並分開key和value
        for line in f.readlines():
            list = line.strip('\n').split(" ")
            if len(list)>1:
                if data['key']==list[0]:
                    return 'key exist'
    #寫檔
    with open(path, 'a') as f:
        string = data['key'] + " " + data['value']+"\n"
        f.write(string)
        
    return 'set success'

@app.route('/key_list',methods=['GET'])
def key_list():
    return_list = []
    #讀檔並寫入txt檔中
    with open(path, 'r') as f:
        for line in f.readlines():
            list = line.strip('\n').split(" ")
            if len(list)>1:
                return_list.append(list[0])
    return str(return_list)
    
@app.route('/get_value/<key>',methods=['GET'])
def get_value(key):
    #讀檔並寫入txt檔中
    with open(path, 'r') as f:
        for line in f.readlines():
            list = line.strip('\n').split(" ")
            if len(list)>1:
                if key==list[0]:
                    return list[1]

    return 'key not found'
   

@app.route('/update_value',methods=['POST'])
def update_value():
    data = request.form.to_dict()
    count = 0
    with open(path, 'r') as f:
        lines = f.readlines()
    ＃看有沒有一樣的，有則不寫ㄒㄨˋ
    with open(path,'w') as f:
        for line in lines:
            list = line.strip('\n').split(" ")
            if list[0]==data['key']:
                string = data['key'] + " " + data['value']+"\n"
                f.write(string)
                count = 1
            else:
                f.write(line)
    if count==0:
        return 'key does not exist'
    else:
        return 'update success'

@app.route('/delete/<key>',methods=['GET'])
def delete(key):
    count = 0
    with open(path, 'r') as f:
        lines = f.readlines()
    #看有沒有一樣的，如果一樣則不寫入
    with open(path,'w') as f:
        for line in lines:
            list = line.strip('\n').split(" ")
            if list[0]==key:
                count = 1
            else:
                f.write(line)
    if count==0:
        return 'key not found'
    else:
        return 'delete success'
# 將webserver執行，監聽任意來源ip，port開在3000，開啟debug模式
# debug模式代表，每次檔案更新後，webserver會自動重啟，不需要手動重啟
app.run(host="0.0.0.0", port=3000, debug=True)
