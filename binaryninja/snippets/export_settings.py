# generate official settings documentation 
#
# Snippet that generates https://docs.binary.ninja/getting-started.html#all-settings

import json
from PySide2.QtGui import QGuiApplication
settings = json.loads(binaryninja.Settings().serialize_schema())
table = """|Category|Setting|Description|Type|Default|Scope|Key|
|---|---|---|---|---|---|---|
"""

excludeEnum = [ "analysis.unicode.blocks", "python.interpreter", "ui.theme"]
allscope = set(["SettingsProjectScope", "SettingsUserScope", "SettingsResourceScope"])

for category in settings:
	for setting in settings[category]['settings']:
		title = settings[category]['settings'][setting]['title']
		description = settings[category]['settings'][setting]['description']
		typ = settings[category]['settings'][setting]['type']
		key = settings[category]['settings'][setting]['key']
		default = settings[category]['settings'][setting]['default']
		if isinstance(default, list):
			default = "[" + ', '.join(["`%s`" % x for x in default]) + "]"
		else:
			default = f"`{str(default)}`"
		if default == "``":
			default = " ";
		print(settings[category]['settings'][setting])
		if 'ignore' in settings[category]['settings'][setting].keys():
			scope = allscope - set(settings[category]['settings'][setting]['ignore'])
		else:
			scope = allscope
		scope = "[" + ', '.join(["`%s`" % x for x in scope]) + "]"
		table += f"|{category}|{title}|{description}|`{typ}`|{default}|{scope}|<a id='{key}'>{key}</a>|\n"
		if settings[category]['settings'][setting].get("enum") and key not in excludeEnum:
			for idx, enum in enumerate(settings[category]['settings'][setting]["enum"]):
				if settings[category]['settings'][setting].get("enumDescriptions"):
					description = "  enum: " + settings[category]['settings'][setting]["enumDescriptions"][idx]
				else:
					description = " "
				table += f"| | |{description}|`enum`|`{enum}`| | |\n"

show_markdown_report("Settings Documentation", "Below table added to the clipboard:\n\n"+table)
log_info("Saving result to the clipboard.")
clip = QGuiApplication.clipboard()
clip.setText(table)