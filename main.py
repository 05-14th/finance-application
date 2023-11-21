import sys, time
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QPushButton, QWidget, QSizePolicy, QLineEdit
from PyQt5.QtCore import Qt  # Import Qt module

#Initialize Global Variables
window = None

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('BudgetBuddy: Expense Tracker App')

        layout = QVBoxLayout()

        title_label = QLabel('Sign In to BudgetBuddy', self)
        title_label.setStyleSheet('font-size: 24px;')
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)

        username_input = QLineEdit(self)
        username_input.setPlaceholderText('Username')
        username_input.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout.addWidget(username_input)

        password_field = QLineEdit(self)
        password_field.setPlaceholderText('Password')
        password_field.setEchoMode(QLineEdit.Password)
        password_field.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout.addWidget(password_field)

        login_button = QPushButton('Login', self)
        login_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout.addWidget(login_button)

        signup_button = QPushButton('Sign up',self)
        signup_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout.addWidget(signup_button)
        signup_button.clicked.connect(self.openSignUp)

        self.setLayout(layout)


    def resizeEvent(self, event):
        # Adjust widget sizes or positions upon window resize (if needed)
        pass

    def openSignUp(self):
        global window
        window=SignupWindow()
        window.show()
        self.destroy()


class SignupWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('BudgetBuddy: Expense Tracker App')

        su_layout = QVBoxLayout()

        title_label = QLabel('Sign Up to BudgetBuddy', self)
        title_label.setStyleSheet('font-size: 24px;')
        title_label.setAlignment(Qt.AlignCenter)
        su_layout.addWidget(title_label)

        fullname_field = QLineEdit(self)
        fullname_field.setPlaceholderText('Full Name')
        fullname_field.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        su_layout.addWidget(fullname_field)

        email_field = QLineEdit(self)
        email_field.setPlaceholderText('Email')
        email_field.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        su_layout.addWidget(email_field)

        new_username = QLineEdit(self)
        new_username.setPlaceholderText('Username')
        new_username.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        su_layout.addWidget(new_username)

        new_password = QLineEdit(self)
        new_password.setPlaceholderText('Password')
        new_password.setEchoMode(QLineEdit.Password)
        new_password.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        su_layout.addWidget(new_password)

        confirm_password = QLineEdit(self)
        confirm_password.setPlaceholderText('Confirm Password')
        confirm_password.setEchoMode(QLineEdit.Password)
        confirm_password.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        su_layout.addWidget(confirm_password)

        reg_button = QPushButton('Register',self)
        reg_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        su_layout.addWidget(reg_button)

        back_button = QPushButton('Back to Sign In', self)
        back_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        back_button.clicked.connect(self.backToLogin)
        su_layout.addWidget(back_button)

        self.setLayout(su_layout)

    def resizeEvent(self, event):
        # Adjust widget sizes or positions upon window resize (if needed)
        pass

    def backToLogin(self):
        global window
        window = MyWindow()
        window.show()
        self.destroy()

def main():
    global window
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
