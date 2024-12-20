from flask import Flask, render_template
import json

app = Flask(__name__)

#打开设置文件
with open('settings.json','r') as f:
    settings = json.load(f)

server_name = settings["server_name"]
server_ip = settings["ip"]
server_port = settings["port"]
print(f"服务器名称：{server_name}\n监听地址：{server_ip}:{server_port}")

# 路由，返回提取的数据
@app.route('/')
def home():
    global settings
    # 读取JSON文件并提取数据
    with open('banned-players.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    # 提取name, created, reason字段
    extracted_data = []
    for item in data:
        extracted_info = {
            "name": item["name"],
            "uuid": item["uuid"],
            "created": item["created"],
            "reason": item["reason"]
        }
        extracted_data.append(extracted_info)
    return render_template('index.html', data=extracted_data, config=server_name)

if __name__ == '__main__':
    app.run(host=server_ip,port=server_port)