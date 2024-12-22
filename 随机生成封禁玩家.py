import random
import json
import uuid
import time

texts = "_abcdefgh_igklm_nopqrstuvwxy_z"
data = []

with open('banned-players.json','w') as f:
    for i in range(int(input("玩家数："))):
        name = ""
        for i in range(random.randint(5,7)):
            name += texts[random.randint(0,29)]
            name += str(random.randint(0,9))
            # 将字符串转换成列表
            str_list = list(name)
            # 调用random模块的shuffle函数打乱列表
            random.shuffle(str_list)
            # 将列表转字符串
            name = "".join(str_list)
        data.append({
            "uuid": str(uuid.uuid4()),
            "name": name,
            "created": f"{random.randint(2019,2024)}-{random.randint(10,12)}-{random.randint(10,30)} {random.randint(10,23)}:{random.randint(10,59)}:{random.randint(10,59)} +0800",
            "source": "Console",
            "expires": "forever",
            "reason": f"TEST_{i}"
        })
    json_data = json.dumps(data, indent=4)
    f.write(json_data)
#print(json_data)
#time.sleep(120)
print("OK")
