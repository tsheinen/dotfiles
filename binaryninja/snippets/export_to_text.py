# export to text
# 
# Can export IL and assembly forms for the current function or the entire binary

import os
import io

def valid_filename(s):
	s = s.strip().replace(' ', '_')
	return re.sub(r'(?u)[^-\w.]', '', s)

def filtername(name):
	return "".join(x for x in name if x.isalnum() or x in ["_", "-"])

def fnsource(fn, form):
	if form == "HLIL":
		return ''.join(["\t" + x + "\n" for x in map(str, fn.hlil.root.lines)])
	if form == "MLIL":
		return ''.join(["\t" + x + "\n" for x in map(str, fn.mlil.instructions)])
	if form == "LLIL":
		return ''.join(["\t" + x + "\n" for x in map(str, fn.llil.instructions)])
	if form == "Assembly":
		return ''.join(["\t" + "".join(map(str, x[0])) + "\n" for x in fn.instructions])
	if form == "Assembly with offset":
		return ''.join([f'\t{x[1]:#04x}: {"".join(map(str, x[0]))}\n' for x in fn.instructions])

def overwrite(fname):
	if show_message_box("File exists", "File exists, delete and overwrite?", buttons=MessageBoxButtonSet.YesNoButtonSet) == MessageBoxButtonResult.YesButton:
		os.unlink(fname)
		return True
	else:
		return False

def main():
	#Maybe eventually add "Whole Binary" to include data from linear view
	all_or_func = ChoiceField("Scope?", ["All functions", "Current function"])
	asm_or_il = ChoiceField("Which form?", ["Assembly with offset", "Assembly", "LLIL", "MLIL", "HLIL"])
	folder = DirectoryNameField("Folder to save result", default_name=os.path.dirname(bv.file.filename))
	choices = get_form_input(["Which would you like to export?\n\nNote that \"whole binary\" will only dump IL contained in functions when IL is selected", all_or_func, asm_or_il, folder], "Export to text")
	
	if choices:
		current_only = all_or_func.result == 1
		form = asm_or_il.choices[asm_or_il.result]
		fname = os.path.splitext(os.path.basename(bv.file.filename))[0]
		if folder.result:
			if current_only:
				outputname = f"{os.path.join(folder.result, fname)}.{valid_filename(current_function.name)}.txt"
				if os.path.isfile(outputname):
					if not overwrite(outputname):
						log_warn("Stopping export to text due to existing file.")
						return
				log_info(f"Dumping {current_function.name} to {outputname}")
				with io.open(outputname, mode='w', encoding="utf-8") as f:
					f.write(fnsource(current_function, form))
			else:
				outputname = f"{os.path.join(folder.result, fname)}.txt"
				if os.path.isfile(outputname):
					if not overwrite(outputname):
						log_warn("Stopping export to text due to existing file.")
						return

				with io.open(outputname, mode='w', encoding="utf-8") as f:
					for fn in bv.functions:
						log_info(f"Writing {fn.name}")
						f.write(f"\n{fn.name}: \n")
						f.write(fnsource(fn, form))
					log_info(f"Done dumping whole binary to {outputname}")

main()    