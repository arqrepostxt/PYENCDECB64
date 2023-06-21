import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PyQt5.QtWidgets import QTextEdit, QPushButton
from PyQt5.QtWidgets import QTabWidget, QLabel, QScrollArea
from PyQt5.QtCore import Qt
import base64


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('ENC/DEC B64')
        self.setGeometry(100, 100, 500, 400)

        # Create the tab widget
        self.tab_widget = QTabWidget()
        self.setCentralWidget(self.tab_widget)

        # Create the first tab
        self.tab1 = QWidget()
        self.tab_widget.addTab(self.tab1, 'Encode to Base64')

        # Add header label to the first tab
        self.header_label1 = QLabel('ENCODE TO BASE 64')
        self.header_label1.setAlignment(Qt.AlignCenter)
        
        # Add text field with scroll bar to the first tab
        self.text_edit1 = QTextEdit()
        self.text_edit1.setLineWrapMode(QTextEdit.WidgetWidth)  # Enable horizontal scrolling
        self.scroll_area1 = QScrollArea()
        self.scroll_area1.setWidgetResizable(True)
        self.scroll_area1.setWidget(self.text_edit1)

        # Add encode button to the first tab
        self.encode_button = QPushButton('Encode')
        self.encode_button.clicked.connect(self.encode_text)

        # Add layout to the first tab
        self.tab1_layout = QVBoxLayout()
        self.tab1_layout.addWidget(self.header_label1)
        self.tab1_layout.addWidget(self.scroll_area1)
        self.tab1_layout.addWidget(self.encode_button)
        self.tab1.setLayout(self.tab1_layout)

        # Create the second tab
        self.tab2 = QWidget()
        self.tab_widget.addTab(self.tab2, 'Decode from Base64')

        # Add header label to the second tab
        self.header_label2 = QLabel('DECODE FROM BASE 64')
        self.header_label2.setAlignment(Qt.AlignCenter)
        
        # Add text field with scroll bar to the second tab
        self.text_edit2 = QTextEdit()
        self.text_edit2.setLineWrapMode(QTextEdit.WidgetWidth)  # Enable horizontal scrolling
        self.scroll_area2 = QScrollArea()
        self.scroll_area2.setWidgetResizable(True)
        self.scroll_area2.setWidget(self.text_edit2)

        # Add decode button to the second tab
        self.decode_button = QPushButton('Decode')
        self.decode_button.clicked.connect(self.decode_text)

        # Add layout to the second tab
        self.tab2_layout = QVBoxLayout()
        self.tab2_layout.addWidget(self.header_label2)
        self.tab2_layout.addWidget(self.scroll_area2)
        self.tab2_layout.addWidget(self.decode_button)
        self.tab2.setLayout(self.tab2_layout)

        self.show()

    def encode_text(self):
        text = self.text_edit1.toPlainText()
        encoded_text = base64.b64encode(text.encode()).decode()
        self.text_edit1.setPlainText(encoded_text)

    def decode_text(self):
        encoded_text = self.text_edit2.toPlainText()
        try:
            decoded_text = base64.b64decode(encoded_text.encode()).decode()
        except base64.binascii.Error:
            decoded_text = "Invalid Base64 input"
        self.text_edit2.setPlainText(decoded_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
