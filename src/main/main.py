from PyQt6.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QLabel, QApplication
from PyQt6.QtGui import QPixmap
from PyQt6 import uic

from structure import structure
import generalUtils

class ProcessWizardWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui/main.ui', self)
        self.current_level_id = 0
        self.current_image_path = None
        self.tools = generalUtils.read_tools_from_json('./data/tools.json')
        self.fill_tools_list()
        self.actionOpen_image.triggered.connect(self.open_image)

        # Assuming you have a QLabel named 'image_label' in your UI file
        # self.image_label = self.findChild(QLabel, 'image_label')
        # self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

    def open_image(self):
        print('opening image')
        self.start_browse_image()

    def fill_tools_list(self):
        tools_list = [None] + [t.name for t in self.tools]
        self.tool_comboBox.addItems(tools_list)

    def start_browse_image(self):
        file_filter = "Image Files (*.png *.jpg *.bmp *.gif);;All Files (*)"
        file_path, _ = QFileDialog.getOpenFileName(self, 'Select Image File', filter=file_filter)
        if file_path:
            self.current_image_path = file_path
            print(self.current_image_path)
            self.display_image(file_path)

    def display_image(self, image_path):
        pixmap = QPixmap(image_path)
        self.image_label.setPixmap(pixmap)
        self.image_label.setScaledContents(True)  # Optionally scale the image to fit the label

if __name__ == '__main__':
    app = QApplication([])
    window = ProcessWizardWindow()
    window.show()
    app.exec()
