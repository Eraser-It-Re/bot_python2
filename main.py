import os
from image_gen.image_gen_main import Image_generator
from weather.weather_main import Weather_viewer


# main.pyのあるディレクトリをカレントディレクトリに
os.chdir(os.path.dirname(os.path.abspath(__file__)))

print('何をしますか？')
print('【1】天気予報を見る | 【2】柄の画像を生成する')

while True:
    try:
        choice = int(input('>> '))
        if not 1 <= choice <= 2:
            raise ValueError
        break
    except ValueError:
        print('適切な整数を入力してください')


 
"""
参考:


天気予報関連

1.【Python】気象庁のAPIから天気予報を取得する方法
https://python.joho.info/scraping/get-weather-forecast-jma/

2.気象庁JSONデータ
https://qiita.com/michan06/items/48503631dd30275288f7

3.気象庁JSON ファイルにある weatherCode 一覧
https://www.t3a.jp/blog/web-develop/weather-code-list/
※載っている対応表を修正してjsonとして使用

3.python3でループを指定箇所から任意回数にしたい
https://teratail.com/questions/30851

4.Python エスケープシーケンスを無効にする方法
https://aiacademy.jp/media/?p=3405

画像生成関連

1.Pythonの画像処理ライブラリPillow(PIL)の使い方
https://note.nkmk.me/python-pillow-basic/

2.[Python] Pillowで長方形を描画する
https://zenn.dev/wtkn25/articles/python-pillow-rectangle

3.Python, Pillowで円や四角、直線などの図形を描画
https://note.nkmk.me/python-pillow-imagedraw/

4.PIL/Pillowで高速にPhotoShopなどの描画モードを実装する
https://qiita.com/pashango2/items/3c99489ebccd468ab454
*ページ内で紹介されているImage4Layerモジュールは不使用

5.【Pillow】ImageDrawモジュールによる直線、四角、円、多角形描画
https://python-no-memo.blogspot.com/2020/05/pillowimagedraw.html

RGBスライダー関連

1.【完全独学Python】TkinterのScale（スライダー）はこれだけ覚えて！
https://yuya-blog.net/?p=342#toc3

2.【Python/tkinter】ウィジェットの配置(place)
https://imagingsolution.net/program/python/tkinter/widget_layout_place/

3.【Python応用】Tkinterでアプリ作成-Windowの固定、拡大、縮小の有効・無効化方法-
https://www.hobby-happymylife.com/%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0/python-programming/tkinter_window-size/

4.【Python】tkinter：ウィンドウを閉じるボタンが押された時の動作を変更
https://office54.net/python/tkinter/window-close-catch

その他

1. Pythonの相対パスimportを理解する
https://qiita.com/u943425f/items/bd94a30b52c9296e942d
"""