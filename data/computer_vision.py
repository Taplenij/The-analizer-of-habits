from PIL import ImageGrab
import asyncio
import pytesseract
import logging
import re

log = logging.getLogger('computer_vision')
log.setLevel(logging.DEBUG)
ch = logging.StreamHandler()

formatter = logging.Formatter(
    fmt='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

ch.setFormatter(formatter)
log.addHandler(ch)

class ComputerVision:
    SOC_NET = ['discord', 'tiktok', 'snapchat', 'youtube',
               'viber', 'facebook', 'vk',
               'telegram', 'instagram']
    TEXT = None

    async def read_text_from_win(self):
        try:
            await asyncio.sleep(2)
            image = ImageGrab.grab(bbox=(200, 40, 1500, 70))
            image.save('test.jpg')
            self.TEXT = pytesseract.image_to_string(image)
        except KeyboardInterrupt:
            log.info('Shutting down')

    async def active_win_info(self):
        if not self.TEXT:
            log.info('Text is empty')
        else:
            find_text = re.findall(r'(?:\w+\.)+\w+', self.TEXT)
            find_text = (' '.join(find_text)).split('.')[1]
            log.info(find_text)
            if find_text in self.SOC_NET:
                log.info(f'Found SOC NET {find_text}')
            else:
                log.info(f'Found TEXT {find_text}')
