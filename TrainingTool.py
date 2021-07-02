import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtWidgets import QFileDialog
from PySide6.QtGui import QImage, QPixmap



from UiForTool.TrainingToolUi import Ui_MainWindow


class MainToolWindow(QMainWindow):
    def __init__(self):
        super(MainToolWindow, self).__init__()
        self.tool_ui = Ui_MainWindow()
        self.tool_ui.setupUi(self)
        self.tool_ui.StartTraining.clicked.connect(self.start_training)
        self.tool_ui.NewImageSetter.clicked.connect(self.set_new_image)

    def start_training(self):
        pass

    def set_new_image(self):
        path_for_file, filetype = self.get_file_name()
        pixmap = QPixmap(QImage(path_for_file))
        self.tool_ui.imageShower.setPixmap(pixmap)
        self.tool_ui.imageShower.move(100,100)

    def get_file_name(self):
         return QFileDialog.getOpenFileName(None, 'Open File', './', "Image (*.png *.jpg *jpeg)")





app = QApplication(sys.argv)

window = MainToolWindow()
window.show()

sys.exit(app.exec())