import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QPushButton, QWidget, QSizePolicy, QLineEdit
from PyQt5.QtCore import Qt  # Import Qt module

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('BudgetBuddy: Expense Tracker App')
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout(self.central_widget)

        title_label = QLabel('Sign In to BudgetBuddy', self)
        title_label.setStyleSheet('font-size: 24px;')
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)

        username_input = QLineEdit(self)
        username_input.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout.addWidget(username_input)

        password_field = QLineEdit(self)
        password_field.setEchoMode(QLineEdit.Password)
        password_field.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout.addWidget(password_field)

        login_button = QPushButton('Login', self)
        login_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout.addWidget(login_button)

        signup_button = QPushButton('Sign up',self)
        signup_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout.addWidget(signup_button)


    def resizeEvent(self, event):
        # Adjust widget sizes or positions upon window resize (if needed)
        pass


def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
