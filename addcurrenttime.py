import sublime
import sublime_plugin
import os
import datetime

class AddCurrentTimeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		#now_time = os.popen('date')
		week = {'0': '星期天', '1': "星期一", '2': '星期二', '3': '星期三', '4': '星期四', '5': '星期五', '6': '星期六'}
		today = week[datetime.datetime.now().strftime("%w")]

		self.view.run_command("insert_snippet",
			{

				"contents": datetime.datetime.now().strftime("%Y年 %m月 %d日 %H:%M:%S "+ today+" CST")

			}
		)
