# -*- coding: UTF-8 -*-

import keyboard
import pygetwindow as gw
import win32api


def get_work_area():
    """
    获取系统的工作区域大小，即除去任务栏后的可用屏幕大小。
    """
    hMonitor = win32api.MonitorFromPoint((0, 0))
    monitorInfo = win32api.GetMonitorInfo(hMonitor)
    workArea = monitorInfo["Work"]
    return workArea[2], workArea[3]  # 返回工作区的宽度和高度


def activate_window():
    """
    将当前已激活的窗口移动到屏幕中央。
    """
    # 获取工作区域大小
    screen_width, screen_height = get_work_area()
    active_window = gw.getActiveWindow()
    # 如果找到了已激活的窗口
    if active_window:
        window_title = active_window.title
        # window_handle = active_window._hWnd
        print(f"当前已激活的窗口标题：{window_title}")
        # print(f"窗口句柄：{window_handle}")

        new_left = (screen_width - active_window.width) // 2
        new_top = (screen_height - active_window.height) // 2

        # 移动当前窗口到屏幕中央，考虑任务栏
        active_window.moveTo(new_left, new_top)
        print(f"考虑任务栏后，窗口已移动到：{new_left}, {new_top}")
    else:
        print("没有找到已激活的窗口")


if __name__ == "__main__":
    # 绑定快捷键Ctrl+Shift+Alt+p
    keyboard.add_hotkey("ctrl+shift+alt+p", activate_window)

    # 保持程序运行，直到用户按Ctrl+Shift+Alt+Esc键决定停止
    keyboard.wait("ctrl+shift+alt+esc")
