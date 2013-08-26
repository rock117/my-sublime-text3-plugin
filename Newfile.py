import sublime, sublime_plugin
import os
class NewfileCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		os.chdir('C:/Users/ke/AppData/Roaming/Sublime Text 3/Packages/User')
		f = open('html.tmpl')
		html = f.read()
		f.close()
		self.view.insert(edit, 0, html)
