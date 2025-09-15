from PIL import ImageGrab
import pytesseract
import time
import re


class ComputerVision:
    SOC_NET = ['discord', 'tiktok', 'snapchat', 'youtube',
               'viber', 'facebook', 'vk', 'telegram', 'instagram']
    TEXT = None

    def read_text_from_win(self):
        time.sleep(2)
        image = ImageGrab.grab(bbox=(200, 40, 1500, 70))
        image.save('test.jpg')
        self.TEXT = pytesseract.image_to_string(image)

    def active_win_info(self):
        pass

c = ComputerVision()
c.active_win_info()