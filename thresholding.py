from PIL import Image, ImageFilter

def thresholding(image_name):
    im = Image.open(image_name)
    pix = im.load()
    for w in range(im.width):
        for h in range(im.height):
            if pix[w, h][0] > 191:
                pix[w, h] = (255, 255, 255)
            else:
                pix[w, h] = (0, 0, 0)
    im.save(image_name, 'PNG')
    print(image_name + " has been succesfully modified.")