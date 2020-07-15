# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PyMoneyOrgaGui.ui'
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


class Ui_PyMoneyOrgaGui(object):
    def setupUi(self, PyMoneyOrgaGui):
        if not PyMoneyOrgaGui.objectName():
            PyMoneyOrgaGui.setObjectName(u"PyMoneyOrgaGui")
        PyMoneyOrgaGui.resize(1168, 775)
        PyMoneyOrgaGui.setMinimumSize(QSize(0, 0))
        PyMoneyOrgaGui.setMaximumSize(QSize(16777215, 16777215))
        self.actionCreate_New_Account = QAction(PyMoneyOrgaGui)
        self.actionCreate_New_Account.setObjectName(u"actionCreate_New_Account")
        self.actionDeleteAccount = QAction(PyMoneyOrgaGui)
        self.actionDeleteAccount.setObjectName(u"actionDeleteAccount")
        self.actionDelete_Account = QAction(PyMoneyOrgaGui)
        self.actionDelete_Account.setObjectName(u"actionDelete_Account")
        self.actionExit = QAction(PyMoneyOrgaGui)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(PyMoneyOrgaGui)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_8 = QGridLayout(self.centralwidget)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_9 = QGridLayout()
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabTableView = QWidget()
        self.tabTableView.setObjectName(u"tabTableView")
        self.gridLayout_10 = QGridLayout(self.tabTableView)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.tableWidgetAccounts = QTableWidget(self.tabTableView)
        if (self.tableWidgetAccounts.columnCount() < 2):
            self.tableWidgetAccounts.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidgetAccounts.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidgetAccounts.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.tableWidgetAccounts.setObjectName(u"tableWidgetAccounts")
        self.tableWidgetAccounts.setMinimumSize(QSize(300, 600))
        self.tableWidgetAccounts.setShowGrid(True)
        self.tableWidgetAccounts.setSortingEnabled(True)
        self.tableWidgetAccounts.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidgetAccounts.horizontalHeader().setMinimumSectionSize(100)
        self.tableWidgetAccounts.horizontalHeader().setDefaultSectionSize(149)
        self.tableWidgetAccounts.horizontalHeader().setStretchLastSection(True)

        self.gridLayout.addWidget(self.tableWidgetAccounts, 0, 1, 3, 1)

        self.tableWidgetTransactions = QTableWidget(self.tabTableView)
        if (self.tableWidgetTransactions.columnCount() < 4):
            self.tableWidgetTransactions.setColumnCount(4)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidgetTransactions.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidgetTransactions.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidgetTransactions.setHorizontalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidgetTransactions.setHorizontalHeaderItem(3, __qtablewidgetitem5)
        self.tableWidgetTransactions.setObjectName(u"tableWidgetTransactions")
        self.tableWidgetTransactions.setMinimumSize(QSize(450, 600))
        self.tableWidgetTransactions.setSortingEnabled(True)
        self.tableWidgetTransactions.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidgetTransactions.horizontalHeader().setMinimumSectionSize(100)
        self.tableWidgetTransactions.horizontalHeader().setDefaultSectionSize(149)
        self.tableWidgetTransactions.horizontalHeader().setProperty("showSortIndicator", True)
        self.tableWidgetTransactions.horizontalHeader().setStretchLastSection(True)

        self.gridLayout.addWidget(self.tableWidgetTransactions, 0, 2, 3, 1)

        self.gridLayout_12 = QGridLayout()
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.checkShowAmount = QCheckBox(self.tabTableView)
        self.checkShowAmount.setObjectName(u"checkShowAmount")
        self.checkShowAmount.setChecked(True)

        self.gridLayout_12.addWidget(self.checkShowAmount, 2, 0, 1, 1)

        self.checkShowTimeStamp = QCheckBox(self.tabTableView)
        self.checkShowTimeStamp.setObjectName(u"checkShowTimeStamp")
        self.checkShowTimeStamp.setChecked(True)

        self.gridLayout_12.addWidget(self.checkShowTimeStamp, 1, 0, 1, 1)

        self.checkShowNewBalance = QCheckBox(self.tabTableView)
        self.checkShowNewBalance.setObjectName(u"checkShowNewBalance")
        self.checkShowNewBalance.setChecked(True)

        self.gridLayout_12.addWidget(self.checkShowNewBalance, 1, 1, 1, 1)

        self.checkShowDescription = QCheckBox(self.tabTableView)
        self.checkShowDescription.setObjectName(u"checkShowDescription")
        self.checkShowDescription.setChecked(True)

        self.gridLayout_12.addWidget(self.checkShowDescription, 2, 1, 1, 1)

        self.label = QLabel(self.tabTableView)
        self.label.setObjectName(u"label")

        self.gridLayout_12.addWidget(self.label, 0, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_12, 3, 2, 1, 1)


        self.gridLayout_10.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tabTableView, "")
        self.tabGraphicView = QWidget()
        self.tabGraphicView.setObjectName(u"tabGraphicView")
        self.gridLayout_5 = QGridLayout(self.tabGraphicView)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.widgetChart = QWidget(self.tabGraphicView)
        self.widgetChart.setObjectName(u"widgetChart")

        self.gridLayout_3.addWidget(self.widgetChart, 0, 0, 1, 1)


        self.gridLayout_5.addLayout(self.gridLayout_3, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tabGraphicView, "")

        self.gridLayout_9.addWidget(self.tabWidget, 0, 1, 1, 1)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.buttonAddExpenses = QPushButton(self.centralwidget)
        self.buttonAddExpenses.setObjectName(u"buttonAddExpenses")

        self.gridLayout_2.addWidget(self.buttonAddExpenses, 2, 0, 1, 1)

        self.buttonAddIncome = QPushButton(self.centralwidget)
        self.buttonAddIncome.setObjectName(u"buttonAddIncome")

        self.gridLayout_2.addWidget(self.buttonAddIncome, 3, 0, 1, 1)

        self.labelChooseAccount = QLabel(self.centralwidget)
        self.labelChooseAccount.setObjectName(u"labelChooseAccount")

        self.gridLayout_2.addWidget(self.labelChooseAccount, 0, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 400, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 4, 1, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.inputDescriptionExpenses = QLineEdit(self.centralwidget)
        self.inputDescriptionExpenses.setObjectName(u"inputDescriptionExpenses")

        self.gridLayout_4.addWidget(self.inputDescriptionExpenses, 0, 1, 1, 1)

        self.inputAddExpenses = QLineEdit(self.centralwidget)
        self.inputAddExpenses.setObjectName(u"inputAddExpenses")

        self.gridLayout_4.addWidget(self.inputAddExpenses, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_4, 2, 1, 1, 1)

        self.gridLayout_6 = QGridLayout()
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.inputDescriptionIncome = QLineEdit(self.centralwidget)
        self.inputDescriptionIncome.setObjectName(u"inputDescriptionIncome")

        self.gridLayout_6.addWidget(self.inputDescriptionIncome, 0, 1, 1, 1)

        self.inputAddIncome = QLineEdit(self.centralwidget)
        self.inputAddIncome.setObjectName(u"inputAddIncome")

        self.gridLayout_6.addWidget(self.inputAddIncome, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_6, 3, 1, 1, 1)

        self.comboChooseAccount = QComboBox(self.centralwidget)
        self.comboChooseAccount.addItem("")
        self.comboChooseAccount.setObjectName(u"comboChooseAccount")

        self.gridLayout_2.addWidget(self.comboChooseAccount, 0, 1, 1, 1)

        self.gridLayout_7 = QGridLayout()
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_7.addWidget(self.label_2, 0, 1, 1, 1)

        self.labelAddExpenses = QLabel(self.centralwidget)
        self.labelAddExpenses.setObjectName(u"labelAddExpenses")

        self.gridLayout_7.addWidget(self.labelAddExpenses, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_7, 1, 1, 1, 1)


        self.gridLayout_9.addLayout(self.gridLayout_2, 0, 0, 1, 1)


        self.gridLayout_8.addLayout(self.gridLayout_9, 0, 0, 1, 1)

        PyMoneyOrgaGui.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(PyMoneyOrgaGui)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1168, 21))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        PyMoneyOrgaGui.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(PyMoneyOrgaGui)
        self.statusbar.setObjectName(u"statusbar")
        PyMoneyOrgaGui.setStatusBar(self.statusbar)
