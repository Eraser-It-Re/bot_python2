from PIL import Image, ImageDraw

def draw_square(x, y):
    return (x, y, x + 64, y + 64)

im = Image.new("RGB", (256, 256), (128, 128, 128))

draw = ImageDraw.Draw(im)


draw.regular_polygon((32, 32, 32), 4, 45, fill=(255, 255, 0))

im.show()