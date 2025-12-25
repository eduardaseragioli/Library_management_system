from PyQt5.QtWidgets import QMainWindow # importa QMainWindow,q é a classe base para janelas de aplicativo
from PyQt5.uic import loadUi #loadUi é usada para carregar arquivos .ui 
import os

class LoginWindow(QMainWindow):# Define a classe LoginWindow que herda de QMainWindow, ou seja, será uma janela principal para a tela de logi.
    def __init__(self, stacked_widget, db_manager): #permitir que a LoginWindow alterne para outras telas
        super(LoginWindow, self).__init__()
        self.stacked_widget = stacked_widget  # Referência ao QStackedWidget principal
        self.db_manager = db_manager  # Referência ao gerenciador de banco de dados

        # Carregar o arquivo login.ui
        ui_path = os.path.join(os.path.dirname(__file__), "login.ui") # Define o caminho do arquivo .ui
        loadUi(ui_path, self) # Carrega a interface gráfica de login.ui

        # Conectar o botão loginButton ao método de validação
        self.salvarButton.clicked.connect(self.validate_and_confirm_credentials)

        # Inicializar o texto do errorLabel como vazio
        self.errorLabel.setText("")
        self.errorLabel.setStyleSheet("color: black;")  # Define a cor do texto como vermelho

    def validate_and_confirm_credentials(self):
        """Valida e confirma as credenciais."""
        email = self.utilizadorInput.text()  # Obtém o texto do campo de email
        employee_id = self.senhaInput.text()  # Obtém o texto do campo de senha (ID do funcionário)

        if not email or not employee_id:
            # Notifica que os campos não podem estar vazios
            self.errorLabel.setText("Os campos não podem estar vazios.")
            return

        try:
            # Consulta ao banco de dados para verificar as credenciais
            query = "SELECT * FROM funcionario WHERE email = %s AND idFuncionario = %s"
            result = self.db_manager.fetch_query(query, (email, employee_id)) #result terá os resultados da consulta uma lista

            if result:
                # Credenciais corretas
                self.errorLabel.setText("")  # Limpa o texto do errorLabel
                # Muda diretamente para a tela do menu
                self.stacked_widget.setCurrentWidget(self.stacked_widget.menu_window)
            else:
                # Credenciais incorretas
                self.errorLabel.setText("Email ou ID incorretos.")  # Exibe a mensagem de erro
        except Exception as e:
            self.errorLabel.setText("Erro ao validar credenciais.")  # Exibe mensagem de erro
            print(f"[ERRO] Não foi possível validar as credenciais: {e}")