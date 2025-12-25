from PyQt5.QtWidgets import QMainWindow, QLabel, QTableWidget, QTableWidgetItem, QPushButton# Importa as classes necessárias do PyQt5.QtWidgets
from PyQt5.uic import loadUi# Importa a função para carregar.ui
import os

class LeitorWindow(QMainWindow):# Define a classe LeitorWindow, que herda de QMainWindow
    def __init__(self, stacked_widget, db_manager): # O método construtor.
        super(LeitorWindow, self).__init__()
        self.stacked_widget = stacked_widget#navegação entre telas
        self.db_manager = db_manager

        # Carregar o arquivo leitor.ui da pasta show
        ui_path = os.path.join(os.path.dirname(__file__), "leitor.ui")
        loadUi(ui_path, self)

        # Conectar o botão menuButton ao método para voltar ao menu
        self.menuButton: QPushButton = self.findChild(QPushButton, "menuButton")
        if self.menuButton:
            self.menuButton.clicked.connect(self.go_to_menu)
        else:
            print("[ERRO] menuButton não encontrado no arquivo leitor.ui")

        self.tabela: QTableWidget = self.findChild(QTableWidget, "tabela")
        if not self.tabela:
            print("[ERRO] tabela não encontrada no arquivo leitor.ui")
        # Procura pelo QTableWidget com o nome de objeto "tabela" na UI.


        self.quantidadeInput: QLabel = self.findChild(QLabel, "quantidadeInput")
        if not self.quantidadeInput:
            print("[ERRO] quantidadeInput não encontrado no arquivo leitor.ui")
        # Procura pelo QLabel com o nome de objeto "quantidadeInput" na UI.

        # Carrega os dados dos leitores e a quantidade ao inicializar a janela.
        self.load_leitores()
        self.load_quantidade()

    def showEvent(self, event):
        """Atualiza a tabela e a quantidade de leitores sempre que a janela for exibida."""
        self.load_leitores()
        self.load_quantidade()
        super().showEvent(event)# Chama a implementação original do showEvent da classe pai.


    def load_leitores(self):
    # Define o método para carregcolocar os dados dos leitores do banco de dados para o QTableWidget.
        """Carrega os dados da tabela leitor e exibe no QTableWidget."""
        if not self.tabela:
            print("[ERRO] tabela não está inicializada.")
            return

        try:
         # Consulta ao banco de dados para obter todos os dados da tabela 'leitor'.
            query = "SELECT * FROM leitor"
            results = self.db_manager.fetch_query(query)

            if not results:
                print("[INFO] Nenhum dado encontrado na tabela leitor.")
                self.tabela.setRowCount(0)# Garante que a tabela esteja vazia.
                return

            # Configurar o número de linhas e colunas no QTableWidget
            self.tabela.setRowCount(len(results))
            self.tabela.setColumnCount(len(results[0]))
            self.tabela.setHorizontalHeaderLabels(results[0].keys())# Define os cabeçalhos das colunas


            # Preenche o QTableWidget com os dados.
            for row_idx, row_data in enumerate(results):
                for col_idx, col_data in enumerate(row_data.values()):
                    # Cria um QTableWidgetItem para cada dado e o insere na célula correspondente.
                    self.tabela.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))

        except Exception as e:
            print(f"[ERRO] Não foi possível carregar os dados da tabela leitor: {e}")

    def load_quantidade(self):
    # Define o método para carregar e exibir a quantidade total de leitores.

        """Carrega a quantidade de leitores e exibe no QLabel."""
        if not self.quantidadeInput:
            print("[ERRO] quantidadeInput não está inicializado.")
            return

        try:
         # Consulta ao banco de dados para contar o número de leitores.
            query = "SELECT COUNT(*) AS quantidade FROM leitor"
            result = self.db_manager.fetch_query(query)

            if result:
                quantidade = result[0]["quantidade"]# Obtém o valor da contagem
                self.quantidadeInput.setText(str(quantidade))# Exibe no QLabel
            else:
                self.quantidadeInput.setText("0")# Exibe 0 se não houver leitores

        except Exception as e:
            print(f"[ERRO] Não foi possível carregar a quantidade de leitores: {e}")

    def go_to_menu(self):
    # Define o método para retornar à tela do menu principal.
        """Volta para a tela do menu."""
        self.stacked_widget.setCurrentWidget(self.stacked_widget.menu_window)