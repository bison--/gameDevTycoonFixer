#!/usr/bin/env python

import subprocess
import os
import time

command = "ps ax | grep gamedev | grep working-directory"
searchForCommand = "--working-directory="
nothingFixed = True

while nothingFixed:
	process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
	os.waitpid(process.pid, 0)
	output = process.stdout.read()
	#print output
	# 17257 ?        Sl     0:15 /home/bison/Games/gamedevtycoon-1.3.1/gamedevtycoon --type=renderer --disable-device-orientation --enable-viewport --no-sandbox --lang=de-DE --nodejs --working-directory=/tmp/.org.chromium.Chromium.2Vyz5y --disable-accelerated-2d-canvas --disable-accelerated-video-decode --channel=17238.0.604442715
	if output == "" or (command in output and not searchForCommand in output):
		print("game not running, please start 'Game Dev Tycoon' ...")
	elif searchForCommand in output:
		outputParts = output.split(" ")
		
		for cmd in outputParts:
			if cmd.startswith(searchForCommand):
				workingPath = cmd.replace(searchForCommand, "")
				
				source = workingPath + "/images/superb/level2Desk.png"
				dest = workingPath + "/images/superb/level2desk.png"
				os.rename(source, dest)
				print("found what we were searching for and fixed it ;)")
				nothingFixed = False
				break
	else:
		print("Found unknown output:\n" + output)
	
	time.sleep(0.5)
