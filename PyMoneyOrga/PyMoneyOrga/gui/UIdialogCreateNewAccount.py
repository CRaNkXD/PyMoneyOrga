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
        dialogCreateNewAccount.resize(401, 171)
        self.gridLayout_2 = QGridLayout(dialogCreateNewAccount)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.inputInitialBalance = QLineEdit(dialogCreateNewAccount)
        self.inputInitialBalance.setObjectName(u"inputInitialBalance")
        self.inputInitialBalance.setMinimumSize(QSize(300, 0))

        self.gridLayout.addWidget(self.inputInitialBalance, 3, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(dialogCreateNewAccount)
        self.buttonBox.setObjectName(u"buttonBox")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Close)
        self.buttonBox.setCenterButtons(False)

        self.gridLayout.addWidget(self.buttonBox, 5, 1, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.buttonAddNewAccount = QPushButton(dialogCreateNewAccount)
        self.buttonAddNewAccount.setObjectName(u"buttonAddNewAccount")

        self.gridLayout_3.addWidget(self.buttonAddNewAccount, 0, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(200, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 0, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_3, 5, 0, 1, 1)

        self.labelCurrency = QLabel(dialogCreateNewAccount)
        self.labelCurrency.setObjectName(u"labelCurrency")

        self.gridLayout.addWidget(self.labelCurrency, 2, 1, 1, 1)

        self.labelAccountName = QLabel(dialogCreateNewAccount)
        self.labelAccountName.setObjectName(u"labelAccountName")

        self.gridLayout.addWidget(self.labelAccountName, 0, 0, 1, 1)

        self.inputAccountName = QLineEdit(dialogCreateNewAccount)
        self.inputAccountName.setObjectName(u"inputAccountName")
        self.inputAccountName.setMinimumSize(QSize(300, 0))

        self.gridLayout.addWidget(self.inputAccountName, 1, 0, 1, 1)

        self.labelInitialBalance = QLabel(dialogCreateNewAccount)
        self.labelInitialBalance.setObjectName(u"labelInitialBalance")

        self.gridLayout.addWidget(self.labelInitialBalance, 2, 0, 1, 1)

        self.comboCurrency = QComboBox(dialogCreateNewAccount)
        self.comboCurrency.setObjectName(u"comboCurrency")

        self.gridLayout.addWidget(self.comboCurrency, 3, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 4, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 2)

#if QT_CONFIG(shortcut)
        self.labelAccountName.setBuddy(self.inputAccountName)
        self.labelInitialBalance.setBuddy(self.inputInitialBalance)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.inputAccountName, self.inputInitialBalance)
        QWidget.setTabOrder(self.inputInitialBalance, self.comboCurrency)
        QWidget.setTabOrder(self.comboCurrency, self.buttonAddNewAccount)

        self.retranslateUi(dialogCreateNewAccount)
        self.buttonBox.clicked.connect(dialogCreateNewAccount.close)

        QMetaObject.connectSlotsByName(dialogCreateNewAccount)
    # setupUi

    def retranslateUi(self, dialogCreateNewAccount):
        dialogCreateNewAccount.setWindowTitle(QCoreApplication.translate("dialogCreateNewAccount", u"Create New Account", None))
        self.buttonAddNewAccount.setText(QCoreApplication.translate("dialogCreateNewAccount", u"Add new account", None))
        self.labelCurrency.setText(QCoreApplication.translate("dialogCreateNewAccount", u"Currency", None))
        self.labelAccountName.setText(QCoreApplication.translate("dialogCreateNewAccount", u"Account name", None))
        self.labelInitialBalance.setText(QCoreApplication.translate("dialogCreateNewAccount", u"Initial balance", None))
    # retranslateUi

