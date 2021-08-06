from flask import Flask
import pandas as pd
from flask import request, send_from_directory
import pymysql
import json
import os

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
    response_json = {}
    response_json['signal'] = '200'
    res = json.dumps(response_json, ensure_ascii=False)
    return res

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
    response_json = {}
    response_json['signal']='200'
    response_json['records']=record_list
    cursor.close()  # 先关闭游标
    res = json.dumps(response_json, ensure_ascii=False)
    return res

'''根据记录的ID号获取蛀牙的未处理过的数据'''
@app.route("/getDataByNo")
def getDataByNo():
    # get the query args
    record_no = request.args.get("record_no")
    database_pd = getCsv("data", record_no)
    print(database_pd)

    head_list = list(database_pd.columns)  # 拿到表头: [A, B, C, D]
    list_dic = []
    for i in database_pd.values:  # i 为每一行的value的列表：[a2, b2, c3, d2]
        i = i.tolist()
        a_line = dict(zip(head_list, i))
        list_dic.append(a_line)
    # 将 DataFrame  数据再次打包为 JSON 并传回
    response_json = {}
    response_json['signal'] = '200'
    response_json['data']=list_dic
    res = json.dumps(response_json, ensure_ascii=False)
    return res

@app.route("/getReportByNo")
def getReportByNo():
    # get the query args
    record_no = request.args.get("record_no")
    directory = os.getcwd()  # 假设在当前目录
    try:
        file = send_from_directory(directory, "database/report/"+str(record_no)+".pdf",as_attachment=True)
        return file
    except:
        response_json = {}
        response_json['signal'] = '200'
        return response_json