# new file from selection
#
# Opens the current selections contents into a new file

import tempfile
from binaryninjaui import UIContext

def get_selected_data():
	#remove when snippets implements this first-class
	return bv.read(current_selection[0], current_selection[1]-current_selection[0])

def openFile(filename):
	ctx = UIContext.activeContext()
	ctx.openFilename(filename)

temp = tempfile.NamedTemporaryFile(delete=False)
buf = get_selected_data()
log_info(f"Writing {len(buf)} bytes to {temp.name}")
temp.write(get_selected_data())
temp.close()
execute_on_main_thread_and_wait(lambda: openFile(temp.name))