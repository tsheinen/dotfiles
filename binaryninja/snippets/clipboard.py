# copy location as offset
#
# copies the currently selected value as an offset from the base to the clipboard
# Was used to include offset as a module name, not needed now
# import os
# modulename=os.path.basename(bv.file.original_filename)
s = bv.get_segment_at(here)
offset=here - s.start

# Alternate implementation that copies as a file offset (requires above lines
#offset=s.data_offset + offset

clip = PySide2.QtGui.QGuiApplication.clipboard()
clip.setText('%x' % (offset))
