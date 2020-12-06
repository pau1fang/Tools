from window import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication,QFileDialog
from PyQt5 import QtGui
import sys
import _thread
import time
import conversion


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.setupUi(self)
        self.centralwidget.setAutoFillBackground(True)
        palette = QtGui.QPalette()
        palette.setBrush(QtGui.QPalette.Background, QtGui.QBrush(
            QtGui.QPixmap("img/bg.png")
        ))
        self.centralwidget.setPalette(palette)
        input_img = QtGui.QPixmap("img/input_test.png")
        self.input_img.setPixmap(input_img)

        export_img = QtGui.QPixmap("img/output_test.png")
        self.export_img.setPixmap(export_img)

    def openfile(self):
        openfile_name = QFileDialog.getOpenFileName()
        print(openfile_name)
        if openfile_name[0] != "":
            self.input_path = openfile_name[0]
            self.show_input_img(self.input_path)

    def show_input_img(self, file_path):
        input_img = QtGui.QPixmap(file_path)
        self.input_img.setPixmap(input_img)


    def start_conversion(self):
        if hasattr(main, "input_path"):
            self.gif = QtGui.QMovie("img/loding.gif")
            self.loding.setMovie(self.gif)
            self.gif.start()
            _thread.start_new_thread(lambda: self.is_conversion(main.input_path), ())
        else:
            print("没有选择指定的图片路径！")

    def is_conversion(self, file_path):
        t = str(int(time.time()))
        export_path = "export_img\\export_img" + t + ".png"
        input_char = main.textEdit.toPlainText()
        definition = main.comboBox.currentText()
        is_over = conversion.picture_conversion(file_path, export_path, input_char, definition)
        if is_over == False:
            self.loding.clear()
            main.show_export_img(export_path)

    def show_export_img(self, file_path):
        export_img = QtGui.QPixmap(file_path)
        self.export_img.setPixmap(export_img)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    main.pushButton_input.clicked.connect(main.openfile)
    main.pushButton_conversion.clicked.connect(main.start_conversion)
    main.show()
    sys.exit(app.exec_())