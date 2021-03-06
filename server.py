import time
import os
import logging
import configparser
from datetime import datetime
from adb_shell.adb_device import AdbDeviceTcp, AdbDeviceUsb
from adb_shell.auth.sign_pythonrsa import PythonRSASigner
from plyer import notification
from adbparser import parse_notifications

'''
Global parameters
'''
packages = set()
interval = 10
address = ""
port = 0
privkey = os.path.join(os.path.expanduser("~"), ".android", "adbkey") # %HOME%/.android/adbkey
pubkey = privkey + ".pub"											  # %HOME%/.android/adbkey.pub


def main():
	parse_config()

	logging.basicConfig(level=logging.INFO)
	logger = logging.getLogger('main')
	logger.setLevel(logging.INFO)

	logger.info("Forwarding notifications for %s" % list(packages))

	device = connect()
	visited = set()
	while True:
		raw = device.shell("dumpsys notification --noredact")
		notifications = parse_notifications(raw)
		if packages:
			notifications = filter_package_names(notifications)

		notifications = filter_duplicate_notifications(notifications, visited)
		for n in notifications:
			logger.info("{pkg} [{time}] \"{title}\" \"{text}\"".format(time=datetime.fromtimestamp(n["time"]/1000), pkg=n["pkg"], title=n["title"], text=n["text"]))
			notification.notify(
				title=n["title"],
				message=n["text"],
				app_icon=None, 
				timeout=0,
				toast=True
			)
		time.sleep(interval)
		if len(visited) > 2*1000: # clear
			visited = set()

# Assumption: notifications have unique mUpdateTimeMs values
def filter_duplicate_notifications(notifications, visited):
	ret = []
	for n in notifications:
		if not n["time"] in visited:
			visited.add(n["time"])
			ret.append(n)

	return ret

def filter_package_names(notifications):
	result = filter(lambda n : n["pkg"] in packages, notifications)
	return list(result)

def connect():
	with open(privkey) as f:
		priv = f.read()
	with open(pubkey) as f:
		pub = f.read()

	signer = PythonRSASigner(pub, priv)
	device = AdbDeviceTcp(address, port, default_transport_timeout_s=9.)
	device.connect(rsa_keys=[signer], auth_timeout_s=0.1)
	return device

def parse_config():
	global packages, interval, address, port, privkey, pubkey

	config = configparser.ConfigParser()
	config.read("config.ini")
	section = config['config']
	if "adbprivkey" in section:
		privkey = section["adbprivkey"]
	if "adbpubkey" in section:
		pubkey = section["adbpubkey"]
	if "packages" in section:
		pkgs = section["packages"].split(",")
		packages = set(map(lambda x: x.strip(), pkgs))
	else:
		packages = set()

	address = section["address"]
	port = section.getint("port")
	interval = section.getint("interval")

if __name__ == "__main__":
	main()