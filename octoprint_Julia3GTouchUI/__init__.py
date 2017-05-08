# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin

class Julia3GTouchUI(octoprint.plugin.StartupPlugin):
	def on_after_startup(self):
		self._logger.info("TouchUI Plugin Started")

	def get_update_information(self):
		return dict(
			Julia3GTouchUI=dict(
				displayName="Julia3GTouchUI",
				displayVersion=self._plugin_version,
				# version check: github repository
				type="github_release",
				user="FracktalWorks",
				repo="Julia3GTouchUI",
				current=self._plugin_version,

				# update method: pip
				pip="https://github.com/FracktalWorks/Julia3GTouchUI/archive/{target_version}.zip"
			)
		)


__plugin_name__ = "Julia3GTouchUI"
__plugin_version__ = "0.1.2"


def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = Julia3GTouchUI()

	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
	}


