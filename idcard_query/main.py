import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt
from id_validator import validator


class IdCardOperation(QWidget):
    """QWdidget派生桌面应用程序窗口类"""

    def __init__(self, title='IDCard information'):
        super(IdCardOperation, self).__init__()
        # 初始化界面
        self.initUI(title)
        self.show()

    def initUI(self, title):
        root_path = os.path.dirname(__file__)
        # 设置标题图标
        self.setWindowTitle(title)
        self.setWindowIcon(QIcon(os.path.join(root_path, 'resources/yuan.jpg')))
        self.setFixedSize(1000, 800)
        # 定义控件
        self.birthday_label = QLabel('出生日期:')
        self.birthday_line_edit = QLineEdit('1997-03-01')
        self.address_label = QLabel('地址:')
        self.address_line_edit = QLineEdit('成都')
        self.sex_label = QLabel('性别:')
        # 单选
        self.sex_comboBox = QComboBox()
        self.sex_comboBox.addItem('男')
        self.sex_comboBox.addItem('女')
        self.random_button = QPushButton('随机')
        self.idcard_label = QLabel('身份证号码:')
        self.idcard_line_edit = QLineEdit()
        self.query_button = QPushButton('查询')
        self.idcard_info_label = QLabel('身份证信息:')
        self.idcard_info_text_edit = QTextEdit()
        # 创建网格布局管理器
        self.grid = QGridLayout()
        # 添加控件 addWidget(QWidget, row, col, r, c, alignment) - 在row行col列添加控件，占r行c列，并设置对齐方式
        self.grid.addWidget(self.birthday_label, 0, 0, 1, 1)
        self.grid.addWidget(self.birthday_line_edit, 0, 1, 1, 3)
        self.grid.addWidget(self.address_label, 0, 4, 1, 1)
        self.grid.addWidget(self.address_line_edit, 0, 5, 1, 3)
        self.grid.addWidget(self.sex_label, 0, 8, 1, 1)
        self.grid.addWidget(self.sex_comboBox, 0, 9, 1, 2)
        self.grid.addWidget(self.random_button, 0, 11, 1, 1)
        self.grid.addWidget(self.idcard_label, 1, 0, 1, 1)
        self.grid.addWidget(self.idcard_line_edit, 1, 1, 1, 10)
        self.grid.addWidget(self.query_button, 1, 11, 1, 1)
        self.grid.addWidget(self.idcard_info_label, 2, 0, 1, 1)
        self.grid.addWidget(self.idcard_info_text_edit, 3, 0, 1, 12)
        # 添加点击事件
        self.query_button.clicked.connect(self.get_id_card_info)
        self.random_button.clicked.connect(self.random_id_card)
        # 设置布局管理器
        self.setLayout(self.grid)

    def get_id_card_info(self):
        id_number = self.idcard_line_edit.text()
        if not validator.is_valid(id_number):
            print('身份证无效')
            self.idcard_info_text_edit.setText('身份证信息:\n身份证无效')
            self.idcard_info_text_edit.setStyleSheet('color:red')
            return
        idcard_info = validator.get_info(id_number)
        info_key = {
            'address_code': '地址码',
            'abandoned': '地址码是否废弃',
            'address': '地址',
            'birthday_code': '出生日期',
            'constellation': '星座',
            'chinese_zodiac': '生肖',
            'sex': '性别',
        }
        info_result = '身份证信息:'
        for key, value in idcard_info.items():
            print('key:value', key, value)
            if key not in info_key:
                continue
            else:
                if key == 'abandoned':
                    if value == 1:
                        info_result += f'{info_key.get(key)}:地址码无效\n'
                    else:
                        info_result += f'{info_key.get(key)}:地址码有效\n'
                else:
                    info_result += f'{info_key.get(key)}:{value}\n'
        print('身份证有效')
        print(info_result)
        self.idcard_info_text_edit.setText(info_result)
        self.idcard_info_text_edit.setStyleSheet('color:green')

    def random_id_card(self):
        birthday = self.birthday_line_edit.text().replace('-', '')
        birthday = birthday if birthday else None
        address = self.address_line_edit.text()
        address = address if address else None
        # 获取单选值
        sex = self.sex_comboBox.currentText()
        sex = 1 if sex == '男' else 0
        try:
            id_ = validator.fake_id(True, address, birthday, sex)
        except:
            id_ = validator.fake_id()
        self.idcard_line_edit.setText(id_)


if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建应用程序,接受命令行参数
    widget = IdCardOperation(title='身份证')  # 创建窗口
    widget.show()
    sys.exit(app.exec())  # 应用程序主循环结束后，调用sys.exit()方法清理现场
