# Notification Forwarder(For Android emulators)

A simple **toy** application that reads notifications from specified apps using the adb interface and display them on your PC desktop using pop-ups.

Suitable for scenarios in which common notification syncing apps won't work due to NAT on android emulators(e.g BlueStacks)

## Install & Run

### Install dependencies

```
pip install -r requirements.txt
```

### Run

```
python server.py
```
or 

```
server.exe
```
(For prebuilt windows binaries)

## Config

Config the application via `config.ini`. 


## License Information

The project is released under the MIT license. See LICENSE.txt for the license text.

The project uses the following libraries and includes compiled binaries of them in the released, prebuilt binaries:

- [Plyer](https://github.com/kivy/plyer) fron kivy. plyer is released under the MIT license. The original license text is reproduced in `NOTICE.txt`

- [adb_shell](https://github.com/JeffLIrion/adb_shell) from Jeff Irion. adb_shell is released under Apache 2.0 license. The original license text is reproduced in `NOTICE.txt`

