import sys

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QWidget, QSlider, QLabel
from PyQt5.QtGui import QPixmap

from math import sqrt, sin, cos, tan, log, e, pi, asin, acos, atan
import csv
from PIL import Image, ImageDraw
import sqlite3


class CurGraphs_Ui(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(492, 424)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.delBtn = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(14)
        self.delBtn.setFont(font)
        self.delBtn.setObjectName("delBtn")
        self.gridLayout.addWidget(self.delBtn, 3, 2, 1, 1, QtCore.Qt.AlignRight)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 0, 1, 1, 2)
        self.backBtn = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(14)
        self.backBtn.setFont(font)
        self.backBtn.setObjectName("backBtn")
        self.gridLayout.addWidget(self.backBtn, 3, 1, 1, 1, QtCore.Qt.AlignLeft)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.delBtn.setText(_translate("Form", "Delete"))
        self.backBtn.setText(_translate("Form", "Back"))


class Settings_Ui(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(226, 187)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setMinimumSize(QtCore.QSize(150, 0))
        self.label.setMaximumSize(QtCore.QSize(226, 34))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.horizontalSlider = QtWidgets.QSlider(Form)
        self.horizontalSlider.setMinimumSize(QtCore.QSize(200, 22))
        self.horizontalSlider.setMaximumSize(QtCore.QSize(10000, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.gridLayout.addWidget(self.horizontalSlider, 1, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.applyBtn = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(14)
        self.applyBtn.setFont(font)
        self.applyBtn.setObjectName("applyBtn")
        self.gridLayout.addWidget(self.applyBtn, 2, 0, 1, 1)
        self.defaultBtn = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(14)
        self.defaultBtn.setFont(font)
        self.defaultBtn.setObjectName("defaultBtn")
        self.gridLayout.addWidget(self.defaultBtn, 3, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Graphic width"))
        self.applyBtn.setText(_translate("Form", "Apply Changes"))
        self.defaultBtn.setText(_translate("Form", "Set default settings"))


class MyGraphs_Ui(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(503, 739)
        Dialog.setMaximumSize(QtCore.QSize(503, 739))
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.deleteallBtn = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(14)
        self.deleteallBtn.setFont(font)
        self.deleteallBtn.setObjectName("deleteallBtn")
        self.gridLayout.addWidget(self.deleteallBtn, 5, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.backBtn = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(14)
        self.backBtn.setFont(font)
        self.backBtn.setObjectName("backBtn")
        self.gridLayout.addWidget(self.backBtn, 0, 3, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(12)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 2, 0, 1, 4)
        self.addGraph = QtWidgets.QPushButton(Dialog)
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(14)
        self.addGraph.setFont(font)
        self.addGraph.setObjectName("addGraph")
        self.gridLayout.addWidget(self.addGraph, 5, 3, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.deleteallBtn.setText(_translate("Dialog", "Delete all"))
        self.backBtn.setText(_translate("Dialog", "Back"))
        self.label.setText(_translate("Dialog", "My Graphs"))
        self.addGraph.setText(_translate("Dialog", "Add this graph"))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1008, 751)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 5, 1, 1)
        self.erraseBtn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(14)
        self.erraseBtn.setFont(font)
        self.erraseBtn.setObjectName("erraseBtn")
        self.gridLayout.addWidget(self.erraseBtn, 4, 7, 1, 1)
        self.openMygraph = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(14)
        self.openMygraph.setFont(font)
        self.openMygraph.setObjectName("openMygraph")
        self.gridLayout.addWidget(self.openMygraph, 4, 6, 1, 1)
        self.optionsBtn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(14)
        self.optionsBtn.setFont(font)
        self.optionsBtn.setObjectName("optionsBtn")
        self.gridLayout.addWidget(self.optionsBtn, 4, 10, 1, 1)
        self.drawBtn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.drawBtn.setFont(font)
        self.drawBtn.setObjectName("drawBtn")
        self.gridLayout.addWidget(self.drawBtn, 2, 7, 1, 2)
        self.imgGraphLbl = QtWidgets.QLabel(self.centralwidget)
        self.imgGraphLbl.setMinimumSize(QtCore.QSize(395, 295))
        self.imgGraphLbl.setObjectName("imgGraphLbl")
        self.gridLayout.addWidget(self.imgGraphLbl, 3, 0, 1, 11)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setMaximumSize(QtCore.QSize(79, 20))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(14)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 2, 6, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setMinimumSize(QtCore.QSize(200, 45))
        font = QtGui.QFont()
        font.setFamily("SimSun-ExtB")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(179, 54))
        self.label.setMaximumSize(QtCore.QSize(16777215, 54))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Symbol")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 2, 1, 4, QtCore.Qt.AlignHCenter)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setMaximumSize(QtCore.QSize(150, 25))
        font = QtGui.QFont()
        font.setFamily("SimSun")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 4, 0, 1, 1)
        self.inputFunc = QtWidgets.QLineEdit(self.centralwidget)
        self.inputFunc.setMinimumSize(QtCore.QSize(283, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.inputFunc.setFont(font)
        self.inputFunc.setObjectName("inputFunc")
        self.gridLayout.addWidget(self.inputFunc, 2, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1008, 21))
        self.menubar.setObjectName("menubar")
        self.menuHints = QtWidgets.QMenu(self.menubar)
        self.menuHints.setObjectName("menuHints")
        self.menuLinear_function = QtWidgets.QMenu(self.menuHints)
        self.menuLinear_function.setObjectName("menuLinear_function")
        self.menuParabola = QtWidgets.QMenu(self.menuHints)
        self.menuParabola.setObjectName("menuParabola")
        self.menuHyperbola = QtWidgets.QMenu(self.menuHints)
        self.menuHyperbola.setObjectName("menuHyperbola")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionHow_can_i_create_graph = QtWidgets.QAction(MainWindow)
        self.actionHow_can_i_create_graph.setObjectName("actionHow_can_i_create_graph")
        self.actionWhere_can_i_check_graph_stats = QtWidgets.QAction(MainWindow)
        self.actionWhere_can_i_check_graph_stats.setObjectName("actionWhere_can_i_check_graph_stats")
        self.actiony_k_x_b = QtWidgets.QAction(MainWindow)
        self.actiony_k_x_b.setObjectName("actiony_k_x_b")
        self.actiony_a_x_2_b_x_c = QtWidgets.QAction(MainWindow)
        self.actiony_a_x_2_b_x_c.setObjectName("actiony_a_x_2_b_x_c")
        self.actiony_k_x_b_2 = QtWidgets.QAction(MainWindow)
        self.actiony_k_x_b_2.setObjectName("actiony_k_x_b_2")
        self.menuLinear_function.addAction(self.actiony_k_x_b)
        self.menuParabola.addAction(self.actiony_a_x_2_b_x_c)
        self.menuHyperbola.addAction(self.actiony_k_x_b_2)
        self.menuHints.addAction(self.menuLinear_function.menuAction())
        self.menuHints.addAction(self.menuParabola.menuAction())
        self.menuHints.addAction(self.menuHyperbola.menuAction())
        self.menubar.addAction(self.menuHints.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Choose color:"))
        self.erraseBtn.setText(_translate("MainWindow", "Errase all"))
        self.openMygraph.setText(_translate("MainWindow", "All graphs"))
        self.optionsBtn.setText(_translate("MainWindow", "Options"))
        self.drawBtn.setText(_translate("MainWindow", "Draw!"))
        self.imgGraphLbl.setText(_translate("MainWindow", "Image"))
        self.comboBox.setItemText(0, _translate("MainWindow", "red"))
        self.comboBox.setItemText(1, _translate("MainWindow", "black"))
        self.comboBox.setItemText(2, _translate("MainWindow", "green"))
        self.comboBox.setItemText(3, _translate("MainWindow", "blue"))
        self.comboBox.setItemText(4, _translate("MainWindow", "gray"))
        self.comboBox.setItemText(5, _translate("MainWindow", "yellow"))
        self.comboBox.setItemText(6, _translate("MainWindow", "pink"))
        self.comboBox.setItemText(7, _translate("MainWindow", "orange"))
        self.comboBox.setItemText(8, _translate("MainWindow", "brown"))
        self.comboBox.setItemText(9, _translate("MainWindow", "purple"))
        self.label_2.setText(_translate("MainWindow", "Input your function:"))
        self.label.setText(_translate("MainWindow", "Graphic Builder 1.0"))
        self.pushButton.setText(_translate("MainWindow", "Current graphs"))
        self.menuHints.setTitle(_translate("MainWindow", "Hints"))
        self.menuLinear_function.setTitle(_translate("MainWindow", "Linear function"))
        self.menuParabola.setTitle(_translate("MainWindow", "Parabola"))
        self.menuHyperbola.setTitle(_translate("MainWindow", "Hyperbola"))
        self.actionHow_can_i_create_graph.setText(_translate("MainWindow", "How can i create graph?"))
        self.actionWhere_can_i_check_graph_stats.setText(_translate("MainWindow", "Where can i check graph stats?"))
        self.actiony_k_x_b.setText(_translate("MainWindow", "y=k*x+b"))
        self.actiony_a_x_2_b_x_c.setText(_translate("MainWindow", "y=a*x^2+b*x+c"))
        self.actiony_k_x_b_2.setText(_translate("MainWindow", "y=k/x+b"))


class GraphBuilder(QMainWindow, Ui_MainWindow):  # Основное окно
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Graph Builder')
        self.showMaximized()

        self.init_field()  # Создаём поле
        self.pixmap = QPixmap('origin_field.jpg')
        self.imgGraphLbl.setPixmap(self.pixmap)

        self.drawBtn.clicked.connect(self.draw_graph_and_save)  # Подключаем кнопки
        self.erraseBtn.clicked.connect(self.errase)
        self.optionsBtn.clicked.connect(self.option)
        self.pushButton.clicked.connect(self.current_graphs)
        self.openMygraph.clicked.connect(self.my_graphs)

        self.actiony_k_x_b.triggered.connect(self.draw_linear)  # Подключаем действия
        self.actiony_k_x_b_2.triggered.connect(self.draw_hyperbola)
        self.actiony_a_x_2_b_x_c.triggered.connect(self.draw_parabola)

        self.fieldnames = ['number', 'function', 'colour']  # Заголовки столбцов таблицы
        self.cur_num = 1
        self.width = 4

        with open('cur_graphs.csv', 'w') as f:  # Перезаписываем csv файл
            writer = csv.DictWriter(f, fieldnames=self.fieldnames, delimiter=';')
            writer.writeheader()

    def draw_graph_and_save(self):  # Основная функция рисования
        self.func = self.inputFunc.text()
        self.func = self.func.replace(' ', '')

        # Проверяем ошибки
        if not self.inputFunc.text():
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Error")
            msg_box.setText('Function input field is empty.')
            msg_box.exec_()
        elif not self.func[:2] == 'y=':
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Error")
            msg_box.setText("""Function should start with 'y='.""")
            msg_box.exec_()
        elif not (('(' in self.func or ')' in self.func and (self.func.count('(') == 1 and self.func.count(')') == 1
                                                             and self.func.find('(') < self.func.find(')'))) or not
                  ('|' in self.func and self.func.count('|') % 2 == 0)):
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Error")
            msg_box.setText("Incorrect parentheses")
            msg_box.exec_()

        else:  # Если ошибок нет, рисуем график
            try:
                im = Image.open('origin_field.jpg')
                draw = ImageDraw.Draw(im)

                # Преобразования функции

                self.func = self.func[2:]
                self.func = self.func.replace('^', '**')

                self.filling = self.comboBox.currentText()  # Цвет заливки

                self.new_func = ''
                if len(self.func) == 1:
                    self.new_func = self.func
                else:
                    while 'x' in self.func:  # Ставим скобки около всех иксов
                        a = self.func.index('x')
                        if 1 < a < len(self.func) - 1 and self.func[a - 1] == '(' and self.func[a + 1] == ')':
                            self.new_func += self.func[:a + 1] + ')'
                            self.func = self.func[a + 2:]
                        else:
                            self.new_func += self.func[:a] + '(x)'
                            self.func = self.func[a + 1:]
                    self.new_func += self.func

                self.func = self.new_func
                self.new_func = ''

                while '(' in self.func:  # Ставим * перед скобками
                    a = self.func.index('(')
                    if (self.func[a - 1].isdigit() or self.func[a - 1] == ')') and a > 0:
                        self.new_func += self.func[:a] + '*' + '('
                        self.func = self.func[a + 1:]
                    else:
                        self.new_func += self.func[:a + 1]
                        self.func = self.func[a + 1:]
                self.new_func += self.func

                prev_x = -48
                while True:
                    try:
                        prev_y = eval(self.new_func.replace('x', str(prev_x)))
                        break
                    except Exception:
                        prev_x += 0.2
                        continue

                for i in range(1920):  # Берём 1/5 от каждой клетки (5 пикс)
                    x = prev_x + 0.2
                    try:
                        y = eval(self.new_func.replace('x', str(x)))
                        if abs(y) > 100:
                            prev_x = x
                            prev_y = y
                            continue
                        draw.line(((prev_x * 25) + 951, 549 - (prev_y * 25), (x * 25) + 951, 549 - (y * 25)),
                                  fill=self.filling, width=self.width)
                        prev_x = x
                        prev_y = y
                    except Exception:
                        prev_x += 0.2
                        continue
                im.save('field.jpg')

                con = sqlite3.connect('database.db')
                cur = con.cursor()
                colour = cur.execute(f"""SELECT id FROM colours WHERE name='{self.filling}'""").fetchone()
                colour = [str(i) for i in colour]
                colour = ''.join(colour)
                cur.execute(f"""INSERT INTO functions(function, id) VALUES('{self.new_func}', '{colour}')""")
                con.commit()
                con.close()

                d = {'number': self.cur_num, 'function': self.new_func, 'colour': self.filling}

                self.pixmap = QPixmap('field.jpg')
                self.imgGraphLbl.setPixmap(self.pixmap)  # 38
                with open('cur_graphs.csv', 'w', newline='', encoding="utf8") as f:
                    writer = csv.DictWriter(f, fieldnames=self.fieldnames, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
                    writer.writeheader()
                    writer.writerow(d)
                self.cur_num += 1
            except Exception:
                msg_box = QMessageBox()
                msg_box.setWindowTitle("Error")
                msg_box.setText('Internal error.')
                msg_box.exec_()

    def adding_graph(self):
        self.func = self.inputFunc.text()
        self.func = self.func.replace(' ', '')
        if not self.inputFunc.text():
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Error")
            msg_box.setText('Function input field is empty.')
            msg_box.exec_()
        elif not self.func[:2] == 'y=':
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Error")
            msg_box.setText("""Function should start with 'y='.""")
            msg_box.exec_()
        elif not (('(' in self.func or ')' in self.func and (self.func.count('(') == 1 and self.func.count(')') == 1
                                                             and self.func.find('(') < self.func.find(')'))) or not
                  ('|' in self.func and self.func.count('|') % 2 == 0)):
            msg_box = QMessageBox()
            msg_box.setWindowTitle("Error")
            msg_box.setText("""Incorrect parentheses""")
            msg_box.exec_()
        else:
            try:
                self.func = self.func.replace('^', '**')
                im = Image.open('field.jpg')
                draw = ImageDraw.Draw(im)

                self.func = self.func[2:]
                self.filling = self.comboBox.currentText()

                self.new_func = ''
                while 'x' in self.func:  # Ставим скобки около всех иксов
                    a = self.func.index('x')
                    if 1 < a < len(self.func) - 1 and self.func[a - 1] == '(' and self.func[a + 1] == ')':
                        self.new_func += self.func[:a + 1] + ')'
                        self.func = self.func[a + 2:]
                    else:
                        self.new_func += self.func[:a] + '(x)'
                        self.func = self.func[a + 1:]
                self.new_func += self.func

                self.func = self.new_func
                self.new_func = ''

                while '(' in self.func:  # Ставим * около всех скобок
                    a = self.func.index('(')
                    if (self.func[a - 1].isdigit() or self.func[a - 1] == ')') and a > 0:
                        self.new_func += self.func[:a] + '*' + '('
                        self.func = self.func[a + 1:]
                    else:
                        self.new_func += self.func[:a + 1]
                        self.func = self.func[a + 1:]
                self.new_func += self.func

                prev_x = -48
                while True:
                    try:
                        prev_y = eval(self.new_func.replace('x', str(prev_x)))
                        break
                    except Exception:
                        prev_x += 0.2
                        continue

                for i in range(1920):  # Берём 1/5 от каждой клетки (5 пикс)
                    x = prev_x + 0.2
                    try:
                        y = eval(self.new_func.replace('x', str(x)))
                        if abs(y) > 100:
                            prev_x = x
                            prev_y = y
                            continue
                        draw.line(((prev_x * 25) + 951, 549 - (prev_y * 25), (x * 25) + 951, 549 - (y * 25)),
                                  fill=self.filling, width=self.width)
                        prev_x = x
                        prev_y = y
                    except Exception:
                        prev_x += 0.2
                        continue
                im.save('field.jpg')

                self.pixmap = QPixmap('field.jpg')
                self.imgGraphLbl.setPixmap(self.pixmap)  # 38
                d = {'number': self.cur_num, 'function': self.new_func, 'colour': self.filling}

                with open('cur_graphs.csv', 'a', newline='', encoding="utf8") as f:
                    writer = csv.DictWriter(f, fieldnames=self.fieldnames, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
                    writer.writerow(d)
                self.cur_num += 1
            except Exception:
                msg_box = QMessageBox()
                msg_box.setWindowTitle("Error")
                msg_box.setText('Internal error.')
                msg_box.exec_()

    def draw_parabola(self):  # Рисование параболы
        self.inputFunc.setText('y=x^2')
        self.draw_graph_and_save()

    def draw_hyperbola(self):  # Рисование гиперболы
        self.inputFunc.setText('y=1/x')
        self.draw_graph_and_save()

    def draw_linear(self):  # Рисование линейной функции
        self.inputFunc.setText('y=x')
        self.draw_graph_and_save()

    def init_field(self):  # Инициализация поля
        im = Image.new('RGB', (1920, 1080), (255, 255, 255))
        draw = ImageDraw.Draw(im)
        for i in range(25, 1921, 25):
            draw.line((i, 0, i, 1080), fill='black', width=3)

        for i in range(25, 1080, 25):
            draw.line((0, i, 1920, i), fill='black', width=3)

        a = 1080 // 2 + 9
        b = 1920 // 2 - 9
        draw.line((0, a, 1980, a), fill='black', width=6)
        draw.line((b, 0, b, 1080), fill='black', width=6)
        im.save('field.jpg')

    def errase(self):  # Стирания поля
        self.init_field()
        self.pixmap = QPixmap('origin_field.jpg')
        self.imgGraphLbl.setPixmap(self.pixmap)

    def option(self):  # Открытие настроек
        global s
        s = Settings()
        s.show()

    def current_graphs(self):  # Открытие текущих графиков
        global cur_graph
        cur_graph = CurrentGraphs()
        cur_graph.show()

    def my_graphs(self):  # Открытие всех графиков
        global my_graph
        my_graph = MyGraphs()
        my_graph.show()


class MyGraphs(QWidget, MyGraphs_Ui):  # Все когда либо созданные графики
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('My graphs')

        self.addGraph.clicked.connect(self.get_graph_from_table) # подключаем кнопки
        self.backBtn.clicked.connect(self.close_win)
        self.deleteallBtn.clicked.connect(self.delete_all)
        self.tableWidget.itemChanged.connect(self.change_item)

        con = sqlite3.connect('database.db')  # Подключаемся к БД
        cur = con.cursor()

        self.tableWidget.setColumnCount(2)  # Добавляем данные в таблицу
        self.tableWidget.setRowCount(0)
        res = cur.execute(
            """SELECT function, name FROM functions LEFT JOIN colours ON functions.id=colours.id""").fetchall()
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))
        lbls = ['Name', 'Colour']
        self.tableWidget.setHorizontalHeaderLabels(lbls)

        con.close()

    def change_item(self, item):
        num = item.row() + 1
        con = sqlite3.connect('database.db')
        cur = con.cursor()
        if item.column() == 0:
            cur.execute(f"""UPDATE functions SET function='{item.text()}' WHERE number={num}""")
        elif item.column() == 1:
            cur.execute(f"""UPDATE functions SET id=(SELECT id FROM colours WHERE name='{item.text()}') WHERE number={num}""")
        con.commit()
        con.close()

    def close_win(self):
        self.close()

    def delete_all(self):  # Стереть всё
        a = QMessageBox()
        res = a.question(self, '', 'Are you sure you want to delete all graphs?', a.Yes | a.No)
        a.show()

        if res == a.Yes:  # Если да, то удаляем все записи
            con = sqlite3.connect('database.db')  # Подключаемся к БД
            cur = con.cursor()

            cur.execute("""DELETE FROM functions""")  # Удаляем записи
            cur.execute("""UPDATE SQLITE_SEQUENCE SET seq = 0 WHERE name = 'functions'""")  # Обнуление автоинкремента
            con.commit()

            self.tableWidget.setColumnCount(2)
            self.tableWidget.setRowCount(0)
            lbls = ['Name', 'Colour']
            self.tableWidget.setHorizontalHeaderLabels(lbls)

            con.close()
        else:
            a.close()

    def get_graph_from_table(self):
        global ex
        graphs_to_draw = []
        colours = []

        for item in self.tableWidget.selectedItems():
            graphs_to_draw.append(item.text())
            con = sqlite3.connect('database.db')
            cur = con.cursor()
            a = cur.execute(f"""SELECT name FROM colours JOIN functions ON 
            colours.id=functions.id WHERE number={item.row() + 1}""").fetchone()
            colours.append(a[0])
            con.close()

        for i in range(len(graphs_to_draw)):
            ex.inputFunc.setText(f'y={graphs_to_draw[i]}')
            ex.comboBox.setCurrentText(str(colours[i]))
            ex.adding_graph()


class CurrentGraphs(QWidget, CurGraphs_Ui):  # Окно для редактирования текущих графиков
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Current graphs')
        self.changes = []

        self.backBtn.clicked.connect(self.back)  # Настройка кнопок
        self.delBtn.clicked.connect(self.delete)

        res = []
        with open('cur_graphs.csv') as csvfile:  # Читаем существующие графики из csv
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            labels = next(reader)
            for i in reader:
                if i:
                    res.append(i)

        self.tableWidget.setColumnCount(3)  # Отображаем данные в таблице
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(labels)

        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))

    def delete(self):  # Удалить выбранные элементы с координатного поля
        global ex
        number = [i.row() for i in self.tableWidget.selectedItems()]
        new_graphs = []
        with open('cur_graphs.csv') as csvfile:  # Читаем существующие графики из csv
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            labels = next(reader)
            for i in reader:
                if i and int(i[0]) - 1 not in number:
                    new_graphs.append(i)

        with open('cur_graphs.csv', 'w') as f:  # Перезаписываем csv файл
            writer = csv.DictWriter(f, fieldnames=ex.fieldnames, delimiter=';')
            writer.writeheader()

        for i in new_graphs:
            ex.inputFunc.setText(f'y={i[1]}')
            ex.comboBox.setCurrentText(i[2])
            ex.init_field()
            ex.adding_graph()

        res = []
        with open('cur_graphs.csv') as csvfile:  # Читаем существующие графики из csv
            reader = csv.reader(csvfile, delimiter=';', quotechar='"')
            labels = next(reader)
            for i in reader:
                if i:
                    res.append(i)

        self.tableWidget.clear()
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        self.tableWidget.setHorizontalHeaderLabels(labels)

        for i, row in enumerate(res):
            self.tableWidget.setRowCount(
                self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(
                    i, j, QTableWidgetItem(str(elem)))

    def back(self):
        self.close()


class Settings(QWidget, Settings_Ui):  # Окно с настройками
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Settings')

        self.horizontalSlider.setRange(1, 8)  # Настройка слайдера
        self.horizontalSlider.setTickPosition(QSlider.TickPosition.TicksAbove)
        self.horizontalSlider.setTickInterval(1)
        self.init_value()

        self.applyBtn.clicked.connect(self.apply_chang) # Настройка кнопок
        self.defaultBtn.clicked.connect(self.standart_settings)

    def init_value(self):  # Текущая ширина графика
        global ex
        self.horizontalSlider.setValue(ex.width)

    def apply_chang(self):  # Подтверждение изменений
        global ex
        ex.width = self.horizontalSlider.value()
        n = QPixmap('origin_field.jpg')
        ex.imgGraphLbl.setPixmap(n)
        self.close()

    def standart_settings(self):  # Установка стандартных настроек
        global ex
        self.horizontalSlider.setValue(4)
        ex.width = 4


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GraphBuilder()
    ex.show()
    sys.exit(app.exec_())
