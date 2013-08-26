my-sublime-text3-plugin
=======================

my sublime text3 plugins collection<br>
1. how to write a sublime text3 plugin<br>
1-1. write a python file, for example Cmd.py, bellow is the content<br>

import sublime, sublime_plugin<br>
import os<br>
class CmdCommand(sublime_plugin.TextCommand):<br>
	def run(self, edit):<br>
		#self.view.insert(edit, 0, "Hello, World!")<br>
		os.startfile('cmd')<br>
		
2. install the written plugin<br>
   save the Cmd.py to sublime home package directory, for mine, <br>
   its location is C:\Users\ke\AppData\Roaming\Sublime Text 3\Packages\User<br>

3. restart your sublime text3<br>
   after restart, it works.<br>
