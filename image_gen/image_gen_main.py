import os
from image_gen.rgb_slider import RGB_slider_GUI
from image_gen.check_pattern import Generate_check_pattern
from image_gen.diamond_pattern import Generate_diamond_pattern
from image_gen.plaid_pattern import Generate_plaid_pattern

class Image_generator:
    def __init__(self):
        
        
        pattern_type = None # 後で柄の種類を代入する変数 画像保存時のファイル名に使用
        
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

        print('ウィンドウが開きます')
        os.system('pause')
        
        # スライダーを呼び出し下地と柄の色をそれぞれ設定 決定されたらスライダーのウィンドウを閉じる
        base_color_slider = RGB_slider_GUI('下地の色')
        base_color = base_color_slider.main()
        base_color_slider.close_window()

        pattern_color1_slider = RGB_slider_GUI('柄の色')
        pattern_color1 = pattern_color1_slider.main()
        pattern_color1_slider.close_window()

        # 選択によってgen_imageに代入するクラス（柄の種類）を変える
        if choice == 1:
            gen_image = Generate_check_pattern(base_color, pattern_color1)
            pattern_type = 'check'
            
        elif choice == 2:   

            # ダイヤ柄を選んだ場合のみ柄の色2を選択させる
            pattern_color2_slider = RGB_slider_GUI('2つ目の柄の色')
            pattern_color2 = pattern_color2_slider.main()
            pattern_color2_slider.close_window()

            gen_image = Generate_diamond_pattern(base_color, pattern_color1, pattern_color2)
            pattern_type = 'diamond'
            
        elif choice == 3:
            
            gen_image = Generate_plaid_pattern(base_color, pattern_color1)
            pattern_type = 'plaid'
        
        # 画像を生成
        image = gen_image.process()
        
        print('生成した画像を表示します')
        os.system('pause')
        image.show()

        # 画像の保存
        while True:
            if (is_saved := input('画像を保存しますか?(y/n) >> ')) == 'y':
                # ファイルが既に存在していた場合、連番で保存
                for num in range(100):
                    if not os.path.isfile(rf'saved_image/{pattern_type}_{str(num).zfill(2)}.png'):
                        image.save(rf'saved_image/{pattern_type}_{str(num).zfill(2)}.png')
                        print('画像の保存が完了しました')
                        break
                    # 99まで埋まっていた場合、保存は行わない
                    elif os.path.isfile(rf'saved_image/{pattern_type}_99.png'):
                        print('これ以上画像を保存できません')
                        break
            elif is_saved == 'n':
                pass
            else:
                print('y/nで指定してください')
                continue
            break    


