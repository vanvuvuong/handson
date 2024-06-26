import pyautogui
from time import sleep

"""
Điều kiện chạy:
- cần mở hết các section trên udemy ra
- copy toàn bộ video của khóa học vào đây & thêm vào biến text_list
"""

CLEAR_ITEMS = (1877, 253)
DOWNLOAD_EXTENSION_BUTTON = (1870, 285)
DOWNLOAD_FILE_NAME = (1010, 550)
DOWNLOAD_AS = (1721, 336)
DOWNLOAD_NOW = (1403, 835)
UDEMY_FIRST_VIDEO = (1315, 267)
UDEMY_SECOND_VIDEO = (1315, 267 + 73)
VIDEO_NAME_BEGIN = (1163, 264)
VIDEO_NAME_LAST = (1430, 290)


def copy_video_name():
    pyautogui.moveTo(VIDEO_NAME_LAST)
    pyautogui.dragTo(VIDEO_NAME_BEGIN, button="left", duration=0.1)
    with pyautogui.hold("ctrl"):
        pyautogui.press("c")


def move_and_click(position: tuple):
    pyautogui.moveTo(position)
    pyautogui.click()


def change_name():
    with pyautogui.hold("ctrl"):
        pyautogui.press("a")

    with pyautogui.hold("ctrl"):
        pyautogui.press("v")
    pyautogui.press("home")
    with pyautogui.hold("ctrl"):
        pyautogui.press("right")
    pyautogui.press("delete")


def main(max_video: int):
    for index in range(max_video):
        SLEEP_TIME = 2
        move_and_click(UDEMY_FIRST_VIDEO)
        copy_video_name()
        sleep(SLEEP_TIME*5)
        move_and_click(DOWNLOAD_EXTENSION_BUTTON)
        sleep(SLEEP_TIME)
        move_and_click(DOWNLOAD_AS)
        sleep(SLEEP_TIME)
        change_name()
        sleep(SLEEP_TIME)
        move_and_click((600, 410))
        sleep(SLEEP_TIME)
        pyautogui.press("enter")
        sleep(SLEEP_TIME*5)
        # move_and_click(CLEAR_ITEMS)
        # sleep(SLEEP_TIME)
        move_and_click(UDEMY_SECOND_VIDEO)
        sleep(SLEEP_TIME)


main(8)
