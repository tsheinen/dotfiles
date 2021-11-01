import importlib  
exec(open('/home/sky/dotfiles/gdbinit-gef.py','r').read(),{"__name__":""}) # i hate this

class InitStack (gdb.Command):

  def __init__ (self):
    super (InitStack, self).__init__ ("init-stack", gdb.COMMAND_USER)

  def invoke (self, arg, from_tty):
  	stack = [x for x in get_process_maps() if x.path == "[stack]"][0]
  	gdb.execute(f"set $rsp = {stack.page_end}")
  	gdb.execute(f"set $rbp = {stack.page_end}") # pray i only use this on 64 bit libs 


if __name__ == "__main__":

	InitStack()