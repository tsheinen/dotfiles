# read dword
# 
# Simple example showing how to read a dword at the current location

dword = int.from_bytes(bv.read(here, 4), "big" if bv.endianness == Endianness.BigEndian else "little")

clip = PySide2.QtGui.QGuiApplication.clipboard()
clip.setText('%x' % (dword))
