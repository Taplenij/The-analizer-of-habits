import pyautogui as pg

active_window = pg.getActiveWindow()
if active_window:
    print(f'{active_window.title}')
else:
    print(f'No active window')
