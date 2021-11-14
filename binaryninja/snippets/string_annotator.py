# annotate inline strings that are assembled via one byte moves/pushes
#
annotation=""
for instruction in current_basic_block.get_disassembly_text():
	if instruction.address >= current_selection[0] and instruction.address < current_selection[1]:
		address = instruction.address
		value = instruction.tokens[-1].value
		operand = instruction.tokens[-1].operand
		type = IntegerDisplayType.CharacterConstantDisplayType
		current_function.set_int_display_type(address, value, operand, type)
		annotation += chr(instruction.tokens[-1].value)
log_info("Adding comment for string: %s" % annotation)
current_function.set_comment_at(current_selection[0], annotation)
