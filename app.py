from flask import Flask
import pandas as pd
from flask import request
import pymysql
import json

host = 'localhost'
port = 3306
db = 'MothSeeker'
user = 'admin'
password = 'password'


# ---- 用pymysql 操作数据库
def get_connection():
    conn = pymysql.connect(host=host, port=port, db=db, user=user, password=password)
    return conn

conn = get_connection()


def getCsv(signal, record_no):
    if(signal=="data"):
        database_pd = pd.read_csv("database/data/"+str(record_no)+".csv",index_col=0)
    elif (signal == "report"):
        database_pd = pd.read_csv("database/report/" + str(record_no) + ".csv",index_col=0)
    return database_pd
app = Flask(__name__)

@app.route("/createNewRecordById")
def createNewRecordById():
    # get the query args
    user_id = request.args.get("user_id")
    # 获取游标
    cursor = conn.cursor()

    # 定义要执行的sql语句
    sql = 'insert into check_record(status,user_id) values(0,'+str(user_id)+');'

    # 拼接并执行sql语句
    cursor.execute(sql)

    # 涉及写操作要注意提交
    conn.commit()
    cursor.close()  # 先关闭游标
    return "111111"

'''根据用户id号获取该用户对应的所有记录Id'''
@app.route("/getAllRecordsNoByUserId")
def getAllRecordsNoByUserId():
    # get the query args
    user_id = request.args.get("user_id")

    # 获取游标
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM CHECK_RECORD WHERE user_id='+str(user_id))

    record_list = []
    while 1:
        record = cursor.fetchone()
        if record is None:
            # 表示已经取完结果集
            break
        print(type(record))
        temp_record = {}
        temp_record['id']=record[0]
        temp_record['status'] = record[1]
        temp_record['time'] = str(record[2])
        temp_record['user_id'] = record[3]
        record_list.append(temp_record)
    print(record_list)
    cursor.close()  # 先关闭游标
    res = json.dumps(record_list, ensure_ascii=False)
    return res

'''根据记录的ID号获取蛀牙的未处理过的数据'''
@app.route("/getDataById")
def getDataById():
    # get the query args
    record_no = request.args.get("record_no")
    database_pd = getCsv("data", record_no)
    print(database_pd)
    # 将 DataFrame  数据再次打包为 JSON 并传回
    res = database_pd.to_json(orient="records", force_ascii=False)
    return res

@app.route("/getAnalysis")
def getAnalysis():
    return ""