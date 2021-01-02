import re


exp_start = re.compile(r"\s*NotificationRecord.*")
exp_title = re.compile(r"\s*android\.title=String \((.*)\)")
exp_text = re.compile(r"\s*android\.text=String \((.*)\)")
exp_time = re.compile(r"\s*mUpdateTimeMs=([0-9]*)")
exp_stop = re.compile(r"(\s*NotificationRecord)|(^\s*$)")
exp_pkg = re.compile(r"pkg=(.*)")

def parse_notifications(result):
	ret = []
	lines = result.split("\n")
	start = 0
	end = 0
	entry = False

	current = {}
	i = -1
	while True:
		i += 1
		if i >= len(lines):
			break
		line = lines[i]
		if entry:
			match_title = exp_title.match(line)
			match_text = exp_text.match(line)
			match_time = exp_time.match(line)
			terminate = exp_stop.match(line)         
			if terminate:
				i -= 1 # rewind 1 line back
				entry = False
				if not "time" in current:
					current["time"] = -1
				if "title" in current and "text" in current: # done parsing current entry
					ret.append(current)
				current = {}
				continue

			if match_title:
				current["title"] = match_title.group(1) # extras={...android.title=String ($1) ...}
			if match_text:
				current["text"] = match_text.group(1) # extras={...android.title=String ($1) ...}
			if match_time:
				current["time"] = int(match_time.group(1)) # mUpdateTimeMs=$1
				
		else:
			if exp_start.match(line): # found start of notification record
				entry = True
				s = line.strip().split(" ")
				if len(s) < 2:
					print("Adb NotificationRecord line parse error, line: %s" % line)
				else:
					pkg = s[1]
					match_pkg = exp_pkg.match(pkg)
					if match_pkg:
						current["pkg"] = match_pkg.group(1)
					else:
						current["pkg"] = None
	return ret