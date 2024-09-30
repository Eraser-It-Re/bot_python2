from rgb_slider import RGB_slider_GUI
# from check_pattern import Generate_check_pattern
# from diamond_pattern import Generate_diamond_pattern
# from plaid_pattern import Generate_plaid_pattern

class Image_generator:
    def __init__(self):
        print('どの柄を生成しますか？')
        print('【1】市松模様 | 【2】ダイヤ柄 | 【3】チェック柄')
        while True:
            try:
                choice = int(input('>> '))
                if choice != 1 <= 3:
                    raise ValueError
                break
            except ValueError:
                print('適切な整数を入力してください')

        base_color = RGB_slider_GUI('下地')
        print(base_color.main())
        # if choice == 1

main = Image_generator()


