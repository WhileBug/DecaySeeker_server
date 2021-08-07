# MothSeeker 服务器端代码

./database：存储数据的文件夹

app.py：主程序

## 部署方式

运行database/sql/mothseeker.sql文件，构建mysql数据库

进入主文件夹，输入flask run运行

## 与微信端的交互

http://127.0.0.1:5000/createNewRecordById?user_id=1

createNewRecordById接口

为id为user_id的用户创建一个新的检查记录

返回示例：

```
{"signal": "200", "token": "838412"}
```

http://127.0.0.1:5000/getAllRecordsNoByUserId?user_id=1

getAllRecordsNoByUserId接口

查询id为user_id的用户的所有检查任务

返回示例：

```
{

  "signal": "200",

  "records": [

​    {

​      "id": 1,

​      "status": 0,

​      "time": "2021-08-05 18:08:14",

​      "user_id": 1

​    },

  ]

}
```

http://127.0.0.1:5000/getDataByNo?record_no=1

getDataByNo接口

返回记录编号为record_no的记录的数据

返回示例

```
{

  "signal": "200",

  "data": [

​    {

​      "position": 1,

​      "ph": 7,

​      "voltage": 2

​    },

  ]

}
```

http://127.0.0.1:5000/getReportByNo?record_no=1

getReportByNo接口

返回记录编号为record_no的记录的分析报告

返回格式：PDF

http://127.0.0.1:5000/getTokenByCheckNo?record_no=1

getTokenByCheckNo接口

返回编号为record_no的记录的验证码token

返回格式：{"signal": "200", "token": 231}

小程序根据用户id新建一次检查任务（接口createNewRecordById）并返回验证码token，设备端填入验证码token，然后通过用户id查找该用户已经有过的检查任务记录（getAllRecordsNoByUserId），点击一个记录，可以根据获取到的记录No查找记录的原始数据（getDataByNo），也可以根据获取到的记录No查找记录的分析报告pdf（getReportByNo）

## 与设备端的交互

启动tcpServer运行与设备端交互的服务端代码即可，传输格式：

```
sendMsg = {
    "method":"report",
    "clientToken":"123",
    "timestamp":12312,
    "params":{
        "position":1,
        "ph":5.5,
        "voltage":10.32
    }
}
```
