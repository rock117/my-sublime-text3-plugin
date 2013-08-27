import sublime, sublime_plugin
import os
import os.path
class RunCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		#os.system('cmd')
		filleName = self.view.file_name()
		dirNmae = os.path.dirname(filleName)
		os.chdir(dirNmae)
		basename = os.path.basename(filleName)
		if(filleName.endswith('.pl')):
			os.system('perl '+basename)
		elif(filleName.endswith('.py')):
			os.system('python '+basename)
		else:
			os.system('chrome '+basename)	


