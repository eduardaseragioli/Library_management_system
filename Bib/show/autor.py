from PyQt5.QtWidgets import QMainWindow, QLabel, QTableWidget, QTableWidgetItem, QPushButton
from PyQt5.uic import loadUi
import os

class AutorWindow(QMainWindow):
    def __init__(self, stacked_widget, db_manager):
        super(AutorWindow, self).__init__()
        self.stacked_widget = stacked_widget  # Referência ao QStackedWidget principal
        self.db_manager = db_manager  # Referência ao gerenciador de banco de dados

        # Carregar o arquivo autor.ui da pasta show
        ui_path = os.path.join(os.path.dirname(__file__), "autor.ui")
        loadUi(ui_path, self)

        # Conectar o botão menuButton ao método para voltar ao menu
        self.menuButton: QPushButton = self.findChild(QPushButton, "menuButton")
        if self.menuButton:
            self.menuButton.clicked.connect(self.go_to_menu)
        else:
            print("[ERRO] menuButton não encontrado no arquivo autor.ui")

        # Referência ao QTableWidget para exibir os dados da tabela AUTOR
        self.tabela: QTableWidget = self.findChild(QTableWidget, "tabela")
        if not self.tabela:
            print("[ERRO] tabela não encontrada no arquivo autor.ui")

        # Referência ao QLabel para exibir a quantidade de autores
        self.quantidadeInput: QLabel = self.findChild(QLabel, "quantidadeInput")
        if not self.quantidadeInput:
            print("[ERRO] quantidadeInput não encontrado no arquivo autor.ui")

        # Carregar os dados da tabela AUTOR e a quantidade de autores
        self.load_autores()
        self.load_quantidade()

    def showEvent(self, event):
        """Atualiza a tabela e a quantidade de autores sempre que a janela for exibida."""
        self.load_autores()
        self.load_quantidade()
        super().showEvent(event)

    def load_autores(self):
        """Carrega os dados da tabela AUTOR e exibe no QTableWidget."""
        if not self.tabela:
            print("[ERRO] tabela não está inicializada.")
            return

        try:
            # Consulta ao banco de dados para obter os dados da tabela AUTOR
            query = "SELECT * FROM AUTOR"
            results = self.db_manager.fetch_query(query)

            if not results:
                print("[INFO] Nenhum dado encontrado na tabela AUTOR.")
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
            print(f"[ERRO] Não foi possível carregar os dados da tabela AUTOR: {e}")

    def load_quantidade(self):
        """Carrega a quantidade de autores e exibe no QLabel."""
        if not self.quantidadeInput:
            print("[ERRO] quantidadeInput não está inicializado.")
            return

        try:
            # Consulta ao banco de dados para contar o número de autores
            query = "SELECT COUNT(*) AS quantidade FROM AUTOR"
            result = self.db_manager.fetch_query(query)

            if result:
                quantidade = result[0]["quantidade"]  # Obtém o valor da contagem
                self.quantidadeInput.setText(str(quantidade))  # Exibe no QLabel
            else:
                self.quantidadeInput.setText("0")  # Exibe 0 se não houver autores

        except Exception as e:
            print(f"[ERRO] Não foi possível carregar a quantidade de autores: {e}")

    def go_to_menu(self):
        """Volta para a tela do menu."""
        self.stacked_widget.setCurrentWidget(self.stacked_widget.menu_window)