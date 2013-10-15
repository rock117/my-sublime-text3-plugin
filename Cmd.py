import sublime, sublime_plugin
import os
import os.path
class CmdCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		#os.system('cmd')
 
		fileName = self.view.file_name()
		dirname = os.path.dirname(fileName)
		os.chdir(dirname)
		os.startfile('cmd')
		# drive = os.path.splitdrive(fileName)[0].replace(':','')
		# driveStr = "/"+drive+" "
		# if(drive=='C' or drive=='c'):
		# 	driveStr=''
		# #os.system("cmd /k cd /d D:/Program Files");
		# os.chdir('C:/Users/rhuang/AppData/Roaming/Sublime Text 3/Packages/User')
		# f = open('runcmd.bat', 'w')
		# f.write("cmd /k cd "+driveStr+dirname)
		# f.close()
		# os.startfile('runcmd.bat')

