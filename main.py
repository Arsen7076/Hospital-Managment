from frontend import *
from backend import *
from PyQt5.QtCore import pyqtSignal, QPropertyAnimation, QEasingCurve


class MainWindow(QWidget, Ui_Form):
    keyPressed = pyqtSignal(str)

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.dragPos = None
        self._animate = None

        self.setWindowIcon(QIcon("../../Downloads/icons/medicine.png"))
        self.setupUi(self)  # // UI Integration
        self.remove_title_bar()  # // TitleBar removed

        self.menuBar.mouseMoveEvent = self.move_win
        # -------------------------------------------------------------------------------------------------------------#
        #                                            Size Police                                                       #
        # -------------------------------------------------------------------------------------------------------------#
        self.gripSize = 16
        self.grips = []
        for i in range(4):
            grip = QSizeGrip(self)
            grip.resize(self.gripSize, self.gripSize)
            self.grips.append(grip)

        # -------------------------------------------------------------------------------------------------------------#
        #                                              Backend                                                         #
        # -------------------------------------------------------------------------------------------------------------#
        self.exp = QGroupBox()

        self.exp.setObjectName("Lists")
        self.back = Backend()
        self.back.update()
        # -------------------------------------------------------------------------------------------------------------#
        #                                       Buttons -> Frame Animation                                             #
        # -------------------------------------------------------------------------------------------------------------#

        self.expandBtn.clicked.connect(lambda: self.property_changed(self.expandBtn, self.optionBar, 300,
                                                                     b"minimumWidth"))
        self.settingBtn.clicked.connect(lambda: self.back.setting())

        self.show_list.clicked.connect(lambda: self.show_list_fnc())
        self.data_update.clicked.connect(lambda: self.back.update_start())
        self.insert.clicked.connect(lambda: self.back.insert_data())
        self.calculate.clicked.connect(lambda: self.back.calculate())
        self.search.clicked.connect(lambda: self.back.search_fnc())
        self.exit.clicked.connect(lambda: self.close())

        # Show list
        self.department.clicked.connect(lambda: self.back.show_info(0))
        self.service.clicked.connect(lambda: self.back.show_info(1))
        self.staf.clicked.connect(lambda: self.back.show_info(2))
        self.patients.clicked.connect(lambda: self.back.show_info(3))
        self.room.clicked.connect(lambda: self.back.show_info(4))
        self.all.clicked.connect(lambda: self.back.all())
        # -------------------------------------------------------------------------------------------------------------#
        #                                                Chasten Set zen                                               #
        # -------------------------------------------------------------------------------------------------------------#
        self.set_shadow(self.menuBar, 10, "#00d0ff", 3, 0)  # // MenuBar
        self.set_shadow(self.optionBar, 20, "#00d0ff", 0, 0)  # // OptionBar
        self.set_shadow(self.groupBox, 20, "#191c22", 0, 8)
        self.set_shadow(self, 20, "#00e6ff", 0, 0)  # // MainWindow//

    # ----------------------------------------- Fester und Widget Eigenstate --------------------------------------#
    # -----------------------------------------------------------------------------------------------------------------#
    # Fester Status Normal und Maximized

    def show_list_fnc(self):
        self.expandBtn.toggle()
        self.property_changed(self.expandBtn, self.optionBar, 300, b"minimumWidth")

    def restoreWindow(self):
        if self.restoreBtn.isChecked():
            self.showMaximized()
        else:
            self.showNormal()

    # Fester between
    def move_win(self, event):
        if event.buttons() == Qt.LeftButton:
            self.move(self.pos() + event.globalPos() - self.dragPos)
            self.dragPos = event.globalPos()
            event.accept()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    # TitleBar efferent
    def remove_title_bar(self):
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

    # Animation der Frames
    def property_changed(self, btn, widget, end, prop):

        self._animate = QPropertyAnimation(widget, prop)
        self._animate.setDuration(1000)
        self._animate.setEasingCurve(QEasingCurve.OutBounce)
        if btn.isChecked():
            self._animate.setEndValue(end)
            self._animate.start()
        else:
            self._animate.setEndValue(0)
            self._animate.start()

    # Schachter initialising
    @staticmethod
    def set_shadow(widget, radius, color, x, y):
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(radius)
        shadow.setXOffset(x)
        shadow.setYOffset(y)
        shadow.setColor(QColor(color))
        widget.setGraphicsEffect(shadow)

    # Boisterousness passenger
    def resizeEvent(self, event):
        # QMainWindow.resizeEvent(self, event)
        rect = self.rect()
        self.grips[1].move(rect.right() - self.gripSize, 0)
        self.grips[2].move(
            rect.right() - self.gripSize, rect.bottom() - self.gripSize)
        self.grips[3].move(0, rect.bottom() - self.gripSize)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    mw = MainWindow()

    mw.show()
    app.exec()