#if QT_CONFIG(shortcut)
        self.labelChooseAccount.setBuddy(self.comboChooseAccount)
        self.labelAddExpenses.setBuddy(self.inputAddExpenses)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.comboChooseAccount, self.inputAddExpenses)
        QWidget.setTabOrder(self.inputAddExpenses, self.inputDescriptionExpenses)
        QWidget.setTabOrder(self.inputDescriptionExpenses, self.buttonAddExpenses)
        QWidget.setTabOrder(self.buttonAddExpenses, self.inputAddIncome)
        QWidget.setTabOrder(self.inputAddIncome, self.inputDescriptionIncome)
        QWidget.setTabOrder(self.inputDescriptionIncome, self.buttonAddIncome)
        QWidget.setTabOrder(self.buttonAddIncome, self.checkShowTimeStamp)
        QWidget.setTabOrder(self.checkShowTimeStamp, self.checkShowNewBalance)
        QWidget.setTabOrder(self.checkShowNewBalance, self.checkShowAmount)
        QWidget.setTabOrder(self.checkShowAmount, self.checkShowDescription)
        QWidget.setTabOrder(self.checkShowDescription, self.tableWidgetAccounts)
        QWidget.setTabOrder(self.tableWidgetAccounts, self.tableWidgetTransactions)
        QWidget.setTabOrder(self.tableWidgetTransactions, self.tabWidget)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menuFile.addAction(self.actionCreate_New_Account)
        self.menuFile.addAction(self.actionDeleteAccount)
        self.menuFile.addAction(self.actionExit)

        self.retranslateUi(PyMoneyOrgaGui)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(PyMoneyOrgaGui)
    # setupUi

    def retranslateUi(self, PyMoneyOrgaGui):
        PyMoneyOrgaGui.setWindowTitle(QCoreApplication.translate("PyMoneyOrgaGui", u"PyMoneyOrga", None))
        self.actionCreate_New_Account.setText(QCoreApplication.translate("PyMoneyOrgaGui", u"Create New Account", None))
        self.actionDeleteAccount.setText(QCoreApplication.translate("PyMoneyOrgaGui", u"Delete Account", None))
        self.actionDelete_Account.setText(QCoreApplication.translate("PyMoneyOrgaGui", u"Delete Account", None))
        self.actionExit.setText(QCoreApplication.translate("PyMoneyOrgaGui", u"Exit", None))
        ___qtablewidgetitem = self.tableWidgetAccounts.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("PyMoneyOrgaGui", u"Account", None));
        ___qtablewidgetitem1 = self.tableWidgetAccounts.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("PyMoneyOrgaGui", u"Balance", None));
        ___qtablewidgetitem2 = self.tableWidgetTransactions.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("PyMoneyOrgaGui", u"Time stamp", None));
        ___qtablewidgetitem3 = self.tableWidgetTransactions.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("PyMoneyOrgaGui", u"Amount", None));
        ___qtablewidgetitem4 = self.tableWidgetTransactions.horizontalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("PyMoneyOrgaGui", u"New balance", None));
        ___qtablewidgetitem5 = self.tableWidgetTransactions.horizontalHeaderItem(3)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("PyMoneyOrgaGui", u"Description", None));
        self.checkShowAmount.setText(QCoreApplication.translate("PyMoneyOrgaGui", u"Amount", None))
        self.checkShowTimeStamp.setText(QCoreApplication.translate("PyMoneyOrgaGui", u"Time stamp", None))
        self.checkShowNewBalance.setText(QCoreApplication.translate("PyMoneyOrgaGui", u"New balance", None))
        self.checkShowDescription.setText(QCoreApplication.translate("PyMoneyOrgaGui", u"Description", None))
        self.label.setText(QCoreApplication.translate("PyMoneyOrgaGui", u"What to show in transaction table", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTableView), QCoreApplication.translate("PyMoneyOrgaGui", u"Table view", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabGraphicView), QCoreApplication.translate("PyMoneyOrgaGui", u"Graphical view", None))
        self.buttonAddExpenses.setText(QCoreApplication.translate("PyMoneyOrgaGui", u"New expenses", None))
        self.buttonAddIncome.setText(QCoreApplication.translate("PyMoneyOrgaGui", u"New income", None))
        self.labelChooseAccount.setText(QCoreApplication.translate("PyMoneyOrgaGui", u"Choose account", None))
        self.comboChooseAccount.setItemText(0, QCoreApplication.translate("PyMoneyOrgaGui", u"NoAccountSaved", None))

        self.label_2.setText(QCoreApplication.translate("PyMoneyOrgaGui", u"Description", None))
        self.labelAddExpenses.setText(QCoreApplication.translate("PyMoneyOrgaGui", u"Amount", None))
        self.menuFile.setTitle(QCoreApplication.translate("PyMoneyOrgaGui", u"File", None))
    # retranslateUi

