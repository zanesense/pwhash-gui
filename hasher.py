import hashlib
from PyQt5 import QtWidgets, QtGui, QtCore
import qdarkstyle

class PasswordHashGenerator(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Hash Generator")

        self.password_label = QtWidgets.QLabel("Enter Password:", self)
        self.password_label.setStyleSheet("font-size: 14px; color: #ffffff;")
        self.password_entry = QtWidgets.QLineEdit(self)
        self.password_entry.setEchoMode(QtWidgets.QLineEdit.Password)

        self.hash_label = QtWidgets.QLabel("Select Hash Algorithm:", self)
        self.hash_label.setStyleSheet("font-size: 14px; color: #ffffff;")
        self.hash_dropdown = QtWidgets.QComboBox(self)
        self.hash_dropdown.addItems(["SHA-256", "SHA-1", "MD5", "SHA-512", "SHA-384", "SHA-224"])

        self.generate_button = QtWidgets.QPushButton("Generate Hash", self)
        self.generate_button.clicked.connect(self.generate_hash)
        self.generate_button.setStyleSheet("font-size: 14px; color: #ffffff; background-color: #007bff; border: 1px solid #007bff; border-radius: 5px; padding: 5px 10px;")
        
        self.output_label = QtWidgets.QLabel("Hashed Password:", self)
        self.output_label.setStyleSheet("font-size: 14px; color: #ffffff;")
        self.hash_output = QtWidgets.QTextEdit(self)
        self.hash_output.setReadOnly(True)
        self.hash_output.setStyleSheet("font-size: 14px; color: #ffffff; background-color: #333333; border: 1px solid #555555; border-radius: 5px; padding: 5px;")

        self.copy_button = QtWidgets.QPushButton("Copy to Clipboard", self)
        self.copy_button.clicked.connect(self.copy_to_clipboard)
        self.copy_button.setStyleSheet("font-size: 14px; color: #ffffff; background-color: #007bff; border: 1px solid #007bff; border-radius: 5px; padding: 5px 10px;")

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.password_label)
        layout.addWidget(self.password_entry)
        layout.addWidget(self.hash_label)
        layout.addWidget(self.hash_dropdown)
        layout.addWidget(self.generate_button)
        layout.addWidget(self.output_label)
        layout.addWidget(self.hash_output)
        layout.addWidget(self.copy_button)
        self.setLayout(layout)

        self.setStyleSheet("background-color: #222222;")

    def generate_hash(self):
        password = self.password_entry.text()
        hash_algorithm = self.hash_dropdown.currentText()

        if password:
            if hash_algorithm == "SHA-256":
                hashed_password = hashlib.sha256(password.encode()).hexdigest()
            elif hash_algorithm == "SHA-1":
                hashed_password = hashlib.sha1(password.encode()).hexdigest()
            elif hash_algorithm == "MD5":
                hashed_password = hashlib.md5(password.encode()).hexdigest()
            elif hash_algorithm == "SHA-512":
                hashed_password = hashlib.sha512(password.encode()).hexdigest()
            elif hash_algorithm == "SHA-384":
                hashed_password = hashlib.sha384(password.encode()).hexdigest()
            elif hash_algorithm == "SHA-224":
                hashed_password = hashlib.sha224(password.encode()).hexdigest()

            self.hash_output.setPlainText(hashed_password)
        else:
            QtWidgets.QMessageBox.warning(self, "Empty Password", "Please enter a password.")

    def copy_to_clipboard(self):
        hash_text = self.hash_output.toPlainText().strip()
        if hash_text:
            clipboard = QtWidgets.QApplication.clipboard()
            clipboard.setText(hash_text)
            QtWidgets.QMessageBox.information(self, "Copied", "Hashed password copied to clipboard.")
        else:
            QtWidgets.QMessageBox.warning(self, "No Hash", "No hash to copy. Generate a hash first.")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(qdarkstyle.load_stylesheet())
    window = PasswordHashGenerator()
    window.show()
    sys.exit(app.exec_())
