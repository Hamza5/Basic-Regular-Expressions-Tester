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
import re
try :
	from PyQt4.QtGui import QApplication, QWidget, QFileDialog, QMessageBox, QTextEdit, QStandardItem, QStandardItemModel
	from PyQt4.QtCore import QObject, SIGNAL, Qt, QUrl
except ImportError :
	print("FATAL ERROR : PyQt4 library can not be loaded !", "You can not use the GUI of BRET, try using bret script without GUI", sep='\n', file=sys.stderr)
	sys.exit(1) # Fatal error.
app = QApplication(sys.argv)
try :
	from GUI.bret_gui import Ui_Window, _translate
	from script import bret
except ImportError as e :
	QMessageBox.critical(None, "FATAL ERROR", "<h3>"+e.msg.capitalize()+"</h3>" + "<p>"+_translate("Window", "Your copy of BRET may be broken", None)+"</p>")
	sys.exit(1)

class MainWindow(QWidget, Ui_Window):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.setupUi(self)
		self.matchesModel = QStandardItemModel(self.MatchesTreeView) # Model to be used in the 'Search and replace' tree view.
		self.MatchesTreeView.setModel(self.matchesModel)
		self.clipboard = QApplication.clipboard()
		if self.clipboard.text() : # If the clipboard contains text data :
			self.PasteTextPushButton.setEnabled(True) # Enable the 'Paste from clipboard' buttons.
			self.PasteURLPushButton.setEnabled(True)
		QObject.connect(self.PasteTextPushButton, SIGNAL("clicked()"), self.TextEdit.paste) # Paste the text from the clipboard to the text edit.
		QObject.connect(self.ResetTextPushButton, SIGNAL("clicked()"), self.TextEdit.clear) # Clear the text area when clicking on the 'Reset' button.
		QObject.connect(self.FilePathPushButton, SIGNAL("clicked()"), self.chooseFile) # Open the file dialog when clicking on the 'Load from file' button.
		QObject.connect(self.ResetFilePathPushButton, SIGNAL("clicked()"), self.FilePathLineEdit.clear)
		QObject.connect(self.PasteURLPushButton, SIGNAL("clicked()"), self.URLLineEdit.paste) # Paste the text from the clipboard to the URL line edit.
		QObject.connect(self.ResetURLPushButton, SIGNAL("clicked()"), self.URLLineEdit.clear) # Clear the URL line edit when clicking on the 'Reset' button.
		QObject.connect(self.NoMatchesLimitCheckBox, SIGNAL("toggled(bool)"), self.MatchesLimitSpinBox.setDisabled) # Enable/disable the matches limit spin box.
		QObject.connect(self.NoReplacementsLimitCheckBox, SIGNAL("toggled(bool)"), self.ReplacementsLimitSpinBox.setDisabled) # Same for the replacements limit spin box.
		QObject.connect(self.NoSplitsLimitCheckBox, SIGNAL("toggled(bool)"), self.SplitsLimitSpinBox.setDisabled) # Same for the splits limit spin box.
		QObject.connect(self.RegExpLineEdit, SIGNAL("textChanged(const QString&)"), self.lineEditChange) # Enable/disable 'Find matches', 'Search and replace' and 'Split text' buttons.
		QObject.connect(self.TextEdit, SIGNAL("textChanged()"), self.textEditChange) # Same for the text edit.
		QObject.connect(self.FilePathLineEdit, SIGNAL("textChanged(const QString&)"), self.lineEditChange) # Same for the file path edit.
		QObject.connect(self.URLLineEdit, SIGNAL("textChanged(const QString&)"), self.lineEditChange) # Same for the URL edit.
		QObject.connect(self.MethodTabWidget, SIGNAL("currentChanged(int)"), self.tabChange) # Same for the file path edit.
		QObject.connect(self.FindMatchesPushButton, SIGNAL("clicked()"), self.searchAndReplace)
		QObject.connect(self.ResetMatchesPushButton, SIGNAL("clicked()"), self.matchesModel.clear) # Clear the results of the match.
		QObject.connect(self.clipboard, SIGNAL("dataChanged()"), self.clipboardDataChanged) # Enable/disable the 'Paste from clipboard' buttons.

	def clipboardDataChanged(self):
		if self.clipboard.text() : # If the clipboard contains text data :
			self.PasteTextPushButton.setEnabled(True) # Enable the 'Paste from clipboard' buttons.
			self.PasteURLPushButton.setEnabled(True)
		else :
			self.PasteTextPushButton.setDisabled(True)
			self.PasteURLPushButton.setDisabled(True)

	def chooseFile(self):
		# Show the file dialog :
		filePath = ""
		fileDialog = QFileDialog(self)
		fileDialog.setAcceptMode(QFileDialog.AcceptOpen)
		fileDialog.setFileMode(QFileDialog.ExistingFile)
		fileDialog.setNameFilters([ _translate("Window", "Text files (*.txt)", None),
									_translate("Window", "XML files (*.xml)", None),
									_translate("Window", "HTML files (*.html)", None),
									_translate("Window", "CSV files (*.csv)", None),
									_translate("Window", "All files (*)", None)
									])
		if fileDialog.exec_():
			filePath = fileDialog.selectedFiles()[0]
		if filePath : # If the user clicked Open :
			self.FilePathLineEdit.setText(filePath)

	def tabChange(self, index):
		if index == 0 : # 'Input text' tab.
			notEmpty = bool((self.RegExpLineEdit.text() != '') and (self.TextEdit.toPlainText() != ''))
			self.FindMatchesPushButton.setEnabled(notEmpty) # Enable/disable 'Find matches' button according to the text.
			self.ReplacePushButton.setEnabled(notEmpty) # Same for 'Search and replace' button.
			self.SplitPushButton.setEnabled(notEmpty) # Same for 'Split text' button.
		elif index == 1 : # 'Load from file' tab.
			notEmpty = bool((self.RegExpLineEdit.text() != '') and (self.FilePathLineEdit.text() != ''))
			self.FindMatchesPushButton.setEnabled(notEmpty) # Enable/disable 'Find matches' button according to the file path.
			self.ReplacePushButton.setEnabled(notEmpty) # Same for 'Search and replace' button.
			self.SplitPushButton.setEnabled(notEmpty) # Same for 'Split text' button.
		elif index == 2 : # 'Load from URL' tab.
			notEmpty = bool((self.RegExpLineEdit.text() != '') and (self.URLLineEdit.text() != ''))
			self.FindMatchesPushButton.setEnabled(notEmpty) # Enable/disable 'Find matches' button according to the URL.
			self.ReplacePushButton.setEnabled(notEmpty) # Same for 'Search and replace' button.
			self.SplitPushButton.setEnabled(notEmpty) # Same for 'Split text' button.

	def textEditChange(self):
		self.tabChange(0)
	def lineEditChange(self, text):
		self.tabChange(self.MethodTabWidget.currentIndex())
	
	def verifiedRegExp(self):
		regexp = None
		try :
			ignoreCase = re.IGNORECASE if self.IgnoreCasePushButton.isChecked() else 0
			multiline = re.MULTILINE if self.MultiLinePushButton.isChecked() else 0
			pointAll = re.DOTALL if self.DotAllPushButton.isChecked() else 0
			ASCIIOnly = re.ASCII if self.ASCIIOnlyPushButton.isChecked() else 0
			regexp = re.compile(self.RegExpLineEdit.text(), flags = ignoreCase | multiline | pointAll | ASCIIOnly)
		except re.error as e: # Syntax errors in the RegExp.
			QMessageBox.warning(self, _translate("Window", "Invalid regular expression", None), "<h3>"+_translate("Window", "The regular expression you entred is invalid !", None)+"</h3><p>"+_translate("Window", "Cause : "+str(e), None)+"</p>")
			self.RegExpLineEdit.selectAll() # Select all the text in the RegExp line edit.
		return regexp # The valid RegExp or None.
	
	def loadTextFile(self): # Try to open and read the file :
		text = ''
		textFile = None
		try :
			textFile = open(filePath, 'r', encoding="utf-8")
			text =  textFile.read()
			return text # File content.
		except FileNotFoundError :
			# Show the error message dialog.
			QMessageBox.warning(self, _translate("Window", "File not found", None), "<h3>"+_translate("Window", "The selected file can not be found !", None)+"</h3><p>"+_translate("Window", "Please verify that the file exist", None)+"</p>")
		except PermissionError :
			QMessageBox.warning(self, _translate("Window", "Permission error", None), "<h3>"+_translate("Window", "You don't have the required permissions to open this file !", None)+"</h3><p>"+_translate("Window", "It seems that the owner of this file didn't give you the permission of reading", None)+"</p>")
		except UnicodeError :
			QMessageBox.warning(self, _translate("Window", "Invalid file", None), "<h3>"+_translate("Window", "The file is not a valid Unicode text file !", None)+"</h3><p>"+_translate("Window", "Maybe because the selected file is not a text file or it is corrupted", None)+"</p>")
		except OSError as e :
			QMessageBox.warning(self, _translate("Window", "Failed to use the selected file", None), "<h3>"+_translate("Window", "Can not open the selected file", None)+"</h3><p>"+e.strerror+"</p>")
		#except Exception :
			#QMessageBox.warning(self, _translate("Window", "Unknown error", None), "<h3>"+_translate("Window", "An error occurred", None)+"</h3><p>"+str(e)+"</p>")
		finally :
			if textFile : textFile.close() # Close the file if no error occurred.
	def loadURL(self): # Try to download and read the file :
		pass

	def searchAndReplace(self):
		pass
		#regexp = self.verifiedRegExp() 
		#if not regexp : return
		#self.matchesModel.clear()
		#matches = bret.search(regexp, self.TextEdit.document().toPlainText(), 0 if self.NoMatLimitCheckBox.isChecked() else self.MatchesLimitSpinBox.value(), self.StartPositionSpinBox.value(), self.EndPositionSpinBox.value()) 
		#self.matchesModel.setHorizontalHeaderLabels(['Match','From position','to position'])
		#for m in matches :
			#item = QStandardItem(m.group())
			#self.matchesModel.appendRow([item, QStandardItem(str(m.start())), QStandardItem(str(m.end()))])
			#if self.GroupsCheckBox.isChecked() :
				#for i in range(len(m.groups())) :
					#item.appendRow([QStandardItem(m.group(i+1)), QStandardItem(str(m.start(i+1))), QStandardItem(str(m.end(i+1)))])

window = MainWindow()
window.show()
sys.exit(app.exec_())
