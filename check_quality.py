import sys
import cv2
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog

class VideoQualityChecker(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Video Qualitätsprüfer")
        self.setGeometry(100, 100, 300, 150)

        layout = QVBoxLayout()

        self.result_label = QLabel("Wähle ein Video aus, um die Qualität zu prüfen.", self)
        layout.addWidget(self.result_label)

        self.select_button = QPushButton("Video auswählen", self)
        self.select_button.clicked.connect(self.select_video)
        layout.addWidget(self.select_button)

        self.setLayout(layout)

    def select_video(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Wähle ein Video", "", "Videos (*.mp4 *.avi *.mkv)", options=options)
        if file_name:
            self.check_quality(file_name)

    def check_quality(self, video_path):
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            self.result_label.setText("Kann das Video nicht öffnen.")
            return

        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        cap.release()

        if width == 640 and height == 360:
            quality = "360p"
        elif width == 1280 and height == 720:
            quality = "720p"
        elif width == 1920 and height == 1080:
            quality = "1080p"
        elif width == 3840 and height == 2160:
            quality = "4K"
        else:
            quality = "Unbekannte Qualität"

        self.result_label.setText(f"Qualität: {quality}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = VideoQualityChecker()
    ex.show()
    sys.exit(app.exec_())
