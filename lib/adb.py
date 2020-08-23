import os
from string import Template
from random import randint


def os_execute(command):
    f = os.popen(command)
    return f.readlines()


def adb_devices():
    """
    获取设备列表
    :return:
    """
    command = "adb devices"
    """
    adb devices 命令如下， 第一行和最后一行是没用的
    List of devices attached
    dd1f1687	device
    
    """
    res = os_execute(command)[1:-1]
    devices = []
    for d in res:
        devices.append(d.split("\t")[0])
    return devices


def adb_wm_size(device):
    command_t = Template('adb -s ${device} shell wm size')
    command = command_t.substitute(device=device)
    res = os_execute(command)
    wm_size = res[0].split(':')[1].replace('\n', '').replace(' ', '').split('x')
    return int(wm_size[0]), int(wm_size[1])


def get_random_start_end(device):

    w, h = adb_wm_size(device)
    start_x = int(w / 10 * 8)
    start_y = int(h / 10 * 8)
    end_x = int(w / 10 * 8)
    end_y = int(h / 10 * 2)
    return start_x, start_y, end_x, end_y


def adb_swipe_up(device, speed=100):
    """
    向上滑动
    :param device:
    :param speed:
    :return:
    """
    start_x, start_y, end_x, end_y = get_random_start_end(device)
    adb_swipe(device, start_x, start_y, end_x, end_y)


def adb_swipe_down(speed=100):
    """
    向上滑动
    :param speed:
    :return:
    """
    start_x, start_y, end_x, end_y = get_random_start_end()
    adb_swipe(end_x, end_y, start_x, start_y)


def adb_swipe(device, start_x, start_y, end_x, end_y, speed=100):
    """
    模拟屏幕滑动
    :param device:
    :param start_x:
    :param start_y:
    :param end_x:
    :param end_y:
    :param speed:
    :return:
    """
    command_t = Template("adb -s ${device} shell input swipe ${start_x} ${start_y} ${end_x} ${end_y} ${speed}")
    command = command_t.substitute(device=device, start_x=start_x, start_y=start_y, end_x=end_x, end_y=end_y,
                                   speed=speed)
    os_execute(command)
