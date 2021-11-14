# navigate to a file offset
#
# Takes a file offset, converts it to a virtual address and navigates there. Note that the relative checkbox wont work but we use this dialog to get calculation feature

while True:
	offset=get_address_input("File offset: ", "Offset")
	if not offset:
		break
	if offset_to_vaddr(offset):
		vaddr = bv.get_address_for_data_offset(offset) 
		log_info("Navigating to file offset %x" % vaddr)
		bv.navigate(bv.view, vaddr)
		break