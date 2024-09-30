from abc import *
from PIL import Image, ImageDraw

class Generator:
    def __init__(self, base_color, pattern_color1, pattern_color2):
        # 下地の色
        self.base_color = base_color

        # 柄の色 2つ目はダイヤ柄のみ使用
        self.pattern_color1 = pattern_color1
        self.pattern_color2 = pattern_color2

        # ベースの画像を生成
        self.image = Image.new("RGB", (256, 256), (base_color))

        self.draw = ImageDraw.Draw(self.image)

    @abstractmethod
    def process(self):
        pass