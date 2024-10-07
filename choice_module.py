# 選択させる際の処理を簡略化するメソッド
def choice_num(is_can_quit, max_num, min_num=1, error_message='適切な整数を入力してください'):
    while True:
        try:
            choice = int(input('>> '))

            if not min_num <= choice <= max_num and (is_can_quit and choice != 9):
                raise ValueError
            
            return choice
        except ValueError:
            print(error_message)