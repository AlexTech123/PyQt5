# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtWidgets


class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.x = 1
        self.setWindowTitle("Блокировка и удаление обработчика")
        self.resize(300, 150)
        self.label = QtWidgets.QLabel()
        self.label.setObjectName("label")
        self.label.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.button1 = QtWidgets.QPushButton("Нажми меня")
        self.button2 = QtWidgets.QPushButton("Блокировать")
        self.button3 = QtWidgets.QPushButton("Разблокировать")
        self.button4 = QtWidgets.QPushButton("Удалить обработчик")
        self.button5 = QtWidgets.QPushButton("Создать обработчик")
        self.button3.setEnabled(False)
        self.button5.setEnabled(False)
        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.label)
        vbox.addWidget(self.button1)
        vbox.addWidget(self.button2)
        vbox.addWidget(self.button3)
        vbox.addWidget(self.button4)
        vbox.addWidget(self.button5)
        self.setLayout(vbox)
        self.button1.clicked.connect(self.on_clicked_button1)
        self.button2.clicked.connect(self.on_clicked_button2)
        self.button3.clicked.connect(self.on_clicked_button3)
        self.button4.clicked.connect(self.on_clicked_button4)
        self.button5.clicked.connect(self.on_clicked_button5)

    @QtCore.pyqtSlot()
    def on_clicked_button1(self):
        #print(self.x)
        self.label.setText(str(self.x))
        self.x += 1

    @QtCore.pyqtSlot()
    def on_clicked_button2(self):
        #print("---Обработчик блокирован---")
        self.label.setText("Обработчик блокирован")
        self.button1.blockSignals(True)
        self.button2.setEnabled(False)
        self.button3.setEnabled(True)

    @QtCore.pyqtSlot()
    def on_clicked_button3(self):
        #print("---Обработчик разблокирован---")
        self.label.setText("Обработчик разблокирован")
        self.button1.blockSignals(False)
        self.button2.setEnabled(True)
        self.button3.setEnabled(False)

    @QtCore.pyqtSlot()
    def on_clicked_button4(self):
        #print("---Обработчик удален---")
        self.label.setText("Обработчик удален")
        self.button1.clicked.disconnect(self.on_clicked_button1)
        self.button2.setEnabled(False)
        self.button3.setEnabled(False)
        self.button4.setEnabled(False)
        self.button5.setEnabled(True)

    @QtCore.pyqtSlot()
    def on_clicked_button5(self):
        self.x = 1
        #print("---Обработчик создан---")
        self.label.setText("Обработчик создан")
        self.button1.clicked.connect(self.on_clicked_button1)
        self.button4.setEnabled(True)
        self.button3.setEnabled(False)
        self.button2.setEnabled(True)
        self.button5.setEnabled(False)
        self.button1.blockSignals(False)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setStyleSheet("QLabel#label {font-size: 17px}")
    window.show()
    sys.exit(app.exec_())
