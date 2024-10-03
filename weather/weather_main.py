from weather.view_weather_report import View_weather_report



class Weather_viewer:
    def __init__(self):
        self.view_weather_report = View_weather_report()

    def choice_mode(self):
        while True:
            # try:
            print('【1】現在の天気を表示 | 【2】今後の天気を表示 | 【9】終了')
            choice = int(input('>> '))

            if choice == 1:
                self.view_weather_report.weather_now()
            elif choice == 2:
                self.view_weather_report.weather_weekly()
            elif choice == 3:
                print('天気予報を終了します')
                break