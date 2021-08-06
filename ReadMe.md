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

{

  "signal": "200"

}

http://127.0.0.1:5000/getAllRecordsNoByUserId?user_id=1

getAllRecordsNoByUserId接口

查询id为user_id的用户的所有检查任务

返回示例：

{

  "signal": "200",

  "records": [

​    {

​      "id": 1,

​      "status": 0,

​      "time": "2021-08-05 18:08:14",

​      "user_id": 1

​    },

​    {

​      "id": 3,

​      "status": 0,

​      "time": "2021-08-05 20:30:33",

​      "user_id": 1

​    },

​    {

​      "id": 4,

​      "status": 0,

​      "time": "2021-08-05 21:01:01",

​      "user_id": 1

​    },

​    {

​      "id": 5,

​      "status": 0,

​      "time": "2021-08-05 21:15:53",

​      "user_id": 1

​    },

​    {

​      "id": 6,

​      "status": 0,

​      "time": "2021-08-06 10:40:15",

​      "user_id": 1

​    }

  ]

}

http://127.0.0.1:5000/getDataByNo?record_no=1

getDataByNo接口

返回记录编号为record_no的记录的数据

返回示例

{

  "signal": "200",

  "data": [

​    {

​      "id": 1,

​      "name": "Wang",

​      "position": "manager"

​    },

​    {

​      "id": 2,

​      "name": "Fang",

​      "position": "manager"

​    },

​    {

​      "id": 3,

​      "name": "Luo",

​      "position": "front"

​    },

​    {

​      "id": 4,

​      "name": "Li",

​      "position": "front"

​    },

​    {

​      "id": 5,

​      "name": "Yu",

​      "position": "back"

​    },

​    {

​      "id": 6,

​      "name": "Tian",

​      "position": "back"

​    },

​    {

​      "id": 7,

​      "name": "Wang",

​      "position": "algorithm"

​    },

​    {

​      "id": 8,

​      "name": "Long",

​      "position": "algorithm"

​    },

​    {

​      "id": 9,

​      "name": "Zeng",

​      "position": "database"

​    },

​    {

​      "id": 10,

​      "name": "Deng",

​      "position": "test"

​    }

  ]

}

http://127.0.0.1:5000/getReportByNo?record_no=1

getReportByNo接口

返回记录编号为record_no的记录的分析报告



小程序根据用户id新建一次检查任务（接口createNewRecordById），然后通过用户id查找该用户已经有过的检查任务记录（getAllRecordsNoByUserId），点击一个记录，可以根据获取到的记录No查找记录的原始数据（getDataByNo），也可以根据获取到的记录No查找记录的分析报告pdf（getReportByNo）

## 与设备端的交互

开发中

