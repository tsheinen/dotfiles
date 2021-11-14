# Simple PySide UI elements/testing
#
import binaryninjaui
from PySide2 import QtWidgets, QtGui, QtWidgets, QtCore

def basic():
	popout = QtWidgets.QDialog()
	popout.setWindowTitle("test popout1")
	popout.exec_()

def qpixmap():
	pixmap = QtGui.QPixmap("play-and-pause-button.png")
	mask = pixmap.createMaskFromColor(QtGui.QColor('black'), QtGui.Qt.MaskOutColor)
	pixmap.fill((QtGui.QColor('red')))
	pixmap.setMask(mask)
	window = QtWidgets.QDialog()
	window.setWindowTitle("View Image")
	label = QtWidgets.QLabel(window)
	label.setPixmap(pixmap)
	label.setGeometry(QtCore.QRect(10, 40, pixmap.width(), pixmap.height()))
	window.resize(pixmap.width()+20, pixmap.height()+100)
	window.exec_()

def qpixmap2():
	icon = QtGui.QIcon("play-and-pause-button.svg")
	button = QtWidgets.QPushButton(icon)
	msg_box = QtWidgets.QMessageBox()
	msg_box.setWindowTitle("Testing Icons")
	msg_box.exec_()

def colorize(img, color):
	pixmap = QtGui.QPixmap(img)
	mask = pixmap.createMaskFromColor(QtGui.QColor('black'), QtGui.Qt.MaskOutColor)
	pixmap.fill(color)
	pixmap.setMask(mask)
	return pixmap

def qicon():
	ico = QtGui.QIcon("play-and-pause-button.svg")
	ico2 = QtGui.QIcon(colorize(ico.pixmap(ico.actualSize(QtCore.QSize(1024, 1024))), QtGui.QColor('red')))
	msg_box = QtWidgets.QMessageBox()
	msg_box.setWindowTitle("Show Icon")
	button = QtWidgets.QPushButton(msg_box)
	button.setIcon(ico2)
	button.setText("PlayPause")
	msg_box.exec_()
 
#qpixmap2()
#qpixmap()
#basic()
qicon()

