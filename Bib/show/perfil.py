from PyQt5.QtWidgets import QMainWindow, QLabel# Importa as classes essenciais
from PyQt5.uic import loadUi# Importa a função para carregar arquivos .ui
import os

class PerfilWindow(QMainWindow):# Define a classe PerfilWindow, que herda de QMainWindow
    def __init__(self, stacked_widget, db_manager):# O método construtor da classe.
        super(PerfilWindow, self).__init__()# Chama o construtor da classe pai QMainWindow
        self.stacked_widget = stacked_widget  # Referência ao QStackedWidget principal
        self.db_manager = db_manager  
        self.id_funcionario = None  # ID do funcionário logado será definido dinamicamente

        # Carregar o arquivo perfil.ui
        ui_path = os.path.join(os.path.dirname(__file__), "perfil.ui")
        loadUi(ui_path, self)

        # Conectar o botão menuButton ao método para voltar ao menu
        self.menuButton.clicked.connect(self.go_to_menu)

        # Referências aos QLabel no perfil.ui
        # Esses QLabel's exibirão os dados do funcionário.
        self.nomeInput: QLabel = self.findChild(QLabel, "nomeInput")
        self.telemovelInput: QLabel = self.findChild(QLabel, "telemovelInput")
        self.nifInput: QLabel = self.findChild(QLabel, "nifInput")
        self.emailInput: QLabel = self.findChild(QLabel, "emailInput")

    def set_funcionario_id(self, id_funcionario):# Define o método para receber o ID do funcionário após o login.
        """recebe o ID do funcionário logado e carrega os dados correspondentes."""
        self.id_funcionario = id_funcionario
        self.load_funcionario_data()

    def load_funcionario_data(self):# Define o método para carregar os dados do funcionário do banco de dados.
        """Carrega os dados do funcionário logado e exibe nos QLabel."""
        try:
            # Verificar se o ID do funcionário foi definido
            if not self.id_funcionario:
                print("[ERRO] ID do funcionário não definido.")
                return

            # Consulta SQL para buscar os dados do funcionário pelo idFuncionario
            query = """
                SELECT nome, telemovel, nif, email
                FROM funcionario
                WHERE idFuncionario = %s
            """
            result = self.db_manager.fetch_query(query, (self.id_funcionario,))
            # O fetch_query retorna uma lista de dicionários. 

            if result:#se o resultado for encontrado,preenche as QLabel.
                # Preencher os QLabel com os dados do funcionário, convertendo para string
                self.nomeInput.setText(str(result[0]["nome"]))
                self.telemovelInput.setText(str(result[0]["telemovel"]))
                self.nifInput.setText(str(result[0]["nif"]))
                self.emailInput.setText(str(result[0]["email"]))
            else:
                # Caso o funcionário não seja encontrado
                self.nomeInput.setText("N/A")
                self.telemovelInput.setText("N/A")
                self.nifInput.setText("N/A")
                self.emailInput.setText("N/A")

        except Exception as e:
            print(f"[ERRO] Não foi possível carregar os dados do funcionário: {e}")

    def go_to_menu(self):
        """Volta para a tela do menu."""
        self.stacked_widget.setCurrentWidget(self.stacked_widget.menu_window)