import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton

class SimpleUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple UI")
        self.setGeometry(100, 100, 300, 150)

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.username_label = QLabel("Username:")
        self.username_input = QLineEdit()

        self.email_label = QLabel("Email:")
        self.email_input = QLineEdit()

        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.submit_data)

        layout.addWidget(self.username_label)
        layout.addWidget(self.username_input)
        layout.addWidget(self.email_label)
        layout.addWidget(self.email_input)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def submit_data(self):
        username = self.username_input.text()
        email = self.email_input.text()
        print("Username:", username)
        print("Email:", email)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SimpleUI()
    window.show()
    sys.exit(app.exec_())