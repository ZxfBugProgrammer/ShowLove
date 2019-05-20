import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QDesktopWidget, QMenu, qApp, QMessageBox
from PyQt5.QtGui import QPixmap, QPainter, QCursor
import random
import pygame
import UI_FORM
import Login_From
import Next_UI
import ShowPicture
import Dialog_UI1


class LoginWindow(QWidget, Login_From.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initAppearance()

    def initAppearance(self):
        # 设置窗口的样式
        self.pix = QPixmap('Loginbeijing.jpg')  # 蒙版
        windowWidth = 960
        windowHeight = 450
        self.resize(windowWidth, windowHeight)
        self.setFixedSize(self.width(), self.height())
        self.pix = self.pix.scaled(int(windowWidth), int(windowHeight))
        self.center()
        # 设置按钮的样式
        self.pushButton.setStyleSheet('QPushButton{border-image:url(button.png)}')
        tempPixmap = QPixmap("button.png").scaled(self.pushButton.size())
        self.pushButton.setMask(tempPixmap.mask())

    def paintEvent(self, event):  # 绘制窗口
        paint = QPainter(self)
        paint.drawPixmap(0, 0, self.pix.width(), self.pix.height(), self.pix)

    def closeEvent(self, event):  # 关闭窗口触发以下事件
        name = ("陈美娟")
        if self.lineEdit.text() in name:
            return
        reply = QMessageBox.question(self, 'Are you kidding me?', '你确定要退出吗?       ', QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def onClicked(self):
        name = ("陈美娟")
        tempText = self.lineEdit.text()
        if tempText in name:
            QMessageBox.information(self, "Prefect", "您通过了验证！", QMessageBox.Yes)
            self.close()
            nextwin.show()
        else:
            QMessageBox.critical(self, "GG", "您没有通过验证！")
            self.lineEdit.setText("请在此输入")

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


class NextWindow(QWidget, Next_UI.Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initAppearance()

    def initAppearance(self):
        # 设置窗口的样式
        self.pix = QPixmap('next.jpg')
        windowWidth = 432
        windowHeight = 768
        self.resize(windowWidth, windowHeight)
        self.pix = self.pix.scaled(int(windowWidth), int(windowHeight))
        # 设置无边框
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.center()
        # 设置按钮的样式
        self.pushButton.setStyleSheet('QPushButton{border-image:url(beijing.png)}')
        tempPixmap = QPixmap("beijing.png").scaled(self.pushButton.size())
        self.pushButton.setMask(tempPixmap.mask())

    def paintEvent(self, event):  # 绘制窗口
        paint = QPainter(self)
        paint.drawPixmap(0, 0, self.pix.width(), self.pix.height(), self.pix)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    def contextMenuEvent(self, event):
        cmenu = QMenu(self)
        quitAct = cmenu.addAction("Quit")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))
        if action == quitAct:
            qApp.quit()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def onClicked(self):
        self.close()
        pictureWin.show()


class PictureWindow(QWidget, ShowPicture.Ui_Form):
    cnt = 0

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initAppearance()

    def initAppearance(self):
        # 设置窗口的样式
        self.pix = QPixmap('0.jpg')
        windowWidth = 432
        windowHeight = 768
        self.resize(windowWidth, windowHeight)
        self.pix = self.pix.scaled(int(windowWidth), int(windowHeight))
        # 设置无边框
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.center()
        # 设置按钮的样式
        self.pushButton.setStyleSheet('QPushButton{border-image:url(button.png)}')
        tempPixmap = QPixmap("button.png").scaled(self.pushButton.size())
        self.pushButton.setMask(tempPixmap.mask())

    def paintEvent(self, event):  # 绘制窗口
        paint = QPainter(self)
        paint.drawPixmap(0, 0, self.pix.width(), self.pix.height(), self.pix)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    def contextMenuEvent(self, event):
        cmenu = QMenu(self)
        quitAct = cmenu.addAction("Quit")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))
        if action == quitAct:
            qApp.quit()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def onClicked(self):
        if self.cnt < 4:
            self.cnt = self.cnt + 1
            self.pix = QPixmap(str(self.cnt) + '.jpg')
            windowWidth = 432
            windowHeight = 768
            self.resize(windowWidth, windowHeight)
            self.pix = self.pix.scaled(int(windowWidth), int(windowHeight))
            self.close()
            self.show()
        else:
            self.close()
            win.show()


