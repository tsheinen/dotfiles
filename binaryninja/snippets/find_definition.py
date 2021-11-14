# Find a variable definition from current selection
#

if uicontext.token.localVarValid:
	log_info("Found a localvar")
	varname = uicontext.token.token.text
	log_info(str(dir(uicontext)))
	log_info("-----\n")
	instrIndex = 0
else:
	log_warn("No variable selected")