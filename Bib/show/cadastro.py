# cadastro.py
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
import os
from registro.funcionarioCadastro import FuncionarioCadastroWindow  # Importa a classe FuncionarioCadastroWindow
from registro.leitorCadastro import LeitorCadastroWindow  # Importa a classe LeitorCadastroWindow
from registro.itemCadastro import ItemCadastroWindow  # Importa a classe ItemCadastroWindow
from registro.autorCadastro import AutorCadastroWindow  # Importa a classe AutorCadastroWindow
from registro.emprestimoCadastro import EmprestimoCadastroWindow  # Importa a classe EmprestimoCadastroWindow
from registro.multaCadastro import MultaCadastroWindow  # Importa a classe MultaCadastroWindow





class CadastroWindow(QMainWindow):# Define a classe CadastroWindow, que herda de QMainWindow
    def __init__(self, stacked_widget):
        super(CadastroWindow, self).__init__()
        self.stacked_widget = stacked_widget  # Referência ao QStackedWidget principal

        # Carregar o arquivo cadastro.ui
        ui_path = os.path.join(os.path.dirname(__file__), "cadastro.ui")
        loadUi(ui_path, self)

        # Conectar o botão menuButton ao método para voltar ao menu
        self.menuButton.clicked.connect(self.go_to_menu)

        # Conectar o botão funcionarioButton ao método para abrir a tela de cadastro de funcionário
        self.funcionarioButton.clicked.connect(self.open_funcionario_cadastro_window)

        # Conectar o botão leitorButton ao método para abrir a tela de cadastro de leitor
        self.leituraButton.clicked.connect(self.open_leitor_cadastro_window)

        # Conectar o botão itemButton ao método para abrir a tela de cadastro de leitor
        self.itemButton.clicked.connect(self.open_item_cadastro_window)

        # Conectar o botão autorButton ao método para abrir a tela de cadastro de leitor
        self.autorButton.clicked.connect(self.open_autor_cadastro_window)

        # Conectar o botão emprestimoButton ao método para abrir a tela de cadastro de leitor
        self.emprestimoButton.clicked.connect(self.open_emprestimo_cadastro_window)

        # Conectar o botão multaButton ao método para abrir a tela de cadastro de leitor
        self.multaButton.clicked.connect(self.open_multa_cadastro_window)

    def go_to_menu(self):
        """Volta para a tela do menu."""
        self.stacked_widget.setCurrentWidget(self.stacked_widget.menu_window)

    def open_funcionario_cadastro_window(self):
        """Abre a tela de cadastro de funcionário."""
        self.stacked_widget.setCurrentWidget(self.stacked_widget.funcionario_cadastro_window)

    def open_leitor_cadastro_window(self):
        """Abre a tela de cadastro de leitor."""
        self.stacked_widget.setCurrentWidget(self.stacked_widget.leitor_cadastro_window)

    def open_item_cadastro_window(self):
        """Abre a tela de cadastro de item."""
        self.stacked_widget.setCurrentWidget(self.stacked_widget.item_cadastro_window)

    def open_autor_cadastro_window(self):
        """Abre a tela de cadastro de autor."""
        self.stacked_widget.setCurrentWidget(self.stacked_widget.autor_cadastro_window)

    def open_emprestimo_cadastro_window(self):
        """Abre a tela de cadastro de empréstimo."""
        self.stacked_widget.setCurrentWidget(self.stacked_widget.emprestimo_cadastro_window)

    def open_multa_cadastro_window(self):
        """Abre a tela de cadastro de multa."""
        self.stacked_widget.setCurrentWidget(self.stacked_widget.multa_cadastro_window)