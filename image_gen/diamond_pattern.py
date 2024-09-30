from PIL import Image, ImageDraw
from generator_abstract import Generator

# ダイヤ柄を生成するクラス
class Generate_diamond_pattern(Generator):
    def __init__(self):
        super().__init__((255,255,255), (0,0,0), (255,0,0))
        
    def process(self):
        

        # ダイヤ柄を2つの色で描画
        for pos_y in range(32, 256, 64):
            for pos_x in range(32, 256, 64):
                self.draw.regular_polygon((pos_x, pos_y, 32), 4, 45, fill=(self.pattern_color1))

            for pos_x in range(pos_y - 128, 256, 128):
                self.draw.regular_polygon((pos_x, pos_y, 32), 4, 45, fill=(self.pattern_color2))


        self.image.show()

ichimatsu = Generate_diamond_pattern()
ichimatsu.process()