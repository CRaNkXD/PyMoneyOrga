# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogCreateNewAccount.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_dialogCreateNewAccount(object):
    def setupUi(self, dialogCreateNewAccount):
        if not dialogCreateNewAccount.objectName():
            dialogCreateNewAccount.setObjectName(u"dialogCreateNewAccount")
        dialogCreateNewAccount.resize(478, 336)
        self.buttonBox = QDialogButtonBox(dialogCreateNewAccount)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)
        self.inputAccountName = QLineEdit(dialogCreateNewAccount)
        self.inputAccountName.setObjectName(u"inputAccountName")
        self.inputAccountName.setGeometry(QRect(250, 113, 200, 20))
        self.labelAccountName = QLabel(dialogCreateNewAccount)
        self.labelAccountName.setObjectName(u"labelAccountName")
        self.labelAccountName.setGeometry(QRect(250, 72, 200, 35))
        self.inputInitialAmount = QLineEdit(dialogCreateNewAccount)
        self.inputInitialAmount.setObjectName(u"inputInitialAmount")
        self.inputInitialAmount.setGeometry(QRect(250, 180, 200, 20))
        self.labelFirstAmount = QLabel(dialogCreateNewAccount)
        self.labelFirstAmount.setObjectName(u"labelFirstAmount")
        self.labelFirstAmount.setGeometry(QRect(250, 139, 200, 34))
        self.buttonAddNewAccount = QPushButton(dialogCreateNewAccount)
        self.buttonAddNewAccount.setObjectName(u"buttonAddNewAccount")
        self.buttonAddNewAccount.setGeometry(QRect(44, 179, 200, 23))
#if QT_CONFIG(shortcut)
        self.labelAccountName.setBuddy(self.inputAccountName)
        self.labelFirstAmount.setBuddy(self.inputInitialAmount)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(dialogCreateNewAccount)
        self.buttonBox.clicked.connect(dialogCreateNewAccount.close)

        QMetaObject.connectSlotsByName(dialogCreateNewAccount)
    # setupUi

    def retranslateUi(self, dialogCreateNewAccount):
        dialogCreateNewAccount.setWindowTitle(QCoreApplication.translate("dialogCreateNewAccount", u"Create New Account", None))
        self.labelAccountName.setText(QCoreApplication.translate("dialogCreateNewAccount", u"Account name", None))
        self.labelFirstAmount.setText(QCoreApplication.translate("dialogCreateNewAccount", u"Starting amount of money", None))
        self.buttonAddNewAccount.setText(QCoreApplication.translate("dialogCreateNewAccount", u"Add new account", None))
    # retranslateUi

