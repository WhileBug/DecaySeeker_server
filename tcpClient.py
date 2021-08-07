# 导入 socket、sys 模块
import socket
import sys
import json

sendMsg = {
    "method":"report",
    "clientToken":234,
    "timestamp":12312,
    "params":[
        {
            "position":1,
            "ph":5.5,
            "voltage":10.32
        },
        {
            "position":2,
            "ph":5.5,
            "voltage":10.32
        },
        {
            "position":3,
            "ph":5.5,
            "voltage":10.32
        },
        {
            "position":4,
            "ph":5.5,
            "voltage":10.32
        },
        {
            "position":5,
            "ph":5.5,
            "voltage":10.32
        },
        {
            "position":6,
            "ph":5.5,
            "voltage":10.32
        }
    ]
}

# 创建 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()

# 设置端口号
port = 8848

# 连接服务，指定主机和端口
s.connect((host, port))

# 发送收集到的数据
sendMsgTxt = json.dumps(sendMsg)
s.send(sendMsgTxt.encode('utf-8'))


s.close()
