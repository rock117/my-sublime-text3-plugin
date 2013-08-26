my-sublime-text3-plugin
=======================

my sublime text3 plugins collection
1. how to write a sublime text3 plugin
1-1. write a python file, for example Cmd.py, bellow is the content

import sublime, sublime_plugin
import os
class CmdCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		#self.view.insert(edit, 0, "Hello, World!")
		os.startfile('cmd')
		
2. install the written plugin
   save the Cmd.py to sublime home package directory, for mine, 
   its location is C:\Users\ke\AppData\Roaming\Sublime Text 3\Packages\User

3. restart your sublime text3
   after restart, it works.
