import requests
import json
from datetime import datetime
from weather.search_prefecture import Search_prefecture

class View_weather_report(Search_prefecture):
    def __init__(self):
        # Search_prefectureクラスを継承して最初に都道府県を設定
        super().__init__()
        # 設定した都道府県の天気予報を取得
        self.weather_report = requests.get(f'https://www.jma.go.jp/bosai/forecast/data/forecast/{self.prefecture_code}.json').json()
        self.weather_report_overview = requests.get(f'https://www.jma.go.jp/bosai/forecast/data/overview_forecast/{self.prefecture_code}.json').json()

        # 概要を表示
        print('--------------------------------------------------------------')
        print(self.weather_report_overview['text'].replace('\n\n', '\n'))
        print('--------------------------------------------------------------')
        
        print()



    # 現在の天気予報
    def weather_now(self):
        # 最新のデータ更新日を取得
        get_time = self.weather_report[0]['timeSeries'][0]['timeDefines'][0]
        get_time = datetime.fromisoformat(get_time).strftime("%Y/%m/%d %H:%M" + "発表")
        print(get_time)
        print()


        # 地方ごとに天気と風向きを表示
        for area in self.weather_report[0]['timeSeries'][0]['areas']:
            print('-----------------------------------------------------------------------------------------------------')
            print(f'{area['area']['name']}      天気 : {area['weathers'][0].replace('　', ' '): <50}        風 : {area['winds'][0].replace('　', ' ')}')
        print('-----------------------------------------------------------------------------------------------------')



    # 今後の気温予想
    def weather_weekly(self):
            
        # WeatherCodeと天気との対応表を読み込む
        with open(r'weather\weather_code_list.json', 'r', encoding='UTF-8') as f:
            weather_code_list_dict = json.load(f)
            
        # 一日毎に予報を表示 当日分は飛ばす
        for i, date in enumerate(self.weather_report[1]['timeSeries'][0]['timeDefines'][1:6], 1):
            print('----------------------------------------------------')
            print(datetime.fromisoformat(date).strftime('%Y/%m/%d'))
            print(f'予想最低気温: {self.weather_report[1]['timeSeries'][1]['areas'][0]['tempsMin'][i]}度', end = ' | ')
            print(f'予想最高気温: {self.weather_report[1]['timeSeries'][1]['areas'][0]['tempsMax'][i]}度', end = ' | ')
            print(f'天気: {weather_code_list_dict[self.weather_report[1]['timeSeries'][0]['areas'][0]['weatherCodes'][i]][3]} ')
        print('-----------------------------------------------------------------------------------------------------')