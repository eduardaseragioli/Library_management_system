from PyQt5.QtWidgets import QMainWindow # Importa a classe QMainWindow (classe base) do PyQt5 para criar janelas principais
from PyQt5.uic import loadUi# Importa a função loadUi do PyQt5 para carregar arquivos .UI
import os

class CapaWindow(QMainWindow): # Define a classe CapaWindow que herda de QMainWindow
    def __init__(self, stacked_widget):# Método construtor da classe CapaWindow. Permitir que a CapaWindow alterne para outras telas.
        super(CapaWindow, self).__init__() 
        self.stacked_widget = stacked_widget  # Referência ao QStackedWidget principal

        # Carregar o arquivo capa.ui
        ui_path = os.path.join(os.path.dirname(__file__), "capa.ui")
        loadUi(ui_path, self) # Carrega a interface gráfica definida em capa.ui

        # Conectar o botão pushButton ao método para mudar para a tela de login
        self.pushButton.clicked.connect(self.go_to_login)

    def go_to_login(self): # Definição do método que muda para a tela de login
        """Muda para a tela de login."""
        self.stacked_widget.setCurrentWidget(self.stacked_widget.login_window)