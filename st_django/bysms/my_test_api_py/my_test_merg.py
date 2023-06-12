import requests,pprint
# 用户列表
response = requests.get('http://localhost:80/api/mgr/customers?action=list_customer')
pprint.pprint(response.json())
# 添加用户
payload = {
    'action':'add_customer',
    'data':{
        "name": "武汉市桥西医院",
        "phonenumber": "13345679934",
        "address": "武汉市桥西医院北路"
    }
}
response = requests.post('http://localhost:80/api/mgr/customers',
              json=payload)
pprint.pprint(response.json())
# 更新用户
# 查看效果
response = requests.get('http://localhost:80/api/mgr/customers?action=list_customer')
pprint.pprint(response.json())

