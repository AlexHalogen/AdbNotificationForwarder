# Notification Forwarder(For Android emulators)

一个基于adb转发android通知至桌面的小工具，适用于由于NAT等网络原因无法使用传统通知转发应用(KDE Connect等)的场景(如bluestacks)

## 安装&运行

### 安装依赖

```
pip3 install -r requirements.txt
```

### 运行

```
python3 server.py
```

或者双击

```
server.exe
```

（适用于预编译过的程序）

## 配置

通过config.ini设置转发的包名、转发间隔、adb key所在位置、adb调试地址等

### 针对Bluestacks 4等和碧蓝航线的特殊设置

截至当前，Bluestacks 4和部分其他Android模拟器自带的通知转发功能会干扰本工具运作。

如果发生无法转发碧蓝航线通知的情况(如：模拟器通知栏内不显示碧蓝航线的通知), 请尝试关闭"通知模式"/"Notification Mode"和"应用通知"/"App Notification"开关并重启模拟器。 (已于Bluestacks 4.240 and 4.250测试)


## License Information

The project is released under the MIT license. See LICENSE.txt for the license text.

The project uses the following libraries and includes compiled binaries of them in the released, prebuilt binaries:

- [Plyer](https://github.com/kivy/plyer) fron kivy. plyer is released under the MIT license. The original license text is reproduced in `NOTICE.txt`

- [adb_shell](https://github.com/JeffLIrion/adb_shell) from Jeff Irion. adb_shell is released under Apache 2.0 license. The original license text is reproduced in `NOTICE.txt`