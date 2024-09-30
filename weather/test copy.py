import requests
import json



weather_report = requests.get(f'https://www.jma.go.jp/bosai/forecast/data/forecast/060000.json')
print(type(weather_report))
weather_report_json = weather_report.json()
print(type(weather_report_json))

print(weather_report_json[0])
#weather_report_dict = json.loads(json.dumps(weather_report_json))


