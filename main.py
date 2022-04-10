# 这是一个示例 Python 脚本。
from PyQt5.QtWidgets import QApplication,QWidget
import sys
# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


def print_hi(name):
    # 在下面的代码行中使用断点来调试脚本。
    print(f'Hi, {name}')  # 按 Ctrl+F8 切换断点。


# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')
    app =QApplication(sys.argv)     #创建QApplication
    w =QWidget()                    #创建一个窗口
    w.resize(600,400)
    w.move(0,0)
    w.setWindowTitle("串口调试工具")
    w.show()
    sys.exit(app.exec())                #进入主循环程序