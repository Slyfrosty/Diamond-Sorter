# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\admin\Desktop\pyqtQQ\ui\MainContactsPanel.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainContactsPanel(object):
    def setupUi(self, MainContactsPanel):
        MainContactsPanel.setObjectName("MainContactsPanel")
        MainContactsPanel.resize(300, 578)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainContactsPanel.sizePolicy().hasHeightForWidth())
        MainContactsPanel.setSizePolicy(sizePolicy)
        MainContactsPanel.setMinimumSize(QtCore.QSize(300, 400))
        MainContactsPanel.setStyleSheet("")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(MainContactsPanel)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.img_avatar = AvatarWidget(MainContactsPanel)
        self.img_avatar.setMinimumSize(QtCore.QSize(80, 80))
        self.img_avatar.setMaximumSize(QtCore.QSize(80, 80))
        self.img_avatar.setObjectName("img_avatar")
        self.horizontalLayout.addWidget(self.img_avatar)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lb_nickname = TitleLabel(MainContactsPanel)
        self.lb_nickname.setObjectName("lb_nickname")
        self.verticalLayout.addWidget(self.lb_nickname)
        self.lb_username = SubtitleLabel(MainContactsPanel)
        self.lb_username.setStyleSheet("color: rgb(121, 121, 121);")
        self.lb_username.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.lb_username.setProperty("pixelFontSize", 15)
        self.lb_username.setObjectName("lb_username")
        self.verticalLayout.addWidget(self.lb_username)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.le_search = SearchLineEdit(MainContactsPanel)
        self.le_search.setObjectName("le_search")
        self.verticalLayout_2.addWidget(self.le_search)
        self.stackedWidget = QtWidgets.QStackedWidget(MainContactsPanel)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_nowChatting = QtWidgets.QWidget()
        self.page_nowChatting.setObjectName("page_nowChatting")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.page_nowChatting)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lv_nowChatting = ListWidget(self.page_nowChatting)
        self.lv_nowChatting.setObjectName("lv_nowChatting")
        self.verticalLayout_3.addWidget(self.lv_nowChatting)
        self.stackedWidget.addWidget(self.page_nowChatting)
        self.page_friends = QtWidgets.QWidget()
        self.page_friends.setObjectName("page_friends")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page_friends)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lv_friends = ListWidget(self.page_friends)
        self.lv_friends.setObjectName("lv_friends")
        self.verticalLayout_5.addWidget(self.lv_friends)
        self.stackedWidget.addWidget(self.page_friends)
        self.page_groups = QtWidgets.QWidget()
        self.page_groups.setObjectName("page_groups")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page_groups)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.lv_groups = ListWidget(self.page_groups)
        self.lv_groups.setObjectName("lv_groups")
        self.verticalLayout_4.addWidget(self.lv_groups)
        self.stackedWidget.addWidget(self.page_groups)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.navigation = SegmentedWidget(MainContactsPanel)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.navigation.sizePolicy().hasHeightForWidth())
        self.navigation.setSizePolicy(sizePolicy)
        self.navigation.setMaximumSize(QtCore.QSize(16777215, 33))
        self.navigation.setObjectName("navigation")
        self.verticalLayout_2.addWidget(self.navigation)

        self.retranslateUi(MainContactsPanel)
        self.stackedWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainContactsPanel)

    def retranslateUi(self, MainContactsPanel):
        _translate = QtCore.QCoreApplication.translate
        MainContactsPanel.setWindowTitle(_translate("MainContactsPanel", "💎 Diamond Sorter Chat"))
        self.lb_nickname.setText(_translate("MainContactsPanel", "Title label"))
        self.lb_username.setText(_translate("MainContactsPanel", "Subtitle label"))
from qfluentwidgets import AvatarWidget, ListWidget, SearchLineEdit, SegmentedWidget, SubtitleLabel, TitleLabel
import resources_rc
