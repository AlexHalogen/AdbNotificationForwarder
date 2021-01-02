# Notification Forwarder(For Azur Lane running on emulators)

A simple **toy** application that reads notifications from specified apps using the adb interface and display them on your PC desktop using pop-ups.

Suitable for scenarios in which common notification syncing apps won't work due to NAT used by android emulators(e.g BlueStacks)

## Install & Run

### Install depencies

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

Config the application in `config.ini`. 


## License Information

The project is released under the MIT license. See LICENSE.txt for full text of the license.

The project uses the following libraries
