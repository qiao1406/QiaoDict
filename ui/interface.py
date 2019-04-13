import sys
from data import data_process
from definition import word
from ui.uiform import Ui_Form
from ui.dialog import Ui_Dialog
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Dialog(QtWidgets.QWidget, Ui_Dialog):

    def __init__(self):
        super(Dialog, self).__init__()
        self.setupUi(self)
        self.set_actions()

    def set_actions(self):
        """
        为部分组件添加动作
        :return:
        """
        self.pushButton.clicked.connect(self.insert_word)  # “提交”按钮

    def collect_info(self):
        """
        收集对话框中的信息，生成 Word 对象
        :return: Word, 要插入的单词
        """
        name = self.te_word.toPlainText()
        mean = word.Meaning(self.te_mean.toPlainText(), self.comboBox.currentText())
        sen = word.Sentence(self.te_enges.toPlainText(), self.te_chnes.toPlainText())
        return word.Word(name, [mean], [sen])

    def insert_word(self):
        """
        :return:
        """
        res = data_process.insert_word(self.collect_info())
        s = '单词添加成功' if res else '单词已存在，添加失败'
        QMessageBox.information(self, '通知', s, QMessageBox.Yes)


class Window(QtWidgets.QWidget, Ui_Form):

    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)
        self.dialog = None
        self.set_actions()

    def set_actions(self):
        """
        为部分组件设置动作
        """
        self.pushButton.clicked.connect(self.look_up_word)
        self.pushButton_2.clicked.connect(self.wakeup_dialog)
        self.pushButton_3.clicked.connect(self.clear_check_box)
        self.pushButton_4.clicked.connect(self.word_list)
        self.pushButton_5.clicked.connect(self.clear_console)

    def look_up_word(self):
        """
        查询按钮从输入框中获取要查询的单词，并将结果输出
        """
        name = self.textEdit.toPlainText()
        result = data_process.look_for_dict(name)
        self.plainTextEdit.insertPlainText(result)

    def clear_check_box(self):
        """
        清空查询输入框
        """
        self.textEdit.clear()

    def clear_console(self):
        """
        清空 Console
        """
        self.plainTextEdit.clear()

    def word_list(self):
        """
        查询单词表
        """
        for w in data_process.get_all_words():
            self.plainTextEdit.insertPlainText(str(w))

    def wakeup_dialog(self):
        """
        唤醒对话框
        :return:
        """
        self.dialog = Dialog()
        self.dialog.show()


def run():
    app = QtWidgets.QApplication(sys.argv)
    w = Window()
    w.show()
    sys.exit(app.exec_())


run()
