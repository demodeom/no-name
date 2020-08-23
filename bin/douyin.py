from lib.adb import adb_devices, adb_swipe_up
from random import randint
from time import sleep


def dou_yin():
    """
    获取设备列表
    向上活动
    :return:
    """

    while True:
        devices = adb_devices()
        for d in devices:
            adb_swipe_up(d)
        sleep(randint(6, 8))


if __name__ == '__main__':
    dou_yin()
