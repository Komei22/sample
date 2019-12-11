from PIL import Image
import math
import glob
import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-id', '--images-dir',
                        required=False, default="images")
    parser.add_argument('-o', '--output',
                        required=False, default="sprite.png")
    return parser.parse_args()


def generate_sprite_image(image_paths, output):
    grid = int(math.sqrt(len(image_paths)))+1
    height = 8192//grid
    width = 8192//grid
    sprite_image = Image.new(
        mode='RGB',
        size=(width*grid, height*grid),
        color=(0, 0, 0))

    for i in range(len(image_paths)):
        row = i // grid
        col = i % grid
        img_path = image_paths[i]
        img = Image.open(img_path)
        img = img.resize((height, width), Image.ANTIALIAS)
        row_loc = row*height
        col_loc = col*width
        sprite_image.paste(img, (col_loc, row_loc))
    sprite_image.save(output)


if __name__ == "__main__":
    args = parse_args()
    img_dir = args.images_dir
    output = args.output

    img_paths = glob.glob("{}/*".format(img_dir))
    print("images: {}".format(img_paths))

    generate_sprite_image(img_paths, output)
