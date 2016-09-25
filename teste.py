# from core.bytes import Bytes
# from game.message.server.S_EACH_SKILL_RESULT import S_EACH_SKILL_RESULT
# from util import tipo
#
#
# data = Bytes([1, 2, 3, 4, 5])
#
# print(str(S_EACH_SKILL_RESULT).split('.')[3])

# import sys
# from PyQt4.QtCore import QSize, Qt
# from PyQt4.QtGui import QMainWindow, QStyle, qApp, QApplication
# 
# class mymainwindow(QMainWindow):
#     def __init__(self):
#         QMainWindow.__init__(self)
#         self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.X11BypassWindowManagerHint)
#         self.setWindowOpacity(0.5)
#         self.setGeometry(QStyle.alignedRect(Qt.LeftToRight, Qt.AlignCenter, QSize(300, 50), qApp.desktop().availableGeometry()))
# 
#     def mousePressEvent(self, event):
#         qApp.quit()
# 
# app = QApplication(sys.argv)
# mywindow = mymainwindow()
# mywindow.show()
# app.exec_()
