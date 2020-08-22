from PIL import Image, ImageDraw, ImageOps
from pypasswords import hash_it
import os.path


def generate_image(keyword):

    image_path = f'home/static/images/profiles/{keyword}.jpg'
    if not os.path.isfile(image_path):
        print('generating')

        hashed_keyword = hash_it(keyword, hash_type='sha512')
        pre_ground = [int(char) // 4 for char in hashed_keyword if char.isdigit()][::2][:25]

        img = Image.new('RGB', (500, 500), color='white')
        draw = ImageDraw.Draw(img)

        ground = [[0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0]]
        colors = {
            1: 'black',
            2: 'blue',
            }

        counter = 0
        for i, line in enumerate(ground):
            for j, pixel in enumerate(line):
                ground[i][j] = pre_ground[counter]
                counter += 1

        for y, line in enumerate(ground):
            for x, pixel in enumerate(line):
                if pixel:
                    x_cord = x * 100
                    y_cord = y * 100
                    draw.rectangle([(x_cord, y_cord), (x_cord+100, y_cord+100)], fill=colors.get(pixel))

        final_img = Image.new('RGB', (1000, 1000))

        final_img.paste(img, (0, 0))
        final_img.paste(ImageOps.flip(img), (0, 500))
        final_img.paste(ImageOps.mirror(img), (500, 0))
        final_img.paste(ImageOps.flip(ImageOps.mirror(img)), (500, 500))

        final_img.save(image_path)
    return image_path
