from PyQt5.QtWidgets import QMainWindow, QPushButton, QLineEdit, QMessageBox, QRadioButton, QComboBox#importar as classes necessárias do PyQt5
from PyQt5.uic import loadUi#Importa a função para carregar arquivos .ui
import os

class MultaCadastroWindow(QMainWindow):# Define a classe MultaCadastroWindow, que herda de QMainWindow
    def __init__(self, stacked_widget, db_manager):# método construtor
        super(MultaCadastroWindow, self).__init__()
        self.stacked_widget = stacked_widget # Referência ao QStackedWidget principal
        self.db_manager = db_manager# iteração do banco de dados
    
        # Carregar o arquivo multaCadastro.ui da pasta registro
        ui_path = os.path.join(os.path.dirname(__file__), "multaCadastro.ui")
        loadUi(ui_path, self)

        # Conectar o botão menuButton ao método para voltar ao menu
        self.menuButton: QPushButton = self.findChild(QPushButton, "menuButton")
        if self.menuButton:
            self.menuButton.clicked.connect(self.go_to_menu)
        else:
            print("[ERRO] menuButton não encontrado no arquivo multaCadastro.ui")

        # Conectar o botão salvarButton ao método de salvar
        self.salvarButton: QPushButton = self.findChild(QPushButton, "salvarButton")
        if self.salvarButton:
            self.salvarButton.clicked.connect(self.salvar_multa)
        else:
            print("[ERRO] salvarButton não encontrado no arquivo multaCadastro.ui")
        # Conecta o botão "Salvar Multa" ao método 'salvar_multa', com verificação.

        # Inputs
        self.valorInput: QLineEdit = self.findChild(QLineEdit, "valorInput")
        self.descricaoInput: QLineEdit = self.findChild(QLineEdit, "descricaoInput")
        self.verdadeiroButton: QRadioButton = self.findChild(QRadioButton, "verdadeiroButton")
        self.falsoButton: QRadioButton = self.findChild(QRadioButton, "falsoButton")
        self.emprestimoBox: QComboBox = self.findChild(QComboBox, "emprestimoBox")

        # Carrega os empréstimos no ComboBox ao abrir a janela
        self.carregar_emprestimos()
        # Garante que o ComboBox de empréstimos esteja preenchido.


    def carregar_emprestimos(self):
    # Define o método para popular o ComboBox de empréstimos.

        """Carrega os empréstimos do banco de dados no ComboBox emprestimoBox."""
        if not self.emprestimoBox:
            print("[ERRO] emprestimoBox não encontrado no arquivo multaCadastro.ui")
            return
        self.emprestimoBox.clear()
        try:
            # Seleciona o ID de todos os empréstimos
            query = "SELECT idEmprestimo FROM emprestimo"
            emprestimos = self.db_manager.fetch_query(query)
            if emprestimos:
                for emp in emprestimos:
                    self.emprestimoBox.addItem(str(emp["idEmprestimo"]), emp["idEmprestimo"])
                    # Adiciona o ID do empréstimo.
            else:
                self.emprestimoBox.addItem("Nenhum empréstimo cadastrado", None)
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao carregar empréstimos: {e}")

    def go_to_menu(self):
    # Define o método para retornar ao menu principal.
        """Volta para a tela do menu."""
        self.stacked_widget.setCurrentWidget(self.stacked_widget.menu_window)

    def salvar_multa(self):
        # Define o método 'salvar_multa'
        """Salva a multa no banco de dados."""
        valor_texto = self.valorInput.text().strip() if self.valorInput else ""
        descricao = self.descricaoInput.text().strip() if self.descricaoInput else ""
        id_emprestimo = self.emprestimoBox.currentData() if self.emprestimoBox else None

        # Tenta converter o valor da multa para um número decimal (float).
        try:
            valor = float(valor_texto)
        except ValueError:
            QMessageBox.warning(self, "Atenção", "Valor deve ser um número!")
            return

        # Determina o status de pagamento da multa com base nos botões de rádio.
        if self.verdadeiroButton and self.verdadeiroButton.isChecked():
            pago = True
        elif self.falsoButton and self.falsoButton.isChecked():
            pago = False
        else:
            pago = None

        # Validação: Verifica se todos os campos obrigatórios estão preenchidos.
        if not valor_texto or not descricao or pago is None or not id_emprestimo:
            QMessageBox.warning(self, "Atenção", "Preencha todos os campos!")
            return

        try:
        # Prepara a consulta SQL para inserir a nova multa na tabela 'multa'.

            query = """
                INSERT INTO multa (valor, descricao, pago, idEmprestimo)
                VALUES (%s, %s, %s, %s)
            """
            #passando os valores como parâmetros
            self.db_manager.execute_query(query, (valor, descricao, pago, id_emprestimo))
            QMessageBox.information(self, "Sucesso", "Multa cadastrada com sucesso!")
            self.valorInput.clear()
            self.descricaoInput.clear()
             # Reseta o ComboBox para o primeiro item.
            self.emprestimoBox.setCurrentIndex(0)
            if self.verdadeiroButton:
                self.verdadeiroButton.setChecked(False)
            if self.falsoButton:
                self.falsoButton.setChecked(False)
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao salvar multa: {e}")