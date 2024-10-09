import requests

class Search_prefecture:
    def __init__(self):
        # エリア一覧を取得し、都道府県（とコードが独立している一部地域）の一覧を抽出
        self.prefectures_list = requests.get('https://www.jma.go.jp/bosai/common/const/area.json').json()['offices']
        # 自身のsearch関数で、ユーザーが指定した都道府県からエリアコードを取得
        self.prefecture_code = self.search()

    # 都道府県を検索して対応するエリアコードを返す関数
    def search(self):

        while True:
            # 検索結果が複数存在した場合に、後で一つに絞るために都道府県名とエリアコードを保存
            hit_prefecture_name = [] 
            hit_prefecture_code = [] 
            
            search_keyword = input('都道府県/地方を検索します。検索キーワードを入力してください >> ') 

            # 検索キーワードで都道府県名一覧を検索 部分一致した都道府県はすべて記録する
            for code, info in self.prefectures_list.items():
                if search_keyword in info['name']:
                    hit_prefecture_code.append(code)
                    hit_prefecture_name.append(info['name'])

            # 検索結果が2つ以上ある場合、候補から選択させる
            if len(hit_prefecture_code) > 2:
                print('検索結果が複数存在します。どの地域の天気予報を表示しますか？')

                #候補一覧の表示
                for i, prefecture in enumerate(hit_prefecture_name, 1):
                    print(f'【{i}】{prefecture}', end=' | ')

                while True:
                    try:
                        choice = int(input('>> ')) - 1
                        if not 0 <= choice <= len(hit_prefecture_name) - 1:
                            raise ValueError
                        break
                    except ValueError:
                        print('適切な整数を入力してください')

                # 選択した都道府県のエリアコードをchoice_prefecture_codeに代入 この変数を最後に返す
                choice_prefecture_code = hit_prefecture_code[choice]

            # 北海道・沖縄が選択された場合、エリアコードが複数あるので選択させる
            elif search_keyword in '北海道':
                prefecture_code_list = ('011000', '012000', '013000', '014100', '015000', '016000', '017000')
                print('北海道は地方別で表示されます。どちらを表示しますか？')
                print('【1】宗谷地方 | 【2】上川・留萌地方 | 【3】網走・北見・紋別地方 | 【4】釧路・根室・十勝地方')
                print('【5】胆振・日高地方 | 【6】石狩・空知・後志地方 | 【7】渡島・檜山地方')
                
                while True:
                    try:
                        choice_num = int(input('>> ')) - 1
                        if not 0 <= choice_num <= 6:
                            raise ValueError
                        choice_prefecture_code = prefecture_code_list[choice_num]
                        break
                    except ValueError:
                        print('適切な整数を入力してください')

            elif search_keyword in '沖縄県':
                print('沖縄県は地方別で表示されます。どちらを表示しますか？')
                prefecture_code_list = ('471000', '472000', '473000', '474000')
                print('【1】沖縄本島地方 | 【2】大東島地方 | 【3】宮古島地方 | 【4】八重山地方')
                
                while True:
                    try:
                        choice_num = int(input('>> ')) - 1
                        if not 0 <= choice_num <= 3:
                            raise ValueError
                        choice_prefecture_code = prefecture_code_list[choice_num]
                        break
                    except ValueError:
                        print('適切な整数を入力してください')

            # 検索にヒットしなかった場合やり直し
            elif len(hit_prefecture_code) == 0:
                print('検索結果が見つかりませんでした。もう一度入力してください')
                continue
            
            # 検索結果が一つだけだった場合、その都道府県のエリアコードを代入
            else:
                choice_prefecture_code = hit_prefecture_code[0]
            
            #表示用の都道府県名を設定する変数
            displayed_choice_prefecture_name = self.prefectures_list[choice_prefecture_code]['name']
            
            # 鹿児島県は奄美地方のコードが分かれているが、実際には鹿児島県のコードで奄美地方の情報も表示され、奄美地方のコードは指定しても何も取得できない
            # そのため奄美地方が選択された場合には鹿児島県のコードに置換する
            if choice_prefecture_code == '460040':
                choice_prefecture_code = '460100'
            # 同様の理由で北海道の十勝地方を釧路・根室地方のコードに置換
            elif choice_prefecture_code == '014030':
                choice_prefecture_code = '014100'
                
            # 表記も変更
            if choice_prefecture_code  == '460100':
                displayed_choice_prefecture_name = '鹿児島県'
            elif choice_prefecture_code == '014100':
                displayed_choice_prefecture_name = '釧路・根室・十勝地方'
                
            print(f'{displayed_choice_prefecture_name}の天気予報を表示します')
            return choice_prefecture_code
