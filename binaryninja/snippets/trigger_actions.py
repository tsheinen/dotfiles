# trigger actions
#
# Trigger actions in the UI Action system via a plugin or snippet 
# Use the command-palette (CMD/CTL-P) to find action descriptions
# Not compatible with headless of course

from binaryninjaui import UIActionHandler, DockHandler

def triggerAction(action):
	handler = UIActionHandler().actionHandlerFromWidget(DockHandler.getActiveDockHandler().parent())
	handler.executeAction(action)

action="About..."
execute_on_main_thread_and_wait(lambda: triggerAction(action))