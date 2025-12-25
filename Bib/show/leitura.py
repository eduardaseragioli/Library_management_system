# leitura.py
from PyQt5.QtWidgets import QMainWindow# Importa QMainWindow, a classe base para criar a janela principal.
from PyQt5.uic import loadUi #Importa a função para carregar arquivos .ui
import os
from show.funcionario import FuncionarioWindow  
from show.leitor import LeitorWindow  
from show.item import ItemWindow  
from show.estatistica import EstatisticaWindow  
from show.autor import AutorWindow  
from show.emprestimo import EmprestimoWindow  
from show.multa import MultaWindow  


class LeituraWindow(QMainWindow):# Define a classe LeituraWindow, que herda de QMainWindow.

    def __init__(self, stacked_widget): # O método construtor da classe.
        super(LeituraWindow, self).__init__()
        self.stacked_widget = stacked_widget  # Referência ao QStackedWidget principal

        # Carregar o arquivo leitura.ui
        ui_path = os.path.join(os.path.dirname(__file__), "leitura.ui")
        loadUi(ui_path, self)

        # Conectar o botão menuButton ao método para voltar ao menu
        self.menuButton.clicked.connect(self.go_to_menu)

        # Conectar o botão funcionarioButton ao método para abrir a tela de funcionário
        self.funcionarioButton.clicked.connect(self.open_funcionario_window)

        # Conectar o botão leituraButton ao método para abrir a tela de leitor
        self.leituraButton.clicked.connect(self.open_leitor_window)

        # Conectar o botão itemButton ao método para abrir a tela de item
        self.itemButton.clicked.connect(self.open_item_window)

        # Conectar o botão estatisticaButton ao método para abrir a tela de estatísticas
        self.estatisticaButton.clicked.connect(self.open_estatistica_window)

        # Conectar o botão autorButton ao método para abrir a tela de autor
        self.autorButton.clicked.connect(self.open_autor_window)

         # Conectar o botão emprestimoButton ao método para abrir a tela de empréstimo
        self.emprestimoButton.clicked.connect(self.open_emprestimo_window)

        # Conectar o botão multaButton ao método para abrir a tela de multa
        self.multaButton.clicked.connect(self.open_multa_window)




    def go_to_menu(self): # Define o método 'go_to_menu'.
        """Volta para a tela do menu."""
        self.stacked_widget.setCurrentWidget(self.stacked_widget.menu_window)

    def open_funcionario_window(self): # Define o método para abrir a tela de visualização de funcionários.
        """Abre a tela de funcionário."""
        self.stacked_widget.setCurrentWidget(self.stacked_widget.funcionario_window)

    def open_leitor_window(self):
        """Abre a tela de leitor."""
        self.stacked_widget.setCurrentWidget(self.stacked_widget.leitor_window)

    def open_item_window(self):
        """Abre a tela de item."""
        self.stacked_widget.setCurrentWidget(self.stacked_widget.item_window)

    def open_estatistica_window(self):
        """Abre a tela de estatísticas."""
        self.stacked_widget.setCurrentWidget(self.stacked_widget.estatistica_window)

    def open_autor_window(self):
        """Abre a tela de autor."""
        self.stacked_widget.setCurrentWidget(self.stacked_widget.autor_window)

    def open_emprestimo_window(self):
        """Abre a tela de empréstimo."""
        self.stacked_widget.setCurrentWidget(self.stacked_widget.emprestimo_window)

    def open_multa_window(self):
        """Abre a tela de multa."""
        self.stacked_widget.setCurrentWidget(self.stacked_widget.multa_window)