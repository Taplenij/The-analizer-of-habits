from PIL import ImageGrab
import pytesseract as ts
import time

soc_net = ['discord', 'tiktok', 'snapchat', 'youtube',
           'viber', 'facebook', 'vk', 'telegram', 'instagram']


def read_text_from_win():
    time.sleep(2)
    image = ImageGrab.grab(bbox=(200, 40, 500, 70))
    image.save('test.jpg')
    text = ts.image_to_string(image)
    print(text)


def active_win_info():
    pass


read_text_from_win()
