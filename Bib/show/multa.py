from PyQt5.QtWidgets import QMainWindow, QLabel, QTableWidget, QTableWidgetItem, QPushButton
from PyQt5.uic import loadUi
import os

class MultaWindow(QMainWindow):
    def __init__(self, stacked_widget, db_manager):
        super(MultaWindow, self).__init__()
        self.stacked_widget = stacked_widget  # Referência ao QStackedWidget principal
        self.db_manager = db_manager  # Referência ao gerenciador de banco de dados

        # Carregar o arquivo multa.ui da pasta show
        ui_path = os.path.join(os.path.dirname(__file__), "multa.ui")
        loadUi(ui_path, self)

        # Conectar o botão menuButton ao método para voltar ao menu
        self.menuButton: QPushButton = self.findChild(QPushButton, "menuButton")
        if self.menuButton:
            self.menuButton.clicked.connect(self.go_to_menu)
        else:
            print("[ERRO] menuButton não encontrado no arquivo multa.ui")

        # Referência ao QTableWidget para exibir os dados da tabela multa
        self.tabela: QTableWidget = self.findChild(QTableWidget, "tabela")
        if not self.tabela:
            print("[ERRO] tabela não encontrada no arquivo multa.ui")

        # Referência ao QLabel para exibir a quantidade de pessoas com multas não pagas
        self.quantidadeInput: QLabel = self.findChild(QLabel, "quantidadeInput")
        if not self.quantidadeInput:
            print("[ERRO] quantidadeInput não encontrado no arquivo multa.ui")

        # Carregar os dados da tabela multa e a quantidade de pessoas com multas não pagas
        self.load_multas()
        self.load_quantidade()

    def showEvent(self, event):
        """Atualiza a tabela e a quantidade de multas sempre que a janela for exibida."""
        self.load_multas()
        self.load_quantidade()
        super().showEvent(event)

    def load_multas(self):
        """Carrega os dados da tabela multa e exibe no QTableWidget."""
        if not self.tabela:
            print("[ERRO] tabela não está inicializada.")
            return

        try:
            # Consulta ao banco de dados para obter os dados da tabela multa
            query = "SELECT * FROM multa"
            results = self.db_manager.fetch_query(query)

            if not results:
                print("[INFO] Nenhum dado encontrado na tabela multa.")
                self.tabela.setRowCount(0)
                return

            # Configurar o número de linhas e colunas no QTableWidget
            self.tabela.setRowCount(len(results))
            self.tabela.setColumnCount(len(results[0]))
            self.tabela.setHorizontalHeaderLabels(results[0].keys())  # Define os cabeçalhos das colunas

            # Preencher o QTableWidget com os dados
            for row_idx, row_data in enumerate(results):
                for col_idx, col_data in enumerate(row_data.values()):
                    self.tabela.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))

        except Exception as e:
            print(f"[ERRO] Não foi possível carregar os dados da tabela multa: {e}")

    def load_quantidade(self):
        """Carrega a quantidade de pessoas com multas não pagas e exibe no QLabel."""
        if not self.quantidadeInput:
            print("[ERRO] quantidadeInput não está inicializado.")
            return

        try:
            # Consulta ao banco de dados para contar a quantidade de pessoas com pago = 0
            query = "SELECT COUNT(*) AS quantidade FROM multa WHERE pago = 0"
            result = self.db_manager.fetch_query(query)

            if result and result[0]["quantidade"] is not None:
                quantidade = result[0]["quantidade"]  # Obtém o valor da contagem
                self.quantidadeInput.setText(str(quantidade))  # Exibe no QLabel
            else:
                self.quantidadeInput.setText("0")  # Exibe 0 se não houver registros com pago = 0

        except Exception as e:
            print(f"[ERRO] Não foi possível carregar a quantidade de pessoas com multas não pagas: {e}")

    def go_to_menu(self):
        """Volta para a tela do menu."""
        self.stacked_widget.setCurrentWidget(self.stacked_widget.menu_window)