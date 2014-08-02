#!/usr/bin/python3
# -*- coding: utf-8 -*-
#
#    Basic Regular Expressions Tester - Graphical User Interface
#    Copyright 2014 Hamza Abbad
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#

import sys
try :
	from PyQt4.QtGui import QApplication, QWidget, QFileDialog, QMessageBox, QTextEdit
	from PyQt4.QtCore import QObject, SIGNAL
except ImportError :
	print("FATAL ERROR : PyQt4 library can not be found !", "You can not use the GUI of BRET, try using bret script without GUI", sep='\n', file=sys.stderr)
	sys.exit(1) # Fatal error.
try :
	from GUI.bret_gui import Ui_Window, _translate
	import script.bret
except ImportError as e :
	print("FATAL ERROR :", e.name, "can not be found !\nYour copy of software may be broken", file=sys.stderr)
	sys.exit(1)
class MainWindow(QWidget, Ui_Window):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.setupUi(self)
		QObject.connect(self.ResetTextPushButton, SIGNAL("clicked()"), self.TextEdit.clear) # Clear the text area when clicking on the 'Reset' button.
		QObject.connect(self.OpenFilePushButton, SIGNAL("clicked()"), self.loadFile) # Open the file dialog when clicking on the 'Load from file' button.
		QObject.connect(self.NoMatLimitCheckBox, SIGNAL("toggled(bool)"), self.MatchesLimitSpinBox.setDisabled) # Enable/disable the matches limit spin box.
		QObject.connect(self.NoRepLimitCheckBox, SIGNAL("toggled(bool)"), self.ReplacementsLimitSpinBox.setDisabled) # Same for the replacements limit spin box.
		QObject.connect(self.TextEdit, SIGNAL("textChanged()"), self.textChange) # Enable/disable the positions group box and the 'Find matches' and the 'Search and replace' buttons.
		QObject.connect(self.SelectionPushButton, SIGNAL("clicked()"), self.useSelection) # Use the selection start and end positions.
		QObject.connect(self.TextEdit, SIGNAL("selectionChanged()"), self.selectionChange) # Change the selection push button text.
		QObject.connect(self.RegExpLineEdit, SIGNAL("textEdited(const QString&)"), self.textAndRegExpChange) # Enable/disable 'Find matches' and 'Search and replace' buttons by editing the text in the RegExp line edit.
		QObject.connect(self.TextEdit, SIGNAL("textChanged()"), self.textAndRegExpChange) # Same for the text edit.
	def loadFile(self):
		# Show the file dialog :
		filePath = ""
		fileDialog = QFileDialog(self)
		fileDialog.setAcceptMode(QFileDialog.AcceptOpen)
		fileDialog.setFileMode(QFileDialog.ExistingFile)
		fileDialog.setNameFilters([ _translate("Window", "Text files (*.txt)", None),
									_translate("Window", "All files (*)", None)
									])
		if fileDialog.exec_():
			filePath = fileDialog.selectedFiles()[0]
		if filePath : # If the user clicked Open :
			# Try to open and read the file :
			textFile = None
			try :
				textFile = open(filePath, 'r', encoding="utf-8")
				text =  textFile.read()
				self.TextEdit.insertPlainText(text) # Load the text and put it in the text area.
			except FileNotFoundError :
				# Show the error message dialog.
				QMessageBox.critical(self, _translate("Window", "File not found", None), _translate("Window", "The selected file can not be found !", None))
			except PermissionError :
				QMessageBox.critical(self, _translate("Window", "Permission error", None), _translate("Window", "You don't have the required permissions to open this file !", None))
			except UnicodeError :
				QMessageBox.warning(self, _translate("Window", "Invalid file", None), _translate("Window", "The file is not a valid Unicode text file !", None))
			except OSError as e :
				QMessageBox.critical(self, _translate("Window", "Failed to use the selected file", None), _translate("Window", "Can not open the selected file", None)+"\n"+e.strerror)
			finally :
				if textFile : textFile.close() # Close the file if no error occurred.
	def textChange(self):
		self.PositionsGroupBox.setDisabled(self.TextEdit.document().isEmpty()) # Disable the positions group box if the text edit is empty, enable it otherwise.
		# self.EndPositionSpinBox.setValue(self.TextEdit.document().characterCount()-1) # Set the end position on the last character.
	def textAndRegExpChange(self):
		self.FindMatchesPushButton.setEnabled(self.RegExpLineEdit.text() != '' and self.TextEdit.toPlainText() != '') # Enable/disable 'Find matches' button
		self.ReplacePushButton.setEnabled(self.RegExpLineEdit.text() != '' and self.TextEdit.toPlainText() != '') # Same for 'Search and replace' button.
			
	def useSelection(self):
		cursor = self.TextEdit.textCursor()
		if cursor.hasSelection() : # If there is some text selected :
			self.StartPositionSpinBox.setValue(cursor.selectionStart())
			self.EndPositionSpinBox.setValue(cursor.selectionEnd())
		else :
			self.StartPositionSpinBox.setValue(0)
			self.EndPositionSpinBox.setValue(self.TextEdit.document().characterCount()-1)
	def selectionChange(self):
		cursor = self.TextEdit.textCursor()
		if cursor.hasSelection() : # If there is some text selected :
			self.SelectionPushButton.setText(_translate("Window", "From selected text", None))
		else :
			self.SelectionPushButton.setText(_translate("Window", "From all the text", None))
app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec_())