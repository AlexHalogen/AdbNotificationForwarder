from distutils.core import setup
import py2exe

setup(
	console=['server.py'],
	data_files=[(".", ["config.ini", "NOTICE.txt", "README.md", "LICENSE.txt"])],
	options={
		"py2exe": {
			"packages": ["plyer", "adb_shell"],
		}
	})