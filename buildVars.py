# Build customizations
# Change this file instead of sconstruct or manifest files, whenever possible.

# Full getext (please don't change)
_ = lambda x : x

# Add-on information variables
addon_info = {
# add-on Name
	"addon_name" : "enhancedAria",
	# Add-on description
	# TRANSLATORS: Summary for this add-on to be shown on installation and add-on informaiton.
	"addon_summary" : _("Enhanced Aria"),
	# Add-on description
	# Translators: Long description to be shown for this add-on on installation and add-on information
	"addon_description" : _(""" This addon allows you to specify which Aria landmarks will be spoken when browsing a website.
It has support for extra aria landmarks which are not included by default in NVDA."""),
	# version
	"addon_version" : "2.8",
	# Author(s)
	"addon_author" : "Jose Manuel Delicado <jm.delicado@nvda.es>",
# URL for the add-on documentation support
	"addon_url" : "https://addons.nvda-project.org/addons/enhancedAria.en.html",
	"addon_docFileName" : "readme.html",
	# Minimum NVDA version supported (e.g. "2018.3")
	"addon_minimumNVDAVersion" : "2017.4.0",
	# Last NVDA version supported/tested (e.g. "2018.4", ideally more recent than minimum version)
	"addon_lastTestedNVDAVersion" : "2019.2.0",
	# Add-on update channel (default is stable or None)
	"addon_updateChannel" : None,
}


import os.path
from glob import glob

# Define the python files that are the sources of your add-on.
# You can use glob expressions here, they will be expanded.
pythonSources = ["addon/globalPlugins/*", "addon/*.py"]

# Files that contain strings for translation. Usually your python sources
i18nSources = pythonSources + ["buildVars.py"]

excludedFiles=[i[6:] for i in glob("addon/doc/*/*.md")+glob("addon/locale/*/LC_MESSAGES/*.po")]+[os.path.join("doc", "en", "readme.md")]
