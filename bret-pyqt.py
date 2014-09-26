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

__appName__ = 'BRET'
__fullAppName__ = 'Basic Regular Expressions Tester'
__version__ = '0.4'

import sys
import re
from urllib.request import urlretrieve
from urllib.error import URLError
from os.path import join, dirname, realpath

try :
	from PyQt4.QtGui import QApplication, QWidget, QFileDialog, QMessageBox, QTextEdit, QStandardItem, QStandardItemModel, QAbstractItemView, QIcon, QMainWindow, QStatusBar
	from PyQt4.QtCore import QObject, SIGNAL, Qt
except ImportError :
	print("FATAL ERROR : PyQt4 library can not be loaded !", "You can not use the GUI of BRET, try using bret script without GUI", sep='\n', file=sys.stderr)
	sys.exit(1) # Fatal error.
app = QApplication(sys.argv)
try :
	from GUI.bret_gui import Ui_CentralWidget, _translate
	from script import bret
except ImportError as e :
	QMessageBox.critical(None, "FATAL ERROR", "<h3>"+e.msg.capitalize()+"</h3>" + "<p>Your copy of BRET may be broken</p>")
	sys.exit(1)

class CentralWidget(QWidget, Ui_CentralWidget):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.setupUi(self)
		self.DownloadProgressBar.hide()
		self.matchesModel = QStandardItemModel(self.MatchesTreeView) # Model to be used in the 'Find matches' tree view.
		self.MatchesTreeView.setModel(self.matchesModel)
		self.MatchesTreeView.setEditTriggers(QAbstractItemView.NoEditTriggers) # Prevent editing.
		self.MatchesTreeView.setSelectionMode(QAbstractItemView.ExtendedSelection) # Multiple selections allowed.
		self.splitsModel = QStandardItemModel(self.SplitResultsListView) # Model to be used in the 'Split text' list view.
		self.SplitResultsListView.setModel(self.splitsModel)
		self.SplitResultsListView.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.SplitResultsListView.setSelectionMode(QAbstractItemView.ExtendedSelection)
		self.clipboard = QApplication.clipboard() # Reference to the system clipboard.
		if self.clipboard.text() : # If the clipboard contains text data :
			self.PasteTextPushButton.setEnabled(True) # Enable the 'Paste from clipboard' buttons.
			self.PasteURLPushButton.setEnabled(True)
		self.c = 0
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
		QObject.connect(self.FindMatchesPushButton, SIGNAL("clicked()"), self.findMatches) # 'Find matches' button.
		QObject.connect(self.ResetMatchesPushButton, SIGNAL("clicked()"), self.resetMatches) # Clear the results of the match.
		QObject.connect(self.clipboard, SIGNAL("dataChanged()"), self.clipboardDataChanged) # Enable/disable the 'Paste from clipboard' buttons.
		QObject.connect(self.ResetReplacementsPushButton, SIGNAL("clicked()"), self.resetSearchAndReplace) # Clear the the 'Search and replace' text area and the replacements count label. 
		QObject.connect(self.ReplacePushButton, SIGNAL("clicked()"), self.searchAndReplace) # 'Search and replace' button.
		QObject.connect(self.ResetSplitPushButton, SIGNAL("clicked()"), self.resetSplitText) # Clear the the 'Split text' list view and the splits count label. 
		QObject.connect(self.SplitPushButton, SIGNAL("clicked()"), self.splitText) # 'Split text' button.
		QObject.connect(self.MatchesTreeView, SIGNAL("doubleClicked (const QModelIndex&)"), self.copyItem) # Copy content of an item in the matches tree view.
		QObject.connect(self.SplitResultsListView, SIGNAL("doubleClicked (const QModelIndex&)"), self.copyItem) # Copy content of an item in the splits list view.
		
	def clipboardDataChanged(self):
		if self.clipboard.text() : # If the clipboard contains text data :
			self.PasteTextPushButton.setEnabled(True) # Enable the 'Paste from clipboard' buttons.
			self.PasteURLPushButton.setEnabled(True)
		else :
			self.PasteTextPushButton.setDisabled(True)
			self.PasteURLPushButton.setDisabled(True)

	def chooseFile(self): # Open the file selection dialog and set the file path.
		filepath = QFileDialog.getOpenFileName(self,  _translate("CentralWidget", 'Open a text file file', None), filter='Text files (*.txt);;All files (*)', options=QFileDialog.ReadOnly)
		if filepath :
			self.FilePathLineEdit.setText(filepath)

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
		
	def resetMatches(self):
		self.NumberOfResultsLabel.clear()
		self.matchesModel.clear()
	def resetSearchAndReplace(self):
		self.ReplacementsPlainTextEdit.setPlainText('')
		self.NumberOfReplacementsLabel.clear()
	def resetSplitText(self):
		self.NumberOfSplitsLabel.clear()
		self.splitsModel.clear()
	def resetAll(self):
		self.resetMatches()
		self.resetSearchAndReplace()
		self.resetSplitText()
	
	def verifiedRegExp(self): # Return the valid RegExp or show an error message to the user.
		regexp = None
		try :
			ignoreCase = re.IGNORECASE if self.IgnoreCasePushButton.isChecked() else 0
			multiline = re.MULTILINE if self.MultiLinePushButton.isChecked() else 0
			pointAll = re.DOTALL if self.DotAllPushButton.isChecked() else 0
			ASCIIOnly = re.ASCII if self.ASCIIOnlyPushButton.isChecked() else 0
			regexp = re.compile(self.RegExpLineEdit.text(), flags = ignoreCase | multiline | pointAll | ASCIIOnly)
		except re.error as e: # Syntax errors in the RegExp.
			self.RegExpLineEdit.selectAll() # Select all the text in the RegExp line edit.
			QMessageBox.warning(self, _translate("CentralWidget", "Invalid regular expression", None), "<h3>"+_translate("CentralWidget", "The regular expression you entred is invalid !", None)+"</h3><p>"+_translate("CentralWidget", "Cause : "+str(e), None)+"</p>")
		finally :
			return regexp # The valid RegExp or None.
	
	def loadTextFile(self): # Try to open and read the file :
		text = ''
		textFile = None
		try :
			textFile = open(self.FilePathLineEdit.text(), 'r', encoding="utf-8")
			text =  textFile.read()
			textFile.close()
		except FileNotFoundError :
			# Show the error message dialog.
			QMessageBox.warning(self, _translate("CentralWidget", "File not found", None), "<h3>"+_translate("CentralWidget", "The selected file can not be found !", None)+"</h3><p>"+_translate("CentralWidget", "Verify that the file exist", None)+"</p>")
		except PermissionError :
			QMessageBox.warning(self, _translate("CentralWidget", "Permission error", None), "<h3>"+_translate("CentralWidget", "You don't have the required permissions to open this file !", None)+"</h3><p>"+_translate("CentralWidget", "It seems that the owner of this file didn't give you the permission of reading", None)+"</p>")
		except UnicodeError :
			QMessageBox.warning(self, _translate("CentralWidget", "Invalid file", None), "<h3>"+_translate("CentralWidget", "The file doesn't contain valid Unicode text !", None)+"</h3><p>"+_translate("CentralWidget", "Maybe because the selected file is not a text file or it is corrupted", None)+"</p>")
		except OSError as e :
			QMessageBox.warning(self, _translate("CentralWidget", "Failed to use the selected file", None), "<h3>"+_translate("CentralWidget", "Can not open the selected file !", None)+"</h3><p>"+e.strerror+"</p>")
		finally :
			return text # File content or empty.

	def loadURL(self): # Try to download and read the file :
		url = self.URLLineEdit.text()
		content = ""
		try :
			self.DownloadProgressBar.show()
			filepath, headers = urlretrieve(url, reporthook=self.updateProgressBar)
			file = open(filepath, encoding='utf-8')
			content = file.read()
			file.close()
		except UnicodeError : # Not a text file :
			QMessageBox.warning(self, _translate("CentralWidget", "Invalid downloaded file", None), "<h3>"+_translate("CentralWidget", "The file downloaded doesn't contain valid Unicode text !", None)+"</h3><p>"+_translate("CentralWidget", "Maybe because the URL doesn't point to a text file or the file is corrupted", None)+"</p>")
		except URLError as e : # Invalid URL or a connection problem :
			QMessageBox.warning(self, _translate("CentralWidget", "URL error", None), "<h3>"+_translate("CentralWidget", "Error occurred when using the URL !", None)+"</h3><p>Cause : "+str(e.reason)+"</p>")
		finally :
			self.DownloadProgressBar.hide()
			return content
	
	def updateProgressBar(self, chunk_number, chunk_size, total_size): # Used only as report hook function for loadURL.
		if chunk_number == 0 :
			self.DownloadProgressBar.setMaximum(total_size if total_size > 0 else 0)
		value = (chunk_number + 1) * chunk_size
		if value > total_size : value = total_size
		self.DownloadProgressBar.setValue(value)
	
	def getRegExpAndText(self):
		self.resetAll()
		regexp = self.verifiedRegExp() 
		if not regexp : return (None, None)
		index = self.MethodTabWidget.currentIndex() # 0 : from text / 1 : from file / 2 : from URL.
		matches = None
		content = ""
		if index == 0 :
			content = self.TextEdit.document().toPlainText()
		elif index == 1 :
			content = self.loadTextFile()
		else :
			content = self.loadURL()
		if not content : return (None, None)
		return (regexp, content)

	def findMatches(self):
		regexp, content = self.getRegExpAndText()
		if not regexp : return # Or if not content : return
		end = len(content)
		matches = bret.search(regexp, content, 0 if self.NoMatchesLimitCheckBox.isChecked() else self.MatchesLimitSpinBox.value(), 0, end)
		headers = [_translate("MatchesTreeView", 'Match', None), _translate("MatchesTreeView", 'From position', None), _translate("MatchesTreeView", 'to position', None)] if self.PositionsCheckBox.isChecked() else [_translate("MatchesTreeView", 'Match', None)]
		self.matchesModel.setHorizontalHeaderLabels(headers)
		for m in matches :
			item = QStandardItem(m.group())
			item.setToolTip(_translate("MatchesTreeView", "Double-click to copy", None))
			if self.PositionsCheckBox.isChecked() :
				startPositionItem = QStandardItem(str(m.start()))
				endPositionItem = QStandardItem(str(m.end()))
				self.matchesModel.appendRow([item, startPositionItem, endPositionItem])
			else :
				self.matchesModel.appendRow([item])
			if self.GroupsCheckBox.isChecked() :
				for i in range(len(m.groups())) :
					subgroupItem = QStandardItem(m.group(i+1))
					subgroupItem.setToolTip(_translate("MatchesTreeView", "Double-click to copy", None))
					if self.PositionsCheckBox.isChecked() :
						subgroupStartItem = QStandardItem(str(m.start(i+1)))
						subgroupEndItem = QStandardItem(str(m.end(i+1)))
						item.appendRow([subgroupItem, subgroupStartItem, subgroupEndItem])
					else :
						item.appendRow([subgroupItem])
		numberOfResults = len(matches)
		self.NumberOfResultsLabel.setText('<i>' + _translate("CentralWidget", 'Number of results returned :', None) + ' </i><b>' + str(numberOfResults) + '</b>')
		self.MatchesTreeView.expandAll()
		self.MatchesTreeView.resizeColumnToContents(0)
		
	def searchAndReplace(self):
		regexp, content = self.getRegExpAndText()
		if not regexp : return # Or if not content : return
		end = len(content)
		text, numberOfReplacements = bret.replace(regexp, content, 0 if self.NoReplacementsLimitCheckBox.isChecked() else self.ReplacementsLimitSpinBox.value(), 0, end, self.ReplacementTextLineEdit.text(), exact=False) 
		self.NumberOfReplacementsLabel.setText('<i>' + _translate("CentralWidget", 'Number of replacements made :', None) + ' </i><b>' + str(numberOfReplacements) + '</b>')
		self.ReplacementsPlainTextEdit.setPlainText(text)
		
	def splitText(self):
		regexp, content = self.getRegExpAndText()
		if not regexp : return # Or if not content : return
		end = len(content)
		strings = bret.split(regexp, content, 0 if self.NoSplitsLimitCheckBox.isChecked() else self.SplitsLimitSpinBox.value(), 0, end)
		self.NumberOfSplitsLabel.setText('<i>' + _translate("CentralWidget", 'Number of splits made :', None) + ' </i><b>' + str(len(strings)-1) + '</b>')
		for s in strings :
			item = QStandardItem(s)
			item.setToolTip(_translate("SplitResultsListView", "Double-click to copy", None))
			self.splitsModel.appendRow(item)
	
	def copyItem(self, modelIndex):
		self.clipboard.setText(modelIndex.data())
		
class MainWindow(QMainWindow):
	def __init__(self):
		super().__init__(parent=None)
		self.setWindowTitle(__fullAppName__)
		self.setWindowIcon(QIcon(join(dirname(realpath(__file__)),'GUI','BRET-128.png')))
		self.setCentralWidget(CentralWidget(self))
		self.setStatusBar(QStatusBar(self))

window = MainWindow()
window.show()
sys.exit(app.exec_())
