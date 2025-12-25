from PyQt5.QtWidgets import QMainWindow, QLabel, QPushButton
from PyQt5.uic import loadUi
import os

class EstatisticaWindow(QMainWindow):
    def __init__(self, stacked_widget, db_manager):
        super(EstatisticaWindow, self).__init__()
        self.stacked_widget = stacked_widget  # Referência ao QStackedWidget principal
        self.db_manager = db_manager  # Referência ao gerenciador de banco de dados

        # Carregar o arquivo estatistica.ui da pasta show
        ui_path = os.path.join(os.path.dirname(__file__), "estatistica.ui")
        loadUi(ui_path, self)

        # Conectar o botão menuButton ao método para voltar ao menu
        self.menuButton: QPushButton = self.findChild(QPushButton, "menuButton")
        if self.menuButton:
            self.menuButton.clicked.connect(self.go_to_menu)
        else:
            print("[ERRO] menuButton não encontrado no arquivo estatistica.ui")

        # Referências aos widgets para exibir os resultados
        self.maximaMultaInput: QLabel = self.findChild(QLabel, "maximaMultaInput")
        if not self.maximaMultaInput:
            print("[ERRO] maximaMultaInput não encontrado no arquivo estatistica.ui")

        self.minimoMultaInput: QLabel = self.findChild(QLabel, "minimoMultaInput")
        if not self.minimoMultaInput:
            print("[ERRO] minimoMultaInput não encontrado no arquivo estatistica.ui")

        self.modaTituloInput: QLabel = self.findChild(QLabel, "modaTituloInput")
        if not self.modaTituloInput:
            print("[ERRO] modaTituloInput não encontrado no arquivo estatistica.ui")

        self.modaDuracaoInput: QLabel = self.findChild(QLabel, "modaDuracaoInput")
        if not self.modaDuracaoInput:
            print("[ERRO] modaDuracaoInput não encontrado no arquivo estatistica.ui")

        self.mediaEmprestimoInput: QLabel = self.findChild(QLabel, "mediaEmprestimoInput")
        if not self.mediaEmprestimoInput:
            print("[ERRO] mediaEmprestimoInput não encontrado no arquivo estatistica.ui")

        # Carregar as estatísticas
        self.load_estatisticas()

    def load_estatisticas(self):
        """Carrega as estatísticas e exibe nos widgets."""
        try:
            # Máximo das multas aplicadas
            if self.maximaMultaInput:
                query = "SELECT MAX(valor) AS max_multa FROM Multa"
                result = self.db_manager.fetch_query(query)
                if result and result[0]["max_multa"] is not None:
                    self.maximaMultaInput.setText(f"{result[0]['max_multa']:.2f}")
                else:
                    self.maximaMultaInput.setText("N/A")

            # Mínimo das multas aplicadas
            if self.minimoMultaInput:
                query = "SELECT MIN(valor) AS min_multa FROM Multa"
                result = self.db_manager.fetch_query(query)
                if result and result[0]["min_multa"] is not None:
                    self.minimoMultaInput.setText(f"{result[0]['min_multa']:.2f}")
                else:
                    self.minimoMultaInput.setText("N/A")

            # Título do livro mais requisitado (moda)
            if self.modaTituloInput:
                query = """
                    SELECT i.titulo, COUNT(*) AS num_emprestimos
                    FROM Emprestimo e
                    JOIN Item i ON e.idItem = i.idItem
                    GROUP BY i.titulo
                    ORDER BY num_emprestimos DESC
                    LIMIT 1
                """
                result = self.db_manager.fetch_query(query)
                if result and result[0]["titulo"] is not None:
                    self.modaTituloInput.setText(f"{result[0]['titulo']} ({result[0]['num_emprestimos']} empréstimos)")
                else:
                    self.modaTituloInput.setText("N/A")

            # Moda da duração dos empréstimos
            if self.modaDuracaoInput:
                query = """
                    SELECT duracao_dias, COUNT(*) AS vezes
                    FROM Emprestimo
                    GROUP BY duracao_dias
                    ORDER BY vezes DESC
                    LIMIT 1
                """
                result = self.db_manager.fetch_query(query)
                if result and result[0]["duracao_dias"] is not None:
                    self.modaDuracaoInput.setText(f"{result[0]['duracao_dias']} dias ({result[0]['vezes']} vezes)")
                else:
                    self.modaDuracaoInput.setText("N/A")

            # Média de empréstimos por funcionário
            if self.mediaEmprestimoInput:
                query = """
                    SELECT COUNT(*) / COUNT(DISTINCT idFuncionario) AS media
                    FROM Emprestimo
                """
                result = self.db_manager.fetch_query(query)
                if result and result[0]["media"] is not None:
                    self.mediaEmprestimoInput.setText(f"{result[0]['media']:.2f}")
                else:
                    self.mediaEmprestimoInput.setText("N/A")

        except Exception as e:
            print(f"[ERRO] Não foi possível carregar as estatísticas: {e}")

    def go_to_menu(self):
        """Volta para a tela do menu."""
        self.stacked_widget.setCurrentWidget(self.stacked_widget.menu_window)