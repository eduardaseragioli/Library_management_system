from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem
from PyQt5.uic import loadUi
import os

class DadosWindow(QMainWindow):
    def __init__(self, stacked_widget, db_manager):
        super(DadosWindow, self).__init__()
        self.stacked_widget = stacked_widget  # Referência ao QStackedWidget principal
        self.db_manager = db_manager  # Referência ao gerenciador de banco de dados

        # Carregar o arquivo dados.ui da pasta show
        ui_path = os.path.join(os.path.dirname(__file__), "dados.ui")
        loadUi(ui_path, self)

        # Preencher o QTableWidget com os dados da tabela funcionario
        self.load_funcionario_data()

    def load_funcionario_data(self):
        """Carrega os dados da tabela funcionario no QTableWidget."""
        query = "SELECT * FROM funcionario"  # Substitua pelo nome correto da tabela
        try:
            results = self.db_manager.fetch_query(query)  # Executa a consulta no banco de dados
            if results:
                self.tabela.setRowCount(len(results))  # Define o número de linhas no QTableWidget
                self.tabela.setColumnCount(len(results[0]))  # Define o número de colunas no QTableWidget
                self.tabela.setHorizontalHeaderLabels(results[0].keys())  # Define os cabeçalhos das colunas

                for row_idx, row_data in enumerate(results):
                    for col_idx, col_data in enumerate(row_data.values()):
                        self.tabela.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))
            else:
                self.tabela.setRowCount(0)  # Limpa o QTableWidget se não houver dados
        except Exception as e:
            print(f"[ERRO] Não foi possível carregar os dados: {e}")

    def go_to_menu(self):
        """Volta para a tela do menu."""
        self.stacked_widget.setCurrentWidget(self.stacked_widget.menu_window)