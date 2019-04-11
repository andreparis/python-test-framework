import datetime
import inspect
import os
from Framework.core.property import Property

class LogTest:
	def __init__(self):
		pass

	@staticmethod
	def write(method, action, element, logname, level = "RUNNED"):
		now = datetime.datetime.now()
		currTime = str(now.strftime('%d-%m-%Y %H:%M:%S'))
		content = currTime+ " - " + method + " - " + level + " - " + action + " - " + element + "\r\n"		
		filename = logname + str(now.strftime("%d%m%Y"))+".txt"
		path = Property.PATH_LOG + filename
		if os.path.exists(path):
			file = open(path, "a", newline='')
		else: 
			file = open(path, "w+", newline='')	
		file.write(content)
		print(filename + " - "+content)
