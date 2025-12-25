from PyQt5.QtWidgets import QMainWindow, QPushButton, QLineEdit, QMessageBox
from PyQt5.uic import loadUi
import os

class LeitorCadastroWindow(QMainWindow):# Define a classe LeitorCadastroWindow, que herda de QMainWindow
    def __init__(self, stacked_widget, db_manager):
        super(LeitorCadastroWindow, self).__init__()
        self.stacked_widget = stacked_widget  # Referência ao QStackedWidget principal
        self.db_manager = db_manager  # Referência ao gerenciador de banco de dados

        # Carregar o arquivo leitorCadastro.ui da pasta registro
        ui_path = os.path.join(os.path.dirname(__file__), "leitorCadastro.ui")
        loadUi(ui_path, self)#carrega a interface gráfica definida em leitorCadastro.ui

        # Conectar o botão menuButton ao método para voltar ao menu
        self.menuButton: QPushButton = self.findChild(QPushButton, "menuButton")
        if self.menuButton:
            self.menuButton.clicked.connect(self.go_to_menu)
        else:
            print("[ERRO] menuButton não encontrado no arquivo leitorCadastro.ui")

        # Conectar o botão salvarButton ao método de salvar
        self.salvarButton: QPushButton = self.findChild(QPushButton, "salvarButton")
        if self.salvarButton:
            self.salvarButton.clicked.connect(self.salvar_leitor)
            # Se o 'salvarButton' conecta ao método 'salvar_leitor'.
        else:
            print("[ERRO] salvarButton não encontrado no arquivo leitorCadastro.ui")

        # Inputs
        self.nomeInput: QLineEdit = self.findChild(QLineEdit, "nomeInput")
        self.telemovelInput: QLineEdit = self.findChild(QLineEdit, "telemovelInput")
        self.nifInput: QLineEdit = self.findChild(QLineEdit, "nifInput")
        self.emailInput: QLineEdit = self.findChild(QLineEdit, "emailInput")

    def go_to_menu(self):
        """Volta para a tela do menu."""
        self.stacked_widget.setCurrentWidget(self.stacked_widget.menu_window)

    def salvar_leitor(self):# Define o método 'salvar_leitor', que é executado quando o 'salvarButton' é clicado.
        """Salva o leitor no banco de dados."""
        nome = self.nomeInput.text().strip() if self.nomeInput else ""
        telemovel = self.telemovelInput.text().strip() if self.telemovelInput else ""
        nif = self.nifInput.text().strip() if self.nifInput else ""
        email = self.emailInput.text().strip() if self.emailInput else ""

        if not nome or not telemovel or not nif or not email:
            QMessageBox.warning(self, "Atenção", "Preencha todos os campos!")
            return

        try:
            query = "INSERT INTO leitor (nome, telemovel, nif, email) VALUES (%s, %s, %s, %s)"
            self.db_manager.execute_query(query, (nome, telemovel, nif, email))
            QMessageBox.information(self, "Sucesso", "Leitor cadastrado com sucesso!")
            self.nomeInput.clear()
            self.telemovelInput.clear()
            self.nifInput.clear()
            self.emailInput.clear()
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao salvar leitor: {e}")