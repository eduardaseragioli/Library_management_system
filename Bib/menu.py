# menu.py
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
import os
from show.cadastro import CadastroWindow  # Importa a classe CadastroWindow janelas que o menu pode navegar
from show.leitura import LeituraWindow  # Importa a classe LeituraWindow
from show.perfil import PerfilWindow  # Importa a classe PerfilWindow

class MenuWindow(QMainWindow):# Define a classe MenuWindow, que herda de QMainWindow
    def __init__(self, stacked_widget):
        super(MenuWindow, self).__init__()
        self.stacked_widget = stacked_widget  # Referência ao QStackedWidget principal

        # Carregar o arquivo menu.ui
        ui_path = os.path.join(os.path.dirname(__file__), "menu.ui")
        loadUi(ui_path, self)

        # Conectar o botão cadastroButton ao método para abrir a tela de cadastro
        self.cadastroButton.clicked.connect(self.open_cadastro_window)

        # Conectar o botão leituraButton ao método para abrir a tela de leitura
        self.leituraButton.clicked.connect(self.open_leitura_window)

        # Conectar o botão perfilButton ao método para abrir a tela de perfil
        self.perfilButton.clicked.connect(self.open_perfil_window)

    def open_cadastro_window(self):
        """Abre a tela de cadastro."""
        self.stacked_widget.setCurrentWidget(self.stacked_widget.cadastro_window)

    def open_leitura_window(self):
        """Abre a tela de leitura."""
        self.stacked_widget.setCurrentWidget(self.stacked_widget.leitura_window)

    def open_perfil_window(self):
        """Abre a tela de perfil."""
        self.stacked_widget.setCurrentWidget(self.stacked_widget.perfil_window)