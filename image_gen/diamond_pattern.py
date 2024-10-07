from PIL import Image, ImageDraw
from image_gen.generator_abstract import Generator # 抽象クラスを継承

# ダイヤ柄を生成するクラス
class Generate_diamond_pattern(Generator):
    def __init__(self, base_color, pattern_color1, pattern_color2):
        super().__init__(base_color, pattern_color1)
        # ダイヤ柄のみ柄の色2を設定
        self.pattern_color2 = pattern_color2
        
    def process(self):
        
        # ダイヤ柄を2つの色で描画
        for pos_y in range(32, 256, 64):
            for pos_x in range(32, 256, 64):
                self.draw.regular_polygon((pos_x, pos_y, 32), 4, 45, fill=(self.pattern_color1))

            # 交互になるように柄の色2を描画
            for pos_x in range(pos_y - 192, 256, 128):
                self.draw.regular_polygon((pos_x, pos_y, 32), 4, 45, fill=(self.pattern_color2))

        return self.image
        # self.image.show()