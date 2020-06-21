# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialogDeleteAccount.ui'
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


class Ui_dialogDeleteAccount(object):
    def setupUi(self, dialogDeleteAccount):
        if not dialogDeleteAccount.objectName():
            dialogDeleteAccount.setObjectName(u"dialogDeleteAccount")
        dialogDeleteAccount.resize(486, 148)
        self.gridLayout_2 = QGridLayout(dialogDeleteAccount)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.comboChooseAccount = QComboBox(dialogDeleteAccount)
        self.comboChooseAccount.addItem("")
        self.comboChooseAccount.setObjectName(u"comboChooseAccount")

        self.gridLayout.addWidget(self.comboChooseAccount, 1, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 50, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.buttonDeleteAccount = QPushButton(dialogDeleteAccount)
        self.buttonDeleteAccount.setObjectName(u"buttonDeleteAccount")

        self.gridLayout_4.addWidget(self.buttonDeleteAccount, 1, 1, 1, 1)

        self.buttonCancel = QPushButton(dialogDeleteAccount)
        self.buttonCancel.setObjectName(u"buttonCancel")

        self.gridLayout_4.addWidget(self.buttonCancel, 1, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(300, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer, 1, 0, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_4, 0, 1, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_3, 3, 0, 1, 1)

        self.label = QLabel(dialogDeleteAccount)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 1, 1, 1)


        self.retranslateUi(dialogDeleteAccount)

        QMetaObject.connectSlotsByName(dialogDeleteAccount)
    # setupUi

    def retranslateUi(self, dialogDeleteAccount):
        dialogDeleteAccount.setWindowTitle(QCoreApplication.translate("dialogDeleteAccount", u"Delete Account", None))
        self.comboChooseAccount.setItemText(0, QCoreApplication.translate("dialogDeleteAccount", u"NoAccountSaved", None))

        self.buttonDeleteAccount.setText(QCoreApplication.translate("dialogDeleteAccount", u"Delete", None))
        self.buttonCancel.setText(QCoreApplication.translate("dialogDeleteAccount", u"Cancel", None))
        self.label.setText(QCoreApplication.translate("dialogDeleteAccount", u"Choose an account to delete", None))
    # retranslateUi

