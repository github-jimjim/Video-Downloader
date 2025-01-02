import sys
import os
import cv2
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QFileDialog, QLabel, QMessageBox

class ConverterApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("WebM to MP4 Converter")

        layout = QVBoxLayout()

        self.label = QLabel("Select a .webm file to convert to .mp4")
        layout.addWidget(self.label)

        self.btn_select_file = QPushButton("Select WebM File")
        self.btn_select_file.clicked.connect(self.select_file)
        layout.addWidget(self.btn_select_file)

        self.btn_convert = QPushButton("Convert to MP4")
        self.btn_convert.clicked.connect(self.convert_file)
        layout.addWidget(self.btn_convert)

        self.setLayout(layout)
        self.selected_file = None

    def select_file(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Select WebM File", "", "WebM Files (*.webm);;All Files (*)", options=options)
        if file_name:
            self.selected_file = file_name
            self.label.setText(f"Selected: {self.selected_file}")

    def convert_file(self):
        if not self.selected_file:
            QMessageBox.warning(self, "No File Selected", "Please select a .webm file first.")
            return

        try:
            mp4_file = os.path.splitext(self.selected_file)[0] + '.mp4'
            
            cap = cv2.VideoCapture(self.selected_file)

            width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
            height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
            fps = cap.get(cv2.CAP_PROP_FPS)

            fourcc = cv2.VideoWriter_fourcc(*'mp4v')
            out = cv2.VideoWriter(mp4_file, fourcc, fps, (width, height))

            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break
                out.write(frame)

            cap.release()
            out.release()

            QMessageBox.information(self, "Success", f"Conversion successful! Output file: {mp4_file}")

        except Exception as e:
            QMessageBox.critical(self, "Error", f"An error occurred during conversion: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    converter = ConverterApp()
    converter.resize(400, 200)
    converter.show()
    sys.exit(app.exec_())