class PixWindow(QWidget, UI_FORM.Ui_Form):  # 不规则窗体
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initAppearance()
        self.setMusic()

    def initAppearance(self):
        # 设置窗口的样式
        self.pix = QPixmap('beijing.png')  # 蒙版
        windowWidth = 700
        windowHeight = 700
        self.resize(windowWidth, windowHeight)
        self.pix = self.pix.scaled(int(windowWidth), int(windowHeight))
        self.setMask(self.pix.mask())
        # 设置无边框
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.center()
        # 设置按钮的样式
        self.pushButton.setStyleSheet('QPushButton{border-image:url(button.png)}')
        tempPixmap = QPixmap("button.png").scaled(self.pushButton.size())
        self.pushButton.setMask(tempPixmap.mask())

    def paintEvent(self, event):  # 绘制窗口
        paint = QPainter(self)
        paint.drawPixmap(0, 0, self.pix.width(), self.pix.height(), self.pix)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    def contextMenuEvent(self, event):
        cmenu = QMenu(self)
        quitAct = cmenu.addAction("Quit")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))
        if action == quitAct:
            qApp.quit()

    def setMusic(self):
        pygame.mixer.init()
        pygame.mixer.music.load(r"music.mp3")
        pygame.mixer.music.play(loops=-1)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def showLove(self):
        dialog1.pushButton_2.move(370, 240)
        dialog1.show()


class Dialog1(QWidget, Dialog_UI1.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.center()
        self.pushButton_2.raise_()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def accept(self):
        self.close()
        dialog2.pushButton_2.move(370, 240)
        dialog2.show()

    def reject(self):
        x = random.randint(0, 600)
        y = random.randint(0, 300)
        self.pushButton_2.move(x, y)


class Dialog2(QWidget, Dialog_UI1.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.center()
        self.pushButton_2.raise_()
        self.label.setText("新的一年，新的开始,往后余生\n不论贫穷还是富贵，健康或是疾病\n你都愿意跟我一直走下去吗？")
        self.pushButton.setText("我愿意")
        self.pushButton_2.setText("才不呢")

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def accept(self):
        self.close()
        dialog3.pushButton_2.move(370, 240)
        dialog3.show()

    def reject(self):
        x = random.randint(0, 600)
        y = random.randint(0, 300)
        self.pushButton_2.move(x, y)


class Dialog3(QWidget, Dialog_UI1.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.center()
        self.pushButton_2.raise_()
        self.label.setText("感谢有你的陪伴\n你在，我在\n就是海枯石烂")
        self.pushButton.setText("Agree")
        self.pushButton_2.setText("Disagree")

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def accept(self):
        self.close()
        dialog4.pushButton_2.move(370, 240)
        dialog4.show()

    def reject(self):
        x = random.randint(0, 600)
        y = random.randint(0, 300)
        self.pushButton_2.move(x, y)


class Dialog4(QWidget, Dialog_UI1.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.center()
        self.pushButton_2.raise_()
        self.label.setText("生日快乐，my baby\nLove you")
        self.pushButton.setText("Love you")
        self.pushButton_2.setText("~哼~")

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def accept(self):
        self.close()

    def reject(self):
        x = random.randint(0, 600)
        y = random.randint(0, 300)
        self.pushButton_2.move(x, y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    login = LoginWindow()
    nextwin = NextWindow()
    win = PixWindow()
    pictureWin = PictureWindow()
    dialog1 = Dialog1()
    dialog2 = Dialog2()
    dialog3 = Dialog3()
    dialog4 = Dialog4()
    login.show()
    sys.exit(app.exec_())
