# save HLIL
#
# DEPRECATED IN FAVOR OF "export to text" snippet

def filtername(name):
	return "".join(x for x in name if x.isalnum() or x in ["_", "-"])

choice = get_choice_input("Save all functions or just current?", "choices", ["All", "Current"])


if (choice == 0):
	import os
	fname = os.path.splitext(os.path.basename(bv.file.filename))[0]
	folder = get_directory_name_input("Where to save decompilation:").decode('utf-8')
	for fn in bv.functions:
		source = '\n'.join(map(str, fn.hlil.root.lines))
		output = os.path.join(folder, filtername(fn.name) + ".txt")
		try:
			with open(output, 'w') as f:
				f.write(source)
			log_info(f"Dumped {fn.name} to {output}")
		except:
			log_error(f"Unable to save {output}")
if (choice == 1):
	source = '\n'.join(map(str, current_function.hlil.root.lines))
	while True:
		output = get_save_filename_input("Source filename:", "txt", "%s.txt" % filtername(current_function.name))
		if output == None:
			msg = "No file specified."
			interaction.show_message_box(msg, msg)
			break
		try:
			with open(output, "w") as f:
				f.write(source)
		except:
			msg = "Save failed. Try again?"
			if not interaction.show_message_box(msg, msg, buttons=MessageBoxButtonSet.YesNoButtonSet):
				break

