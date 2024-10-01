from rgb_slider import RGB_slider_GUI
from check_pattern import Generate_check_pattern
from diamond_pattern import Generate_diamond_pattern
from plaid_pattern import Generate_plaid_pattern

class Image_generator:
    def __init__(self):
        print('どの柄を生成しますか？')
        print('【1】市松模様 | 【2】ダイヤ柄 | 【3】チェック柄')
        while True:
            try:
                choice = int(input('>> '))
                if not 1 <= choice <= 3:
                    raise ValueError
                break
            except ValueError:
                print('適切な整数を入力してください')

        # スライダーを呼び出し色を設定 決定を押したらスライダーのウィンドウを閉じる
        base_color_slider = RGB_slider_GUI('下地の色')
        base_color = base_color_slider.main()
        base_color_slider.close_window()

        pattern_color1_slider = RGB_slider_GUI('柄の色')
        pattern_color1 = pattern_color1_slider.main()
        pattern_color1_slider.close_window()

        if choice == 1:
            gen_image = Generate_check_pattern(base_color, pattern_color1)
            gen_image.process()
        elif choice == 2:

            # ダイヤ柄を選んだ場合のみ柄の色2を選択させる
            pattern_color2_slider = RGB_slider_GUI('2つ目の柄の色')
            pattern_color2 = pattern_color1_slider.main()
            pattern_color2_slider.close_window()

            gen_image = Generate_diamond_pattern(base_color, pattern_color1, pattern_color2)
            gen_image.process()
        elif choice == 3:
            gen_image = Generate_plaid_pattern(base_color, pattern_color1)
            gen_image.process()
            

main = Image_generator()


