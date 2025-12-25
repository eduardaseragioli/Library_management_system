from PyQt5.QtWidgets import QMainWindow, QPushButton, QLabel, QMessageBox
from PyQt5.uic import loadUi
import os

class FuncionarioCadastroWindow(QMainWindow):
    def __init__(self, stacked_widget, db_manager):
        super(FuncionarioCadastroWindow, self).__init__()
        self.stacked_widget = stacked_widget  # Referência ao QStackedWidget principal
        self.db_manager = db_manager  # Referência ao gerenciador de banco de dados

        # Carregar o arquivo funcionarioCadastro.ui
        ui_path = os.path.join(os.path.dirname(__file__), "funcionarioCadastro.ui")
        loadUi(ui_path, self)

        # Conectar o botão salvar ao método para salvar os dados
        self.salvarButton: QPushButton = self.findChild(QPushButton, "salvarButton")
        if self.salvarButton:
            self.salvarButton.clicked.connect(self.salvar_dados)
        else:
            print("[ERRO] salvarButton não encontrado no arquivo funcionarioCadastro.ui")

        # Referências aos QLabel no arquivo .ui
        self.nomeInput: QLabel = self.findChild(QLabel, "nomeInput")
        self.telemovelInput: QLabel = self.findChild(QLabel, "telemovelInput")
        self.nifInput: QLabel = self.findChild(QLabel, "nifInput")
        self.emailInput: QLabel = self.findChild(QLabel, "emailInput")

    def salvar_dados(self):
        """Salva os dados inseridos nos QLabel na tabela FUNCIONARIO."""
        try:
            # Obter os valores dos QLabel
            nome = self.nomeInput.text().strip()
            telemovel = self.telemovelInput.text().strip()
            nif = self.nifInput.text().strip()
            email = self.emailInput.text().strip()

            # Verificar se todos os campos estão preenchidos
            if not nome or not telemovel or not nif or not email:
                QMessageBox.warning(self, "Erro", "Por favor, preencha todos os campos.")
                return

            # Inserir os dados na tabela FUNCIONARIO
            query = """
                INSERT INTO FUNCIONARIO (nome, telemovel, nif, email)
                VALUES (%s, %s, %s, %s)
            """
            self.db_manager.execute_query(query, (nome, telemovel, nif, email))

            # Exibir mensagem de sucesso
            QMessageBox.information(self, "Sucesso", "Funcionário cadastrado com sucesso!")

            # Limpar os QLabel
            self.nomeInput.setText("")
            self.telemovelInput.setText("")
            self.nifInput.setText("")
            self.emailInput.setText("")

        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Não foi possível salvar os dados: {e}")
            print(f"[ERRO] Não foi possível salvar os dados: {e}")

    def go_to_menu(self):
        """Volta para a tela do menu."""
        self.stacked_widget.setCurrentWidget(self.stacked_widget.menu_window)