import sys, time
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QPushButton, QWidget, QSizePolicy, QLineEdit, QFrame, QHBoxLayout, QComboBox, QDateEdit, QDialog, QTableWidget, QAbstractItemView, QTableWidgetItem
from PyQt5.QtCore import Qt, QDate  # Import Qt module

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
        login_button.clicked.connect(lambda: self.verify(username_input.text(), password_field.text()))

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

    def verify(self, username, password):
        global window
        with open("Source/textdb.txt", "r") as users:
            for user in users:
                user = user.strip().split("~")
                user = user[1::2]
                if (username in user) and (password in user):
                    window=MainWindow()
                    window.show()
                    self.destroy()
                    break
                else:
                    print("Account Not Found")

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
        reg_button.clicked.connect(lambda: self.add_verification(fullname_field.text(), email_field.text(), new_username.text(), new_password.text(), confirm_password.text()))
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

    def add_verification(self, name, email, username, password, cpassword):
        if(password == cpassword):
            full_credentials = f"{name}~{email}~{username}~{password}\n"
            with open("Source/signupdb.txt", "a") as new_user:
                new_user.write(full_credentials)
                print("Registration Completed!")
        else:
            print("Password does not match.")

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('BudgetBuddy: Expense Tracker App')
        main_layout = QHBoxLayout()

        #Button Sets
        button_frame = QFrame()
        button_frame.setFrameShape(QFrame.StyledPanel)
        button_frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        add_button = QPushButton("Add Record", self)
        add_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        add_button.clicked.connect(self.additionPopup)
        remove_button = QPushButton("Remove Record", self)
        remove_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        generate_button = QPushButton("Generate Record", self)
        generate_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        exit_button = QPushButton("Exit", self)
        exit_button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        exit_button.clicked.connect(self.exit_)

        button_layout = QVBoxLayout()
        button_layout.addWidget(add_button)
        button_layout.addWidget(remove_button)
        button_layout.addWidget(generate_button)
        button_layout.addWidget(exit_button)
        button_frame.setLayout(button_layout)

        #Viewing Area
        viewing_frame = QFrame()
        viewing_frame.setFrameShape(QFrame.StyledPanel)
        viewing_frame.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Table View
        table_view = QVBoxLayout()
        self.default_row_count = 5
        self.current_row_count = self.default_row_count

        # Data Table
        self.data_table = QTableWidget()
        self.data_table.setRowCount(self.default_row_count)  # Set the initial number of rows to 0
        self.data_table.setColumnCount(7)  # Set the number of columns
        self.data_table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        titles = ["Category", "Description", "Quantity", "Unit","Transaction Date", "Amount", "Payment Method"]
        self.data_table.setHorizontalHeaderLabels(titles)
        self.data_table.resizeColumnsToContents()
        self.data_table.horizontalHeader().setStretchLastSection(True)
        self.disable_editing()

        #Edit Button
        toggle_cells = QPushButton("Edit Mode")
        toggle_cells.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        toggle_cells.clicked.connect(self.toggle_editing)

        table_view.addWidget(self.data_table)
        table_view.addWidget(toggle_cells)
        viewing_frame.setLayout(table_view)

        self.load_data_from_file(self.data_table, 'Source/data.txt', '~')

        main_layout.addWidget(button_frame)
        main_layout.addWidget(viewing_frame)
        self.setLayout(main_layout)

    def resizeEvent(self, event):
        # Adjust widget sizes or positions upon window resize (if needed)
        pass

    def additionPopup(self):
        dialog = AdditionModal()
        dialog.setModal(True)  # Set the dialog as modal
        dialog.exec_()

    def exit_(self):
        exit()

    def set_table_rows(self, row_count):
        self.data_table.setRowCount(row_count)

    def load_data_from_file(self, table, filename, delimiter):
        try:
            with open(filename, 'r') as file:
                lines = file.readlines()
                num_rows = len(lines)
                extra_rows = max(0, num_rows - self.default_row_count)
                if extra_rows > 0:
                    self.current_row_count += extra_rows
                    self.set_table_rows(self.current_row_count)

                for row, line in enumerate(lines):
                    if row >= self.default_row_count:
                        table.insertRow(row)
                        self.current_row_count += 1
                    line = line.strip()
                    columns = line.split(delimiter)
                    for column, text in enumerate(columns):
                        item = QTableWidgetItem(text)
                        table.setItem(row, column - 1, item)
        except FileNotFoundError:
            print(f"File '{filename}' not found.")

    def disable_editing(self):
        self.data_table.setEditTriggers(QAbstractItemView.NoEditTriggers)

    def enable_editing(self):
        self.data_table.setEditTriggers(QAbstractItemView.CurrentChanged)

    def toggle_editing(self):
        if self.data_table.editTriggers() == QAbstractItemView.NoEditTriggers:
            self.enable_editing()
        else:
            self.disable_editing()

class AdditionModal(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Expense")

        #Adding View
        adding_view = QVBoxLayout()

        category_selection = QComboBox()
        category_selection.addItem('Select a Category')
        category_selection.addItem('Home & Utilities')
        category_selection.addItem('Insurance & Financial Section')
        category_selection.addItem('Obligations')
        category_selection.addItem('Groceries')
        category_selection.addItem('Personal & Medical Expense')
        category_selection.addItem('Entertainment')
        category_selection.addItem('Transportation Fare')
        category_selection.addItem('Child Care')
        category_selection.addItem('Other Expense')
        category_selection.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        adding_view.addWidget(category_selection)

        item_edit = QLineEdit()
        item_edit.setPlaceholderText('Description')
        item_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        adding_view.addWidget(item_edit)

        date_frame = QFrame();
        date_layout = QHBoxLayout()
        date_label = QLabel("Transaction Date: ")
        date_edit = QDateEdit()
        date_edit.setCalendarPopup(True)
        date_edit.setDate(QDate.currentDate())  # Set default date to current day
        date_edit.setDisplayFormat("yyyy-MM-dd")  # Set the display format of the date
        date_layout.addWidget(date_label)
        date_layout.addWidget(date_edit)
        date_frame.setLayout(date_layout)
        adding_view.addWidget(date_frame)

        amount_edit = QLineEdit()
        amount_edit.setPlaceholderText('Amount')
        amount_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        adding_view.addWidget(amount_edit)

        payment_method = QComboBox()
        payment_method.addItem('Payment Method')
        payment_method.addItem('Cash')
        payment_method.addItem('Credit')
        payment_method.addItem('Debit')
        payment_method.addItem('Gcash')
        payment_method.addItem('Paymaya')
        payment_method.addItem('Other')
        payment_method.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        adding_view.addWidget(payment_method)

        specify_pm = QLineEdit()
        specify_pm.setPlaceholderText("Specify Payment Method")
        specify_pm.setEnabled(False)
        specify_pm.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        adding_view.addWidget(specify_pm)

        self.setLayout(adding_view)

def main():
    global window
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()


