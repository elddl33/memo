import socket
from time import strftime
import json
import datetime
import requests


import kivy 
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.clock import Clock



#Builder.load_file('my.kv')
user = 'srv_doos01'
password = 'Dsme001!'

database = 'demo'
table = 'doos01_monitor_stat'


class MyLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyLayout, self).__init__(**kwargs)
        self.cols = 2
        #Clock.schedule_interval(self.update, 0.1)
    
    '''    
    def on_start(self):
        Clock.schedule_interval(self.update, 0.1)
    '''
    
    def check_time():   #현재시간 return  
        try:
            utc_time = datetime.datetime.utcnow()
            log_time = utc_time - datetime.timedelta(hours=-(int(times[0])),minutes=-(int(times[1])),seconds=-(int(times[2])))
        
        except:
            log_time = datetime.datetime.utcnow()
        
        return log_time 

    def api():
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
            "fromDate": MyLayout.check_time().strftime('%Y%m%d %H:%M:%S_%f')[:8],
            "toDate": MyLayout.check_time().strftime('%Y%m%d %H:%M:%S_%f')[:8],
            "limit": 1,
            "orderBy": "desc",
            "orderByColumn": "ds_timestamp",
            "latest": "True"
        }
        url_getdata = 'http://20.39.190.208:18080/api/connections/query/hive/getdata'
        response = requests.post(url_getdata, headers=headers, json=json_data)
        result = json.loads(response.content)
        print(result)

        return result
    
    
        
    
    def update(self, *args):
        
        self.pc_id = self.ids.text_input.text
        
        self.api_data = str(MyLayout.api())
        self.api_data_split = self.api_data.split(',')

        self.ds_timestamp = self.api_data_split[0].split(':')[1]
        self.pc_time = self.api_data_split[1].split(':')[1]
        self.latitude = self.api_data_split[2].split(':')[1]
        self.longitude = self.api_data_split[3].split(':')[1]
        self.wave_height = self.api_data_split[4].split(':')[1]
        self.wave_direction = self.api_data_split[5].split(':')[1]
        self.wave_freq = self.api_data_split[6].split(':')[1]
        self.ds_date = self.api_data_split[7].split(':')[1].split("'")[1]
        
        self.utc_time = datetime.datetime.fromtimestamp(int(self.ds_timestamp[:-3])).strftime('%Y_%m_%d %H_%M')
        self.log_time = datetime.datetime.fromtimestamp(int(self.pc_time[:-3])).strftime('%Y_%m_%d %H_%M')
        
        self.ids.desktop_id.text = self.pc_id
        self.ids.today_data.text = self.ds_date
        self.ids.DOOS_time_data.text = self.utc_time
        self.ids.PC_time_data.text = self.log_time
        self.ids.height_data.text = self.wave_height
        self.ids.period_data.text = self.wave_freq
        self.ids.direction_data.text = self.wave_direction
        self.ids.latitude_data.text = self.latitude
        self.ids.longitude_data.text = self.longitude
            

class MyApp(App):
    def build(self):
        return MyLayout()
        
        
    
if __name__ == '__main__':
    MyApp().run()