from PIL import Image, ImageDraw, ImageFont
import numpy
scale = 1
default_char = "abcdefghigklmnopqrstuvwxyz"


def picture_conversion(import_img, export_img=None, input_char="",pix_distance=""):
    img = Image.open(import_img)
    img_pix = img.load()
    img_width = img.size[0]
    img_height = img.size[1]

    canvas_array = numpy.ndarray((img_height*scale, img_width*scale, 3), numpy.uint8)
    canvas_array[:,:,:] = 255
    new_image = Image.fromarray(canvas_array)
    img_draw = ImageDraw.Draw(new_image)
    font = ImageFont.truetype("simsun.ttc", 10)
    if input_char == "":
        char_list = list(default_char)
    else:
        char_list = list(input_char)
    if pix_distance == "清晰":
        pix_distance=3
    elif pix_distance == "一般":
        pix_distance = 4
    elif pix_distance == "字符":
        pix_distance = 5
    pix_count = 0
    table_len = len(char_list)
    for y in range(img_height):
        for x in range(img_width):
            if x%pix_distance == 0 and y%pix_distance == 0:
                img_draw.text((x*scale, y*scale), char_list[pix_count%table_len],
                              img_pix[x, y], font)
                pix_count += 1
    if export_img is not None:
        new_image.save(export_img)
    return False
