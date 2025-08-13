import pyautogui as pg


async def get_win_title():
    active_window = pg.getActiveWindow()
    if active_window:
        return active_window.title
    else:
        return None
