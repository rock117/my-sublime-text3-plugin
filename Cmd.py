import sublime, sublime_plugin
import os
import os.path
class CmdCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		#os.system('cmd')
		filleName = self.view.file_name()
		drive = os.path.splitdrive(filleName)[0]
		drive = drive[0,len(drive)-1]
		dirNmae = os.path.dirname(filleName)
		print dirNmae
		#os.system("cmd /k cd /"+drive+" "+dirNmae);
		self.view.insert(edit, 0, "cmd /k cd /"+drive+" "+dirNmae+"\n")
		#os.system("cmd /k cd /d D:/Program Files");

