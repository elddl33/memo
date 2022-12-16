import json
import requests

user = 'srv_doos01'
password = 'Dsme001!'

database = 'demo'
table = 'doos01_monitor_stat'
#############################################################################
url_token = 'http://20.39.190.208:18080/oauth/token'
headers_token = {
    'accept': 'application/json',
    'Content-Type': 'application/x-www-form-urlencoded'
}
data = f'grant_type=&username={user}&password={password}&scope=&client_id=&client_secret='
response = requests.post(url_token, headers=headers_token, data=data)
response_json = json.loads(response.content)
token = response_json['access_token']

#############################################################################
headers = {
    'accept': 'application/json',
    'Authorization': f'Bearer {token}'
}

#############################################################################
# 날짜와 limit 부분 수정해서 사용
# 날짜는 UTC 날짜 기준임
#############################################################################
json_data = {
    "database": "demo",
    "table": "doos01_monitor_stat",
    "columns": "*",
    "fromDate": "20221216",
    "toDate": "20221216",
    "limit": 1,
    "orderBy": "desc",
    "orderByColumn": "ds_timestamp",
    "latest": "True"
}
url_getdata = 'http://20.39.190.208:18080/api/connections/query/hive/getdata'
response = requests.post(url_getdata, headers=headers, json=json_data)
result = json.loads(response.content)
print(result)