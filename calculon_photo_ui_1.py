# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculon_photo_ui_1.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1600, 1048)
        MainWindow.setFocusPolicy(QtCore.Qt.NoFocus)
        MainWindow.setStyleSheet("background-color: rgb(242, 238, 235);")
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        MainWindow.setIconSize(QtCore.QSize(22, 11))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(1, 1, 1598, 1022))
        self.tabWidget.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setIconSize(QtCore.QSize(16, 16))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.label_40 = QtWidgets.QLabel(self.tab_8)
        self.label_40.setGeometry(QtCore.QRect(660, 10, 321, 61))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_40.setFont(font)
        self.label_40.setAlignment(QtCore.Qt.AlignCenter)
        self.label_40.setObjectName("label_40")
        self.label_41 = QtWidgets.QLabel(self.tab_8)
        self.label_41.setGeometry(QtCore.QRect(570, 90, 521, 20))
        self.label_41.setAlignment(QtCore.Qt.AlignCenter)
        self.label_41.setObjectName("label_41")
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_8)
        self.pushButton_6.setGeometry(QtCore.QRect(290, 190, 531, 34))
        self.pushButton_6.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton_6.setCheckable(True)
        self.pushButton_6.setChecked(False)
        self.pushButton_6.setObjectName("pushButton_6")
        self.textEdit = QtWidgets.QTextEdit(self.tab_8)
        self.textEdit.setGeometry(QtCore.QRect(150, 280, 1280, 500))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(247, 247, 248))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(196, 201, 205))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(252, 252, 252))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(242, 238, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 247, 248))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 201, 205))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 252, 252))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 238, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 247, 248))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 201, 205))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 252, 252))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 238, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        self.textEdit.setPalette(palette)
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.textEdit.setObjectName("textEdit")
        self.label_95 = QtWidgets.QLabel(self.tab_8)
        self.label_95.setGeometry(QtCore.QRect(30, 30, 236, 236))
        self.label_95.setText("")
        self.label_95.setObjectName("label_95")
        self.tabWidget.addTab(self.tab_8, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_18 = QtWidgets.QLabel(self.tab_2)
        self.label_18.setGeometry(QtCore.QRect(670, 610, 100, 18))
        self.label_18.setObjectName("label_18")
        self.label_20 = QtWidgets.QLabel(self.tab_2)
        self.label_20.setGeometry(QtCore.QRect(0, 390, 230, 20))
        self.label_20.setToolTip("")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(self.tab_2)
        self.label_21.setGeometry(QtCore.QRect(370, 690, 200, 20))
        self.label_21.setAlignment(QtCore.Qt.AlignCenter)
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.tab_2)
        self.label_22.setGeometry(QtCore.QRect(10, 470, 190, 20))
        self.label_22.setObjectName("label_22")
        self.lineEdit_18 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_18.setGeometry(QtCore.QRect(460, 500, 230, 32))
        self.lineEdit_18.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_18.setStyleSheet("background-color: rgb(252, 250, 249);")
        self.lineEdit_18.setMaxLength(25)
        self.lineEdit_18.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_18.setDragEnabled(True)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.label_24 = QtWidgets.QLabel(self.tab_2)
        self.label_24.setGeometry(QtCore.QRect(10, 540, 100, 20))
        self.label_24.setAlignment(QtCore.Qt.AlignCenter)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.tab_2)
        self.label_25.setGeometry(QtCore.QRect(150, 10, 500, 20))
        self.label_25.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_25.setAlignment(QtCore.Qt.AlignCenter)
        self.label_25.setObjectName("label_25")
        self.lineEdit_19 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_19.setGeometry(QtCore.QRect(20, 570, 100, 32))
        self.lineEdit_19.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_19.setStyleSheet("background-color: rgb(252, 250, 249);")
        self.lineEdit_19.setMaxLength(13)
        self.lineEdit_19.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_19.setDragEnabled(True)
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.label_26 = QtWidgets.QLabel(self.tab_2)
        self.label_26.setGeometry(QtCore.QRect(450, 470, 230, 20))
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.tab_2)
        self.label_27.setGeometry(QtCore.QRect(210, 480, 180, 20))
        self.label_27.setAlignment(QtCore.Qt.AlignCenter)
        self.label_27.setObjectName("label_27")
        self.lineEdit_22 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_22.setGeometry(QtCore.QRect(0, 420, 291, 32))
        self.lineEdit_22.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_22.setStyleSheet("background-color: rgb(252, 250, 249);")
        self.lineEdit_22.setMaxLength(30)
        self.lineEdit_22.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_22.setDragEnabled(True)
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.lineEdit_23 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_23.setGeometry(QtCore.QRect(250, 500, 113, 32))
        self.lineEdit_23.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_23.setStyleSheet("background-color: rgb(252, 250, 249);")
        self.lineEdit_23.setMaxLength(10)
        self.lineEdit_23.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_23.setDragEnabled(True)
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.label_29 = QtWidgets.QLabel(self.tab_2)
        self.label_29.setGeometry(QtCore.QRect(-10, 610, 550, 20))
        self.label_29.setAlignment(QtCore.Qt.AlignCenter)
        self.label_29.setObjectName("label_29")
        self.lineEdit_24 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_24.setGeometry(QtCore.QRect(10, 720, 300, 32))
        self.lineEdit_24.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_24.setStyleSheet("background-color: rgb(252, 250, 249);")
        self.lineEdit_24.setMaxLength(30)
        self.lineEdit_24.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_24.setDragEnabled(True)
        self.lineEdit_24.setObjectName("lineEdit_24")
        self.label_30 = QtWidgets.QLabel(self.tab_2)
        self.label_30.setGeometry(QtCore.QRect(200, 540, 150, 20))
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName("label_30")
        self.lineEdit_25 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_25.setGeometry(QtCore.QRect(380, 720, 200, 32))
        self.lineEdit_25.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_25.setStyleSheet("background-color: rgb(252, 250, 249);")
        self.lineEdit_25.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_25.setDragEnabled(True)
        self.lineEdit_25.setObjectName("lineEdit_25")
        self.lineEdit_26 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_26.setGeometry(QtCore.QRect(0, 640, 550, 32))
        self.lineEdit_26.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_26.setStyleSheet("background-color: rgb(252, 250, 249);")
        self.lineEdit_26.setMaxLength(50)
        self.lineEdit_26.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_26.setDragEnabled(True)
        self.lineEdit_26.setObjectName("lineEdit_26")
        self.lineEdit_27 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_27.setGeometry(QtCore.QRect(650, 640, 113, 32))
        self.lineEdit_27.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_27.setStyleSheet("background-color: rgb(252, 250, 249);")
        self.lineEdit_27.setObjectName("lineEdit_27")
        self.lineEdit_28 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_28.setGeometry(QtCore.QRect(230, 570, 100, 32))
        self.lineEdit_28.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_28.setStyleSheet("background-color: rgb(252, 250, 249);")
        self.lineEdit_28.setMaxLength(10)
        self.lineEdit_28.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_28.setDragEnabled(True)
        self.lineEdit_28.setObjectName("lineEdit_28")
        self.lineEdit_29 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_29.setGeometry(QtCore.QRect(430, 420, 251, 32))
        self.lineEdit_29.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_29.setStyleSheet("background-color: rgb(252, 250, 249);")
        self.lineEdit_29.setMaxLength(20)
        self.lineEdit_29.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_29.setObjectName("lineEdit_29")
        self.label_33 = QtWidgets.QLabel(self.tab_2)
        self.label_33.setGeometry(QtCore.QRect(440, 390, 150, 20))
        self.label_33.setAlignment(QtCore.Qt.AlignCenter)
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(self.tab_2)
        self.label_34.setGeometry(QtCore.QRect(10, 690, 300, 20))
        self.label_34.setAlignment(QtCore.Qt.AlignCenter)
        self.label_34.setObjectName("label_34")
        self.lineEdit_33 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_33.setGeometry(QtCore.QRect(0, 500, 150, 32))
        self.lineEdit_33.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_33.setStyleSheet("background-color: rgb(252, 250, 249);")
        self.lineEdit_33.setMaxLength(15)
        self.lineEdit_33.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_33.setDragEnabled(True)
        self.lineEdit_33.setObjectName("lineEdit_33")
        self.spinBox_2 = QtWidgets.QSpinBox(self.tab_2)
        self.spinBox_2.setGeometry(QtCore.QRect(530, 40, 1, 1))
        self.spinBox_2.setFocusPolicy(QtCore.Qt.NoFocus)
        self.spinBox_2.setMinimum(0)
        self.spinBox_2.setMaximum(99)
        self.spinBox_2.setSingleStep(0)
        self.spinBox_2.setProperty("value", 50)
        self.spinBox_2.setDisplayIntegerBase(10)
        self.spinBox_2.setObjectName("spinBox_2")
        self.lineEdit_53 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_53.setGeometry(QtCore.QRect(25, 230, 500, 25))
        self.lineEdit_53.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit_53.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_53.setDragEnabled(True)
        self.lineEdit_53.setObjectName("lineEdit_53")
        self.lineEdit_52 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_52.setGeometry(QtCore.QRect(25, 205, 500, 25))
        self.lineEdit_52.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit_52.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_52.setDragEnabled(True)
        self.lineEdit_52.setObjectName("lineEdit_52")
        self.lineEdit_48 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_48.setGeometry(QtCore.QRect(25, 105, 500, 25))
        self.lineEdit_48.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit_48.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_48.setDragEnabled(True)
        self.lineEdit_48.setObjectName("lineEdit_48")
        self.label_38 = QtWidgets.QLabel(self.tab_2)
        self.label_38.setGeometry(QtCore.QRect(25, 305, 821, 45))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_38.setFont(font)
        self.label_38.setAlignment(QtCore.Qt.AlignCenter)
        self.label_38.setObjectName("label_38")
        self.lineEdit_49 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_49.setGeometry(QtCore.QRect(25, 130, 500, 25))
        self.lineEdit_49.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit_49.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_49.setDragEnabled(True)
        self.lineEdit_49.setObjectName("lineEdit_49")
        self.lineEdit_54 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_54.setGeometry(QtCore.QRect(25, 255, 500, 25))
        self.lineEdit_54.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit_54.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_54.setDragEnabled(True)
        self.lineEdit_54.setObjectName("lineEdit_54")
        self.lineEdit_50 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_50.setGeometry(QtCore.QRect(25, 155, 500, 25))
        self.lineEdit_50.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit_50.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_50.setDragEnabled(True)
        self.lineEdit_50.setObjectName("lineEdit_50")
        self.lineEdit_46 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_46.setGeometry(QtCore.QRect(25, 55, 500, 25))
        self.lineEdit_46.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit_46.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_46.setDragEnabled(True)
        self.lineEdit_46.setObjectName("lineEdit_46")
        self.lineEdit_51 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_51.setGeometry(QtCore.QRect(25, 180, 500, 25))
        self.lineEdit_51.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit_51.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_51.setDragEnabled(True)
        self.lineEdit_51.setObjectName("lineEdit_51")
        self.lineEdit_47 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_47.setGeometry(QtCore.QRect(25, 80, 500, 25))
        self.lineEdit_47.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit_47.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_47.setDragEnabled(True)
        self.lineEdit_47.setObjectName("lineEdit_47")
        self.lineEdit_45 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_45.setGeometry(QtCore.QRect(25, 30, 500, 25))
        self.lineEdit_45.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit_45.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_45.setDragEnabled(True)
        self.lineEdit_45.setObjectName("lineEdit_45")
        self.label_37 = QtWidgets.QLabel(self.tab_2)
        self.label_37.setGeometry(QtCore.QRect(530, 270, 101, 20))
        self.label_37.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_37.setObjectName("label_37")
        self.widget = QtWidgets.QWidget(self.tab_2)
        self.widget.setGeometry(QtCore.QRect(865, 1, 722, 1005))
        self.widget.setObjectName("widget")
        self.label_42 = QtWidgets.QLabel(self.widget)
        self.label_42.setGeometry(QtCore.QRect(1, 1, 720, 900))
        self.label_42.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_42.setFrameShape(QtWidgets.QFrame.Box)
        self.label_42.setScaledContents(False)
        self.label_42.setAlignment(QtCore.Qt.AlignCenter)
        self.label_42.setObjectName("label_42")
        self.spinBox_4 = QtWidgets.QSpinBox(self.widget)
        self.spinBox_4.setGeometry(QtCore.QRect(261, 901, 451, 84))
        self.spinBox_4.setFocusPolicy(QtCore.Qt.NoFocus)
        self.spinBox_4.setAlignment(QtCore.Qt.AlignCenter)
        self.spinBox_4.setButtonSymbols(QtWidgets.QAbstractSpinBox.UpDownArrows)
        self.spinBox_4.setSuffix("")
        self.spinBox_4.setMaximum(50)
        self.spinBox_4.setSingleStep(1)
        self.spinBox_4.setDisplayIntegerBase(10)
        self.spinBox_4.setObjectName("spinBox_4")
        self.label_46 = QtWidgets.QLabel(self.tab_2)
        self.label_46.setGeometry(QtCore.QRect(149, 780, 711, 32))
        self.label_46.setStyleSheet("background-color: rgb(255, 255, 196);")
        self.label_46.setText("")
        self.label_46.setAlignment(QtCore.Qt.AlignCenter)
        self.label_46.setObjectName("label_46")
        self.label_47 = QtWidgets.QLabel(self.tab_2)
        self.label_47.setGeometry(QtCore.QRect(0, 780, 150, 20))
        self.label_47.setAlignment(QtCore.Qt.AlignCenter)
        self.label_47.setObjectName("label_47")
        self.checkBox_18 = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_18.setGeometry(QtCore.QRect(630, 120, 151, 31))
        self.checkBox_18.setObjectName("checkBox_18")
        self.radioButton_19 = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton_19.setGeometry(QtCore.QRect(630, 170, 171, 22))
        self.radioButton_19.setObjectName("radioButton_19")
        self.buttonGroup_7 = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup_7.setObjectName("buttonGroup_7")
        self.buttonGroup_7.addButton(self.radioButton_19)
        self.radioButton_20 = QtWidgets.QRadioButton(self.tab_2)
        self.radioButton_20.setGeometry(QtCore.QRect(630, 210, 151, 22))
        self.radioButton_20.setObjectName("radioButton_20")
        self.buttonGroup_7.addButton(self.radioButton_20)
        self.pushButton_18 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_18.setGeometry(QtCore.QRect(20, 930, 149, 34))
        self.pushButton_18.setAutoDefault(False)
        self.pushButton_18.setDefault(True)
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_19.setGeometry(QtCore.QRect(190, 930, 150, 34))
        self.pushButton_19.setAutoDefault(False)
        self.pushButton_19.setDefault(True)
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_21 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_21.setGeometry(QtCore.QRect(450, 930, 150, 34))
        self.pushButton_21.setDefault(True)
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_9 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_9.setGeometry(QtCore.QRect(640, 930, 150, 34))
        self.pushButton_9.setDefault(True)
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_8 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_8.setGeometry(QtCore.QRect(640, 840, 150, 34))
        self.pushButton_8.setDefault(True)
        self.pushButton_8.setObjectName("pushButton_8")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_7 = QtWidgets.QWidget()
        self.tab_7.setEnabled(False)
        self.tab_7.setObjectName("tab_7")
        self.lineEdit_102 = QtWidgets.QLineEdit(self.tab_7)
        self.lineEdit_102.setGeometry(QtCore.QRect(20, 110, 1550, 25))
        self.lineEdit_102.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.lineEdit_102.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_102.setDragEnabled(True)
        self.lineEdit_102.setObjectName("lineEdit_102")
        self.lineEdit_108 = QtWidgets.QLineEdit(self.tab_7)
        self.lineEdit_108.setGeometry(QtCore.QRect(20, 50, 1550, 25))
        self.lineEdit_108.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.lineEdit_108.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_108.setDragEnabled(True)
        self.lineEdit_108.setObjectName("lineEdit_108")
        self.lineEdit_112 = QtWidgets.QLineEdit(self.tab_7)
        self.lineEdit_112.setGeometry(QtCore.QRect(20, 170, 750, 25))
        self.lineEdit_112.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.lineEdit_112.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_112.setDragEnabled(True)
        self.lineEdit_112.setObjectName("lineEdit_112")
        self.lineEdit_113 = QtWidgets.QLineEdit(self.tab_7)
        self.lineEdit_113.setGeometry(QtCore.QRect(800, 170, 750, 25))
        self.lineEdit_113.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.lineEdit_113.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_113.setObjectName("lineEdit_113")
        self.label_161 = QtWidgets.QLabel(self.tab_7)
        self.label_161.setGeometry(QtCore.QRect(500, 90, 500, 20))
        self.label_161.setAlignment(QtCore.Qt.AlignCenter)
        self.label_161.setObjectName("label_161")
        self.label_167 = QtWidgets.QLabel(self.tab_7)
        self.label_167.setGeometry(QtCore.QRect(500, 30, 500, 20))
        self.label_167.setAlignment(QtCore.Qt.AlignCenter)
        self.label_167.setObjectName("label_167")
        self.label_171 = QtWidgets.QLabel(self.tab_7)
        self.label_171.setGeometry(QtCore.QRect(125, 150, 500, 20))
        self.label_171.setAlignment(QtCore.Qt.AlignCenter)
        self.label_171.setObjectName("label_171")
        self.label_172 = QtWidgets.QLabel(self.tab_7)
        self.label_172.setGeometry(QtCore.QRect(900, 150, 500, 20))
        self.label_172.setAlignment(QtCore.Qt.AlignCenter)
        self.label_172.setObjectName("label_172")
        self.lineEdit_125 = QtWidgets.QLineEdit(self.tab_7)
        self.lineEdit_125.setGeometry(QtCore.QRect(20, 230, 370, 25))
        self.lineEdit_125.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.lineEdit_125.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_125.setObjectName("lineEdit_125")
        self.label_184 = QtWidgets.QLabel(self.tab_7)
        self.label_184.setGeometry(QtCore.QRect(105, 210, 200, 20))
        self.label_184.setAlignment(QtCore.Qt.AlignCenter)
        self.label_184.setObjectName("label_184")
        self.lineEdit_132 = QtWidgets.QLineEdit(self.tab_7)
        self.lineEdit_132.setGeometry(QtCore.QRect(410, 230, 370, 25))
        self.lineEdit_132.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.lineEdit_132.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_132.setObjectName("lineEdit_132")
        self.label_191 = QtWidgets.QLabel(self.tab_7)
        self.label_191.setGeometry(QtCore.QRect(490, 210, 200, 20))
        self.label_191.setAlignment(QtCore.Qt.AlignCenter)
        self.label_191.setObjectName("label_191")
        self.label_192 = QtWidgets.QLabel(self.tab_7)
        self.label_192.setGeometry(QtCore.QRect(880, 210, 200, 20))
        self.label_192.setAlignment(QtCore.Qt.AlignCenter)
        self.label_192.setObjectName("label_192")
        self.lineEdit_133 = QtWidgets.QLineEdit(self.tab_7)
        self.lineEdit_133.setGeometry(QtCore.QRect(800, 230, 370, 25))
        self.lineEdit_133.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.lineEdit_133.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_133.setObjectName("lineEdit_133")
        self.label_193 = QtWidgets.QLabel(self.tab_7)
        self.label_193.setGeometry(QtCore.QRect(1270, 210, 200, 20))
        self.label_193.setAlignment(QtCore.Qt.AlignCenter)
        self.label_193.setObjectName("label_193")
        self.lineEdit_134 = QtWidgets.QLineEdit(self.tab_7)
        self.lineEdit_134.setGeometry(QtCore.QRect(1190, 230, 370, 25))
        self.lineEdit_134.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.lineEdit_134.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_134.setObjectName("lineEdit_134")
        self.label_211 = QtWidgets.QLabel(self.tab_7)
        self.label_211.setGeometry(QtCore.QRect(40, 270, 200, 20))
        self.label_211.setAlignment(QtCore.Qt.AlignCenter)
        self.label_211.setObjectName("label_211")
        self.lineEdit_161 = QtWidgets.QLineEdit(self.tab_7)
        self.lineEdit_161.setGeometry(QtCore.QRect(20, 290, 240, 25))
        self.lineEdit_161.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.lineEdit_161.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_161.setObjectName("lineEdit_161")
        self.tabWidget.addTab(self.tab_7, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEdit_22, self.lineEdit_29)
        MainWindow.setTabOrder(self.lineEdit_29, self.lineEdit_33)
        MainWindow.setTabOrder(self.lineEdit_33, self.lineEdit_23)
        MainWindow.setTabOrder(self.lineEdit_23, self.lineEdit_18)
        MainWindow.setTabOrder(self.lineEdit_18, self.lineEdit_19)
        MainWindow.setTabOrder(self.lineEdit_19, self.lineEdit_28)
        MainWindow.setTabOrder(self.lineEdit_28, self.lineEdit_26)
        MainWindow.setTabOrder(self.lineEdit_26, self.lineEdit_27)
        MainWindow.setTabOrder(self.lineEdit_27, self.lineEdit_24)
        MainWindow.setTabOrder(self.lineEdit_24, self.lineEdit_25)
        MainWindow.setTabOrder(self.lineEdit_25, self.pushButton_6)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_40.setText(_translate("MainWindow", "GGGGG"))
        self.label_41.setText(_translate("MainWindow", "ID Helper"))
        self.pushButton_6.setText(_translate("MainWindow", "Press for Manual"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_8), _translate("MainWindow", "&0.Welcome!"))
        self.label_18.setText(_translate("MainWindow", "Country"))
        self.label_20.setText(_translate("MainWindow", "Name, Patronim or only Name"))
        self.label_21.setText(_translate("MainWindow", "Phone"))
        self.label_22.setText(_translate("MainWindow", "ID or pass and number"))
        self.label_24.setText(_translate("MainWindow", "Personal code"))
        self.label_25.setText(_translate("MainWindow", "Clients"))
        self.label_26.setText(_translate("MainWindow", "Place of issue "))
        self.label_27.setText(_translate("MainWindow", "date of issue  xx xx yy"))
        self.label_29.setText(_translate("MainWindow", "Address"))
        self.label_30.setText(_translate("MainWindow", "ID/pass valid"))
        self.label_33.setText(_translate("MainWindow", "Surname"))
        self.label_34.setText(_translate("MainWindow", "Profession"))
        self.label_38.setText(_translate("MainWindow", "Input Text"))
        self.label_37.setText(_translate("MainWindow", "pages selection"))
        self.label_42.setText(_translate("MainWindow", "Image window"))
        self.spinBox_4.setPrefix(_translate("MainWindow", "Scrolling with the mouse wheel, picture "))
        self.label_47.setText(_translate("MainWindow", "a comment"))
        self.checkBox_18.setText(_translate("MainWindow", "Graphics mode"))
        self.radioButton_19.setText(_translate("MainWindow", "ID two images in one"))
        self.radioButton_20.setText(_translate("MainWindow", "passport one img"))
        self.pushButton_18.setText(_translate("MainWindow", "eXit"))
        self.pushButton_19.setText(_translate("MainWindow", "Next person"))
        self.pushButton_21.setText(_translate("MainWindow", "Go and save"))
        self.pushButton_9.setText(_translate("MainWindow", "Previous"))
        self.pushButton_8.setText(_translate("MainWindow", "view eDitet"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "&1.Entering and view data"))
        self.label_161.setText(_translate("MainWindow", "nn.2 endReport"))
        self.label_167.setText(_translate("MainWindow", "nn.8 List of clients"))
        self.label_171.setText(_translate("MainWindow", "nn.12  imgFileFull2"))
        self.label_172.setText(_translate("MainWindow", "nn.13 eDit len Group"))
        self.label_184.setText(_translate("MainWindow", "nn.25 gEx7"))
        self.label_191.setText(_translate("MainWindow", "nn.32 eDit_1"))
        self.label_192.setText(_translate("MainWindow", "nn.33 gEx"))
        self.label_193.setText(_translate("MainWindow", "nn.34 gEy"))
        self.label_211.setText(_translate("MainWindow", "nn.61"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("MainWindow", "not use"))
