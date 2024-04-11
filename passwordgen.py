import sys
import random
import string
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QSpinBox, QLineEdit, QListWidget, QListWidgetItem, QMessageBox, QFileDialog

class PasswordGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gerador de Senha")
        self.setGeometry(200, 200, 400, 300)

        layout = QVBoxLayout()

        # Tamanho da senha
        self.size_label = QLabel("Tamanho da Senha:")
        self.size_spinbox = QSpinBox()
        self.size_spinbox.setMinimum(10)
        self.size_spinbox.setMaximum(200)
        self.size_spinbox.setValue(10)

        # Complexidade da senha
        self.complexity_label = QLabel("Complexidade da Senha:")
        self.complexity_spinbox = QSpinBox()
        self.complexity_spinbox.setMinimum(1)
        self.complexity_spinbox.setMaximum(10)
        self.complexity_spinbox.setValue(5)

        # Botão para gerar senha
        self.generate_button = QPushButton("Gerar Senha")
        self.generate_button.clicked.connect(self.generate_password)

        # Botão para limpar senhas
        self.clear_button = QPushButton("Limpar Senhas")
        self.clear_button.clicked.connect(self.clear_passwords)

        # Botão para salvar senhas
        self.save_button = QPushButton("Salvar Senhas")
        self.save_button.clicked.connect(self.save_passwords)

        # Botão para copiar senha selecionada
        self.copy_button = QPushButton("Copiar Senha")
        self.copy_button.clicked.connect(self.copy_password)

        # Campo de texto para mostrar a senha gerada
        self.password_lineedit = QLineEdit()
        self.password_lineedit.setReadOnly(True)

        # Lista para mostrar senhas geradas anteriormente
        self.password_listwidget = QListWidget()
        self.password_listwidget.itemDoubleClicked.connect(self.copy_to_clipboard)

        layout.addWidget(self.size_label)
        layout.addWidget(self.size_spinbox)
        layout.addWidget(self.complexity_label)
        layout.addWidget(self.complexity_spinbox)
        layout.addWidget(self.generate_button)
        layout.addWidget(self.clear_button)
        layout.addWidget(self.save_button)
        layout.addWidget(self.copy_button)
        layout.addWidget(self.password_lineedit)
        layout.addWidget(self.password_listwidget)

        self.setLayout(layout)

    def generate_password(self):
        size = self.size_spinbox.value()
        complexity = self.complexity_spinbox.value()

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(size))

        # Adiciona a senha gerada à lista
        item = QListWidgetItem(password)
        self.password_listwidget.addItem(item)

        # Define a senha gerada no campo de texto
        self.password_lineedit.setText(password)

    def clear_passwords(self):
        self.password_listwidget.clear()
        self.password_lineedit.clear()

    def save_passwords(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Salvar Senhas", "", "Text Files (*.txt)")
        if file_path:
            with open(file_path, "w") as file:
                for index in range(self.password_listwidget.count()):
                    password_item = self.password_listwidget.item(index)
                    password = password_item.text()
                    file.write(password + "\n")

    def copy_password(self):
        selected_item = self.password_listwidget.currentItem()
        if selected_item:
            password = selected_item.text()
            QApplication.clipboard().setText(password)
            QMessageBox.information(self, "Senha Copiada", "A senha foi copiada para a área de transferência.")

    def copy_to_clipboard(self, item):
        password = item.text()
        QApplication.clipboard().setText(password)
        QMessageBox.information(self, "Senha Copiada", "A senha foi copiada para a área de transferência.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PasswordGenerator()
    window.show()
    sys.exit(app.exec_())
