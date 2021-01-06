# Notification Forwarder(For Android emulators)

[中文README](/README_CN.md)

A simple **toy** application that reads notifications from specified apps using the adb interface and display them on your PC desktop using pop-ups.

Suitable for scenarios in which common notification syncing apps won't work due to NAT on android emulators(e.g BlueStacks)

## Install & Run

### Install dependencies

```
pip3 install -r requirements.txt
```

### Run

```
python3 server.py
```
or 

```
server.exe
```
(For prebuilt windows binaries)

## Config

Config the application via `config.ini`. 

### Special Instructions for Bluestacks 4

As of today, Bluestacks isn't working well with notifications from Azur Lane.

If you have trouble getting notifications from Azur Lane(e.g no notifications in the notification bar at all), try turning off "Notification Mode" and "App Notification" and restarting Bluestacks. (Tested on Bluestacks 4.240 and 4.250)


## License Information

The project is released under the MIT license. See LICENSE.txt for the license text.

The project uses the following libraries and includes compiled binaries of them in the released, prebuilt binaries:

- [Plyer](https://github.com/kivy/plyer) fron kivy. plyer is released under the MIT license. The original license text is reproduced in `NOTICE.txt`

- [adb_shell](https://github.com/JeffLIrion/adb_shell) from Jeff Irion. adb_shell is released under Apache 2.0 license. The original license text is reproduced in `NOTICE.txt`