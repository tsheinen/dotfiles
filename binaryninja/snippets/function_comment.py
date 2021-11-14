# function comment
#
# The UI currently lacks a way to add a "function" based comment that will be repeated when the function is called

newcomment = get_text_line_input("Current value: " + current_function.comment, "Function plate comment")
if (newcomment):
  current_function.comment = newcomment
