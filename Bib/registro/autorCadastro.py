# autorCadastro.py
from PyQt5.QtWidgets import QMainWindow, QPushButton, QLineEdit, QMessageBox
from PyQt5.uic import loadUi
import os

class AutorCadastroWindow(QMainWindow):#Define a classe 'AutorCadastroWindow', que herda de 'QMainWindow'.

    def __init__(self, stacked_widget, db_manager):
        super(AutorCadastroWindow, self).__init__()
        self.stacked_widget = stacked_widget  # Referência ao QStackedWidget principal
        self.db_manager = db_manager  # Referência ao gerenciador de banco de dados

        # Carregar o arquivo autorCadastro.ui da pasta registro
        ui_path = os.path.join(os.path.dirname(__file__), "autorCadastro.ui")
        loadUi(ui_path, self)

        # Conectar o botão menuButton ao método para voltar ao menu
        self.menuButton: QPushButton = self.findChild(QPushButton, "menuButton")
        if self.menuButton:
            self.menuButton.clicked.connect(self.go_to_menu)
        else:
            print("[ERRO] menuButton não encontrado no arquivo autorCadastro.ui")

        # Conectar o botão salvarButton ao método de salvar
        self.salvarButton: QPushButton = self.findChild(QPushButton, "salvarButton")
        if self.salvarButton:
            self.salvarButton.clicked.connect(self.salvar_autor)
            # Conectar o botão salvarButton ao método de salvar_autor 
        else:
            print("[ERRO] salvarButton não encontrado no arquivo autorCadastro.ui")

        # Inputs
        self.nomeInput: QLineEdit = self.findChild(QLineEdit, "nomeInput")
        self.nacionalidadeInput: QLineEdit = self.findChild(QLineEdit, "nacionalidadeInput")

    def go_to_menu(self):# Define o método 'go_to_menu'
        """Volta para a tela do menu."""
        self.stacked_widget.setCurrentWidget(self.stacked_widget.menu_window)

    def salvar_autor(self):# Define o método 'salvar_autor'
        """Salva o autor no banco de dados."""
         # Coleta o texto dos campos de entrada
        nome = self.nomeInput.text().strip() if self.nomeInput else ""
        nacionalidade = self.nacionalidadeInput.text().strip() if self.nacionalidadeInput else ""

        if not nome or not nacionalidade:
            QMessageBox.warning(self, "Atenção", "Preencha todos os campos!")
            return

        try:
            query = "INSERT INTO autor (nome, nacionalidade) VALUES (%s, %s)"
            self.db_manager.execute_query(query, (nome, nacionalidade))
            QMessageBox.information(self, "Sucesso", "Autor cadastrado com sucesso!")
            self.nomeInput.clear()
            self.nacionalidadeInput.clear()
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao salvar autor: {e}")