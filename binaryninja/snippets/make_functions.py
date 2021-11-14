# make functions in selection
#
# Will create multiple functions in a background thread across the selected region using the default architecture

class FunctionTask(BackgroundTaskThread):
    def __init__(self, bv, selection):
        BackgroundTaskThread.__init__(self, "Finding functions...", False)
        self.bv = bv
        self.selection = selection

    def run(self):
        self.bv.begin_undo_actions()
        for addr in range(self.selection[0], self.selection[1]):
            if len(self.bv.get_functions_containing(addr)) == 0:
                self.bv.create_user_function(addr)
                self.bv.update_analysis_and_wait()
        self.bv.commit_undo_actions()

FunctionTask(bv, current_selection).start()