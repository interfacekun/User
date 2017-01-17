import sublime
import sublime_plugin
import os


class AddCurrentTimeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		now_time = os.popen('date').readlines()
		self.view.run_command("insert_snippet",
			{

				"contents": now_time

			}
		)
