from PyQt5.QtWidgets import QMainWindow, QLabel, QTableWidget, QTableWidgetItem, QPushButton# Importa as classes essenciais do PyQt5
from PyQt5.uic import loadUi# Importa a função para carregar .ui
import os

class FuncionarioWindow(QMainWindow):# Define a classe FuncionarioWindow, que herda de QMainWindow

    def __init__(self, stacked_widget, db_manager):# O método construtor da classe.
        super(FuncionarioWindow, self).__init__()
        self.stacked_widget = stacked_widget  # Referência ao QStackedWidget principal
        self.db_manager = db_manager  #gerenciador de banco de dados

        # Carregar o arquivo funcionario.ui da pasta show
        ui_path = os.path.join(os.path.dirname(__file__), "funcionario.ui")
        loadUi(ui_path, self)

        # Conectar o botão menuButton ao método para voltar ao menu
        self.menuButton: QPushButton = self.findChild(QPushButton, "menuButton")
        if self.menuButton:
            self.menuButton.clicked.connect(self.go_to_menu)
        else:
            print("[ERRO] menuButton não encontrado no arquivo funcionario.ui")

        # Referência ao QTableWidget para exibir os dados da tabela funcionario
        self.tabela: QTableWidget = self.findChild(QTableWidget, "tabela")
        if not self.tabela:
            print("[ERRO] tabela não encontrada no arquivo funcionario.ui")
        # Procura pelo QTableWidget com o nome de objeto "tabela" na UI.

        # Referência ao QLabel para exibir a quantidade de funcionários
        self.quantidadeInput: QLabel = self.findChild(QLabel, "quantidadeInput")
        if not self.quantidadeInput:
            print("[ERRO] quantidadeInput não encontrado no arquivo funcionario.ui")
        # Procura pelo QLabel com o nome de objeto "quantidadeInput" na UI.


        # Carregar os dados da tabela funcionario e a quantidade de funcionários
        self.load_funcionarios()
        self.load_quantidade()
        # Chama estes métodos na inicialização para popular a tabela e a quantidade assim que a janela é criada.


    def showEvent(self, event):
        """Atualiza a tabela e a quantidade de funcionários sempre que a janela for exibida."""
        self.load_funcionarios()
        self.load_quantidade()
        super().showEvent(event)
        # Garante que os dados sejam atualizados

    def load_funcionarios(self):
    # Define o método para carregar e exibir os dados dos funcionários na tabela.

        """Carrega os dados da tabela funcionario e exibe no QTableWidget."""
        if not self.tabela:
            print("[ERRO] tabela não está inicializada.")
            return

        try:
            # Consulta ao banco de dados para obter os dados da tabela funcionario
            query = "SELECT * FROM funcionario"
            results = self.db_manager.fetch_query(query)

            if not results:
                print("[INFO] Nenhum dado encontrado na tabela funcionario.")
                self.tabela.setRowCount(0)# Garante que a tabela esteja vazia se não houver dados.
                return

            # Configurar o número de linhas e colunas no QTableWidget
            self.tabela.setRowCount(len(results))# Define o nº de linhas
            self.tabela.setColumnCount(len(results[0]))# Define o nº de colunas
            self.tabela.setHorizontalHeaderLabels(results[0].keys())  # Define os cabeçalhos das colunas

            # Preencher o QTableWidget com os dados
            for row_idx, row_data in enumerate(results):
            # Itera sobre cada linha (dicionário) dos resultados.
                for col_idx, col_data in enumerate(row_data.values()):
                    self.tabela.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))
                    # Cria um QTableWidgetItem com o dado e o insere na célula correta da tabela.

        except Exception as e:
            print(f"[ERRO] Não foi possível carregar os dados da tabela funcionario: {e}")

    def load_quantidade(self):
    # Define o método para carregar e exibir a quantidade de funcionários.

        """Carrega a quantidade de funcionários e exibe no QLabel."""
        if not self.quantidadeInput:
            print("[ERRO] quantidadeInput não está inicializado.")
            return

        try:
            # Consulta ao banco de dados para contar o número de funcionários
            query = "SELECT COUNT(*) AS quantidade FROM funcionario"
            result = self.db_manager.fetch_query(query)#retorna uma lista de dicionários

            if result:
                quantidade = result[0]["quantidade"]  # Obtém o valor da contagem
                self.quantidadeInput.setText(str(quantidade))  # Exibe no QLabel
            else:
                self.quantidadeInput.setText("0")  # Exibe 0 se não houver funcionários

        except Exception as e:
            print(f"[ERRO] Não foi possível carregar a quantidade de funcionários: {e}")

    def go_to_menu(self):
    # Define o método para retornar ao menu principal.
        """Volta para a tela do menu."""
        self.stacked_widget.setCurrentWidget(self.stacked_widget.menu_window)