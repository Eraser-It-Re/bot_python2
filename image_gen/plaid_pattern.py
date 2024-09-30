from PIL import Image, ImageDraw, ImageChops
from generator_abstract import Generator

#チェック柄を生成するクラス
class Generate_plaid_pattern(Generator):
    def __init__(self):
        super().__init__((255,255,255), (230,150,150), (0,0,0))

    def process(self):
        
        # 横線のみの素材画像を生成
        material_image1 = Image.new("RGB", (256, 256), (255, 255, 255))

        draw = ImageDraw.Draw(material_image1)

        for draw_pos in range(0, 257, 32):
            draw.line((0, draw_pos, 256, draw_pos), fill=(self.pattern_color1), width=16)

        # 縦線のみの素材画像を生成
        material_image2 = Image.new("RGB", (256, 256), (255, 255, 255))

        draw = ImageDraw.Draw(material_image2)

        for draw_pos in range(0, 257, 32):
            draw.line((draw_pos, 0, draw_pos, 256), fill=(self.pattern_color1), width=16)

        # 縦線と横線の画像を乗算モードで合成し、チェック柄を作る
        plaid = ImageChops.multiply(material_image1, material_image2)

        # 作ったチェック柄を下地の画像に乗算モードで合成
        self.image = ImageChops.multiply(self.image, plaid)
        self.image.show()

pattern = Generate_plaid_pattern()
pattern.process()