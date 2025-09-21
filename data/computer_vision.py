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
    IS_SOC = False

    async def _read_text_from_win(self):
        try:
            image = ImageGrab.grab(bbox=(200, 40, 1500, 70))
            image.save('test.jpg')
            self.TEXT = pytesseract.image_to_string(image)
        except KeyboardInterrupt:
            log.info('Shutting down')

    async def active_win_info(self):
        try:
            log.info('Computer Vision started')
            await self._read_text_from_win()
            if not self.TEXT:
                log.info('Text is empty')
            else:
                find_text = re.findall(r'(?:\w+\.)+\w+', self.TEXT)
                find_text = (' '.join(find_text)).split('.')[1]
                self.TEXT = find_text
                log.info(self.TEXT)
                if self.TEXT in self.SOC_NET:
                    log.info(f'Found SOC NET {self.TEXT}')
                    self.IS_SOC = True
                else:
                    log.info(f'Found TEXT {self.TEXT}')
        except Exception as e:
            log.error(e)