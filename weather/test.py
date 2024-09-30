import requests
import json



weather_report = requests.get(f'https://www.jma.go.jp/bosai/forecast/data/forecast/060000.json')
print(type(weather_report))
#print(f'weather_report: {weather_report}')
weather_report_json = weather_report.json()
weather_report_load = json.load(weather_report)
print(f'weather_report_load: {weather_report_load}')
print(f'weather_report_json: {weather_report_json}')
weather_report_json_dump = json.dumps(weather_report_json)
print(f'weather_report_json_dump: {weather_report_json_dump}')
weather_report_json_dump = json.dumps(weather_report_json)
weather_report_json_load = json.loads(weather_report_json_dump)
print(weather_report_json_load)

   
#weather_report_dict = json.loads(json.dumps(weather_report_json))


