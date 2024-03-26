## 定位窗口垂直居中

由于一直使用`macos`系统，有个窗口管理神器`Rectangle`有个功能就是让鼠标所在区域的窗口一键让该窗口垂直居中的功能，让我这种有强迫症的人而言太棒了，最近有个项目需在`Windows`下开发，没有了这个功能让开发索然无味，新开的app窗口位置不在居中位置就特别不舒服，在`macos`上我把窗口居中的快捷键加到了鼠标侧键的快捷键中，很自然的就能让所有窗口都垂直居中的显示在我面前，`Google`搜了N页在`Windows`下并没有这样功能的软件，好吧那就自己开发吧。

## 使用方法

### 鼠标所在窗口垂直居中

> 防止与其他快捷键冲突索性就设置了个很长的快捷键，反正能加到鼠标侧键中，也可自行修改源码。

`Ctrl+Shift+Alt+p`

### 退出应用

`ctrl+shift+alt+esc`

## 构建应用

```bash
pyinstaller --onefile --windowed --icon="icon.ico" --distpath="compiled" --name="窗口控制器" app.py
```

## 设置Windows开机自启

```
快捷键：Windows + R 打开运行窗口输入：shell:startup

将Build后的app复制到该目录即可
```

## License

This project is licensed under the MIT License - see the LICENSE file for details