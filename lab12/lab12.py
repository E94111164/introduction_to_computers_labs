import requests
import pymysql
#新竹縣立案短期補習班基本資料
#https://bsb.kh.edu.tw/afterschool/opendata/afterschool_json.jsp?city=36
#從網頁上get 新竹市立案短期補習班基本資料的json檔
s = requests.get('https://bsb.kh.edu.tw/afterschool/opendata/afterschool_json.jsp?city=36')
#此為存dictionary的list
data = s.json()
#wordpress連線
db = pymysql.connect(host='localhost', port=3306, user='e94111164', passwd='Ll96120828', db='wordpress')
##建立操作游標
cursor = db.cursor()
#i為得到json檔中的dictionary
for i in data:
      #用dict的key找value並加進資料表
      sql = "INSERT INTO 新竹縣立案短期補習班基本資料(地區縣市, 短期補習班名稱, 主管機關文件單位代碼, 短期補習班類別) VALUES ('" + i["地區縣市"] + "','" + i["短期補習班名稱"] + "', '" + i["主管機關文件單位代碼"] +"', '" + i["短期補習班類別"] +"')"
      cursor.execute(sql)
      #提交修改
      db.commit()
 
#關閉連線
db.close()
