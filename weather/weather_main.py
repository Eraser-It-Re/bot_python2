from view_weather_report import View_weather_report



class Weather_viewer:
    def __init__(self):
        self.view_weather_report = View_weather_report()

    def choice_mode(self):
        print('【1】現在の天気を表示 | 【2】今後の気温予想を表示')
        choice = int(input('>> '))

        if choice == 1:
            self.view_weather_report.weather_now()
        elif choice == 2:
            self.view_weather_report.weather_weekly()

Weather_viewer().choice_mode()