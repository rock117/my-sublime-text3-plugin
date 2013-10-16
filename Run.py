import sublime, sublime_plugin
import os
import os.path
import subprocess
class RunCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		#os.system('cmd')
		filleName = self.view.file_name()
		dirNmae = os.path.dirname(filleName)
		os.chdir(dirNmae)
		basename = os.path.basename(filleName)
		if(filleName.endswith('.pl')):
			subprocess.Popen(['perl',basename])
		elif(filleName.endswith('.py')):
			subprocess.Popen(['python',basename])
		else:
			os.system('chrome '+basename)	




