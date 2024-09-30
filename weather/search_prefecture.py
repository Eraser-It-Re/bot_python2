import requests

class Search_prefecture:
    def __init__(self):
        # エリア一覧を取得し、都道府県（とコードが独立している一部地域）の一覧を抽出
        self.prefectures_list = requests.get('https://www.jma.go.jp/bosai/common/const/area.json').json()['offices']
        # 自身のsearch関数で、ユーザーが指定した都道府県からエリアコードを取得
        self.prefecture_code = self.search()
        print(self.prefecture_code)

    # 都道府県を検索して対応するエリアコードを返す関数
    def search(self):

        while True:
            # 検索結果が複数存在した場合に、後で一つに絞るために都道府県名とエリアコードを保存
            hit_prefecture_name = [] 
            hit_prefecture_code = [] 
            search_keyword = input('都道府県/地方を検索します。検索キーワードを入力してください >>  ') # 検索キーワード設定

            # 検索キーワードで都道府県名一覧を検索 部分一致した都道府県はすべて記録
            for code, info in self.prefectures_list.items():
                if search_keyword in info['name']:
                    hit_prefecture_code.append(code)
                    hit_prefecture_name.append(info['name'])

            # 検索結果が2つ以上ある場合、候補から選択させる
            if len(hit_prefecture_code) > 2:
                print('検索結果が複数存在します。どの天気予報を表示しますか？')

                #候補一覧の表示
                for i, prefecture in enumerate(hit_prefecture_name, 1):
                    print(f'【{i}】{prefecture}', end=' | ')

                print()
                choice = int(input('>> ')) - 1

                # 選択した都道府県のエリアコードをchoice_prefecture_codeに代入 この変数を最後に返す
                choice_prefecture_code = hit_prefecture_code[choice]

            # 北海道・鹿児島・沖縄が選択された場合、エリアコードが複数あるので選択させる
            elif search_keyword in '北海道':
                prefecture_code_list = ('011000', '012000', '013000', '014030', '014100', '015000', '016000', '017000')
                print('北海道は地方別で表示されます。どちらを表示しますか？')
                print('【1】宗谷地方 | 【2】上川・留萌地方 | 【3】網走・北見・紋別地方 | 【4】十勝地方')
                print('【5】釧路・根室地方 | 【6】胆振・日高地方 | 【7】石狩・空知・後志地方 | 【8】渡島・檜山地方')
                choice_prefecture_code = prefecture_code_list[int(input('>> ')) - 1]

            elif search_keyword in '鹿児島県':
                print('奄美地方は鹿児島県本土とは別に表示されます。どちらを表示しますか？')
                prefecture_code_list = ('460100', '460040')
                print('【1】鹿児島県本土 | 【2】奄美地方')
                choice_prefecture_code = prefecture_code_list[int(input('>> ')) - 1]

            elif search_keyword in '沖縄県':
                print('沖縄県は地方別で表示されます。どちらを表示しますか？')
                prefecture_code_list = ('471000', '472000', '473000', '474000')
                print('【1】沖縄本島地方 | 【2】大東島地方 | 【3】宮古島地方 | 【4】八重山地方')
                choice_prefecture_code = prefecture_code_list[int(input('>> ')) - 1]

            # 見つからなかった場合やり直し
            elif len(hit_prefecture_code) == 0:
                print('検索結果が見つかりませんでした。もう一度入力してください')
                continue
            
            # 検索結果が一つだけだった場合、その都道府県のエリアコードを代入
            else:
                print(f'{hit_prefecture_name[0]}の天気予報を表示します')
                choice_prefecture_code = hit_prefecture_code[0]

            return choice_prefecture_code
