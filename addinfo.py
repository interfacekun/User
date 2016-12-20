import sublime
import sublime_plugin
import os

import datetime
import sublime_plugin
class AddInfoCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		fileName = os.path.basename(self.view.file_name())
		self.view.run_command("insert_snippet",
			{
				"contents": "\n--[[""\n"
				" * @brief: "+fileName+"\n\n"
				" * @author:	  kun si""\n"
				" * @date:	"  "%s"  %datetime.datetime.now().strftime("%Y-%m-%d") +"\n"
				"--]]\n\n"
			}
		)