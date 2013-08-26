import sublime, sublime_plugin
import os
class CmdCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		#os.system('cmd')
		os.system("cmd /k cd /d D:/Program Files");

