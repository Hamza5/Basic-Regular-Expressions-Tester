# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI/bret.ui'
#
# Created: Sat Aug  2 21:37:28 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Window(object):
    def setupUi(self, Window):
        Window.setObjectName(_fromUtf8("Window"))
        Window.resize(511, 426)
        self.verticalLayout_3 = QtGui.QVBoxLayout(Window)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.RegExpGroupBox = QtGui.QGroupBox(Window)
        self.RegExpGroupBox.setObjectName(_fromUtf8("RegExpGroupBox"))
        self.formLayout_2 = QtGui.QFormLayout(self.RegExpGroupBox)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.RegExpLabel = QtGui.QLabel(self.RegExpGroupBox)
        self.RegExpLabel.setObjectName(_fromUtf8("RegExpLabel"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.RegExpLabel)
        self.RegExpLineEdit = QtGui.QLineEdit(self.RegExpGroupBox)
        self.RegExpLineEdit.setObjectName(_fromUtf8("RegExpLineEdit"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.RegExpLineEdit)
        self.TextLabel = QtGui.QLabel(self.RegExpGroupBox)
        self.TextLabel.setObjectName(_fromUtf8("TextLabel"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.TextLabel)
        self.RegExpButtonsLayout = QtGui.QHBoxLayout()
        self.RegExpButtonsLayout.setObjectName(_fromUtf8("RegExpButtonsLayout"))
        self.OpenFilePushButton = QtGui.QPushButton(self.RegExpGroupBox)
        self.OpenFilePushButton.setObjectName(_fromUtf8("OpenFilePushButton"))
        self.RegExpButtonsLayout.addWidget(self.OpenFilePushButton)
        self.ResetTextPushButton = QtGui.QPushButton(self.RegExpGroupBox)
        self.ResetTextPushButton.setObjectName(_fromUtf8("ResetTextPushButton"))
        self.RegExpButtonsLayout.addWidget(self.ResetTextPushButton)
        self.formLayout_2.setLayout(3, QtGui.QFormLayout.FieldRole, self.RegExpButtonsLayout)
        self.TextEdit = QtGui.QPlainTextEdit(self.RegExpGroupBox)
        self.TextEdit.setObjectName(_fromUtf8("TextEdit"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.TextEdit)
        self.verticalLayout_3.addWidget(self.RegExpGroupBox)
        self.PositionsGroupBox = QtGui.QGroupBox(Window)
        self.PositionsGroupBox.setEnabled(False)
        self.PositionsGroupBox.setObjectName(_fromUtf8("PositionsGroupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.PositionsGroupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.StartPositionLabel = QtGui.QLabel(self.PositionsGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StartPositionLabel.sizePolicy().hasHeightForWidth())
        self.StartPositionLabel.setSizePolicy(sizePolicy)
        self.StartPositionLabel.setObjectName(_fromUtf8("StartPositionLabel"))
        self.horizontalLayout.addWidget(self.StartPositionLabel)
        self.StartPositionSpinBox = QtGui.QSpinBox(self.PositionsGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StartPositionSpinBox.sizePolicy().hasHeightForWidth())
        self.StartPositionSpinBox.setSizePolicy(sizePolicy)
        self.StartPositionSpinBox.setMaximum(9999)
        self.StartPositionSpinBox.setObjectName(_fromUtf8("StartPositionSpinBox"))
        self.horizontalLayout.addWidget(self.StartPositionSpinBox)
        self.EndPositionLabel = QtGui.QLabel(self.PositionsGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.EndPositionLabel.sizePolicy().hasHeightForWidth())
        self.EndPositionLabel.setSizePolicy(sizePolicy)
        self.EndPositionLabel.setObjectName(_fromUtf8("EndPositionLabel"))
        self.horizontalLayout.addWidget(self.EndPositionLabel)
        self.EndPositionSpinBox = QtGui.QSpinBox(self.PositionsGroupBox)
        self.EndPositionSpinBox.setMaximum(9999)
        self.EndPositionSpinBox.setObjectName(_fromUtf8("EndPositionSpinBox"))
        self.horizontalLayout.addWidget(self.EndPositionSpinBox)
        self.SelectionPushButton = QtGui.QPushButton(self.PositionsGroupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SelectionPushButton.sizePolicy().hasHeightForWidth())
        self.SelectionPushButton.setSizePolicy(sizePolicy)
        self.SelectionPushButton.setObjectName(_fromUtf8("SelectionPushButton"))
        self.horizontalLayout.addWidget(self.SelectionPushButton)
        self.verticalLayout_3.addWidget(self.PositionsGroupBox)
        self.tabWidget = QtGui.QTabWidget(Window)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.MatchesTab = QtGui.QWidget()
        self.MatchesTab.setObjectName(_fromUtf8("MatchesTab"))
        self.verticalLayout = QtGui.QVBoxLayout(self.MatchesTab)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.MatchesLayout = QtGui.QHBoxLayout()
        self.MatchesLayout.setObjectName(_fromUtf8("MatchesLayout"))
        self.MatchesLimitLabel = QtGui.QLabel(self.MatchesTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MatchesLimitLabel.sizePolicy().hasHeightForWidth())
        self.MatchesLimitLabel.setSizePolicy(sizePolicy)
        self.MatchesLimitLabel.setObjectName(_fromUtf8("MatchesLimitLabel"))
        self.MatchesLayout.addWidget(self.MatchesLimitLabel)
        self.MatchesLimitSpinBox = QtGui.QSpinBox(self.MatchesTab)
        self.MatchesLimitSpinBox.setEnabled(False)
        self.MatchesLimitSpinBox.setMinimum(1)
        self.MatchesLimitSpinBox.setObjectName(_fromUtf8("MatchesLimitSpinBox"))
        self.MatchesLayout.addWidget(self.MatchesLimitSpinBox)
        self.NoMatLimitCheckBox = QtGui.QCheckBox(self.MatchesTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NoMatLimitCheckBox.sizePolicy().hasHeightForWidth())
        self.NoMatLimitCheckBox.setSizePolicy(sizePolicy)
        self.NoMatLimitCheckBox.setChecked(True)
        self.NoMatLimitCheckBox.setObjectName(_fromUtf8("NoMatLimitCheckBox"))
        self.MatchesLayout.addWidget(self.NoMatLimitCheckBox)
        self.GroupsCheckBox = QtGui.QCheckBox(self.MatchesTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.GroupsCheckBox.sizePolicy().hasHeightForWidth())
        self.GroupsCheckBox.setSizePolicy(sizePolicy)
        self.GroupsCheckBox.setObjectName(_fromUtf8("GroupsCheckBox"))
        self.MatchesLayout.addWidget(self.GroupsCheckBox)
        self.verticalLayout.addLayout(self.MatchesLayout)
        self.MatchesTreeView = QtGui.QTreeView(self.MatchesTab)
        self.MatchesTreeView.setObjectName(_fromUtf8("MatchesTreeView"))
        self.verticalLayout.addWidget(self.MatchesTreeView)
        self.MatchesButtonsLayout = QtGui.QHBoxLayout()
        self.MatchesButtonsLayout.setObjectName(_fromUtf8("MatchesButtonsLayout"))
        self.FindMatchesPushButton = QtGui.QPushButton(self.MatchesTab)
        self.FindMatchesPushButton.setEnabled(False)
        self.FindMatchesPushButton.setDefault(True)
        self.FindMatchesPushButton.setObjectName(_fromUtf8("FindMatchesPushButton"))
        self.MatchesButtonsLayout.addWidget(self.FindMatchesPushButton)
        self.ResetMatPushButton = QtGui.QPushButton(self.MatchesTab)
        self.ResetMatPushButton.setObjectName(_fromUtf8("ResetMatPushButton"))
        self.MatchesButtonsLayout.addWidget(self.ResetMatPushButton)
        self.verticalLayout.addLayout(self.MatchesButtonsLayout)
        self.tabWidget.addTab(self.MatchesTab, _fromUtf8(""))
        self.ReplaceTab = QtGui.QWidget()
        self.ReplaceTab.setObjectName(_fromUtf8("ReplaceTab"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.ReplaceTab)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.ReplacementsLayout = QtGui.QHBoxLayout()
        self.ReplacementsLayout.setObjectName(_fromUtf8("ReplacementsLayout"))
        self.ReplacementsLimitLabel = QtGui.QLabel(self.ReplaceTab)
        self.ReplacementsLimitLabel.setObjectName(_fromUtf8("ReplacementsLimitLabel"))
        self.ReplacementsLayout.addWidget(self.ReplacementsLimitLabel)
        self.ReplacementsLimitSpinBox = QtGui.QSpinBox(self.ReplaceTab)
        self.ReplacementsLimitSpinBox.setEnabled(False)
        self.ReplacementsLimitSpinBox.setMinimum(1)
        self.ReplacementsLimitSpinBox.setObjectName(_fromUtf8("ReplacementsLimitSpinBox"))
        self.ReplacementsLayout.addWidget(self.ReplacementsLimitSpinBox)
        self.NoRepLimitCheckBox = QtGui.QCheckBox(self.ReplaceTab)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NoRepLimitCheckBox.sizePolicy().hasHeightForWidth())
        self.NoRepLimitCheckBox.setSizePolicy(sizePolicy)
        self.NoRepLimitCheckBox.setChecked(True)
        self.NoRepLimitCheckBox.setObjectName(_fromUtf8("NoRepLimitCheckBox"))
        self.ReplacementsLayout.addWidget(self.NoRepLimitCheckBox)
        self.verticalLayout_2.addLayout(self.ReplacementsLayout)
        self.ReplacementsTextBrowser = QtGui.QTextBrowser(self.ReplaceTab)
        self.ReplacementsTextBrowser.setObjectName(_fromUtf8("ReplacementsTextBrowser"))
        self.verticalLayout_2.addWidget(self.ReplacementsTextBrowser)
        self.ReplaceButtonsLayout = QtGui.QHBoxLayout()
        self.ReplaceButtonsLayout.setObjectName(_fromUtf8("ReplaceButtonsLayout"))
        self.ReplacePushButton = QtGui.QPushButton(self.ReplaceTab)
        self.ReplacePushButton.setEnabled(False)
        self.ReplacePushButton.setDefault(True)
        self.ReplacePushButton.setObjectName(_fromUtf8("ReplacePushButton"))
        self.ReplaceButtonsLayout.addWidget(self.ReplacePushButton)
        self.ResetRepPushButton = QtGui.QPushButton(self.ReplaceTab)
        self.ResetRepPushButton.setObjectName(_fromUtf8("ResetRepPushButton"))
        self.ReplaceButtonsLayout.addWidget(self.ResetRepPushButton)
        self.verticalLayout_2.addLayout(self.ReplaceButtonsLayout)
        self.tabWidget.addTab(self.ReplaceTab, _fromUtf8(""))
        self.verticalLayout_3.addWidget(self.tabWidget)
        self.RegExpLabel.setBuddy(self.RegExpLineEdit)
        self.TextLabel.setBuddy(self.TextEdit)
        self.StartPositionLabel.setBuddy(self.EndPositionSpinBox)
        self.EndPositionLabel.setBuddy(self.StartPositionSpinBox)
        self.MatchesLimitLabel.setBuddy(self.MatchesLimitSpinBox)
        self.ReplacementsLimitLabel.setBuddy(self.ReplacementsLimitSpinBox)

        self.retranslateUi(Window)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Window)
        Window.setTabOrder(self.tabWidget, self.RegExpLineEdit)
        Window.setTabOrder(self.RegExpLineEdit, self.TextEdit)

    def retranslateUi(self, Window):
        Window.setWindowTitle(_translate("Window", "Basic Regular Expression Tester", None))
        self.RegExpGroupBox.setTitle(_translate("Window", "Regular expresion and text", None))
        self.RegExpLabel.setText(_translate("Window", "Regular ex&pression", None))
        self.TextLabel.setText(_translate("Window", "Te&xt", None))
        self.OpenFilePushButton.setText(_translate("Window", "L&oad text from file", None))
        self.ResetTextPushButton.setText(_translate("Window", "R&eset text", None))
        self.PositionsGroupBox.setTitle(_translate("Window", "Starting and stoping positions", None))
        self.StartPositionLabel.setText(_translate("Window", "Start at position", None))
        self.EndPositionLabel.setText(_translate("Window", "Stop at position", None))
        self.SelectionPushButton.setText(_translate("Window", "From all the text", None))
        self.MatchesLimitLabel.setText(_translate("Window", "Results limit", None))
        self.NoMatLimitCheckBox.setText(_translate("Window", "&No limit", None))
        self.GroupsCheckBox.setText(_translate("Window", "Sho&w matched groups", None))
        self.FindMatchesPushButton.setText(_translate("Window", "Find &matches", None))
        self.ResetMatPushButton.setText(_translate("Window", "Rese&t results", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.MatchesTab), _translate("Window", "&Find matches", None))
        self.ReplacementsLimitLabel.setText(_translate("Window", "Replacements limit", None))
        self.NoRepLimitCheckBox.setText(_translate("Window", "&No limit", None))
        self.ReplacePushButton.setText(_translate("Window", "Search and &replace", None))
        self.ResetRepPushButton.setText(_translate("Window", "Rese&t results", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ReplaceTab), _translate("Window", "&Search and replace", None))

