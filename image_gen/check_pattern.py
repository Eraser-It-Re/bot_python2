from PIL import Image, ImageDraw
from image_gen.generator_abstract import Generator

# 市松模様を生成するクラス
class Generate_check_pattern(Generator):
        
    def process(self):
        
        # 描画する正方形の終点を相対的に指定し、サイズの設定を簡略化するメソッド
        def draw_square(x, y):
            return (x, y, x + 64, y + 64)
        
        

        # 正方形の始点一覧
        positions = [(64, 0), (192, 0), (0, 64), (128, 64), (64,128), (192, 128), (0, 192), (128, 192)]

        # positionsでfor文を回し正方形を描画
        for pos in positions:
            self.draw.rectangle(draw_square(*pos), fill=(self.pattern_color1))
            
        return self.image