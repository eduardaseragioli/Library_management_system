from PyQt5.QtWidgets import QMainWindow, QPushButton, QLineEdit, QMessageBox, QDateEdit, QRadioButton, QComboBox
from PyQt5.uic import loadUi
import os

class EmprestimoCadastroWindow(QMainWindow):# Define a classe 'EmprestimoCadastroWindow', herdando de QMainWindow.

    def __init__(self, stacked_widget, db_manager):# método construtor
        super(EmprestimoCadastroWindow, self).__init__()
        self.stacked_widget = stacked_widget
        self.db_manager = db_manager

        # Carregar o arquivo emprestimoCadastro.ui da pasta registro
        ui_path = os.path.join(os.path.dirname(__file__), "emprestimoCadastro.ui")
        loadUi(ui_path, self)

        # Conectar o botão menuButton ao método para voltar ao menu
        self.menuButton: QPushButton = self.findChild(QPushButton, "menuButton")
        if self.menuButton:
            self.menuButton.clicked.connect(self.go_to_menu)
        else:
            print("[ERRO] menuButton não encontrado no arquivo emprestimoCadastro.ui")

        # Conectar o botão salvarButton ao método de salvar
        self.salvarButton: QPushButton = self.findChild(QPushButton, "salvarButton")
        if self.salvarButton:
            self.salvarButton.clicked.connect(self.salvar_emprestimo)
        else:
            print("[ERRO] salvarButton não encontrado no arquivo emprestimoCadastro.ui")
        # Conecta o botão "Salvar Empréstimo" ao método 'salvar_emprestimo'

        # Inputs
        self.dateEdit: QDateEdit = self.findChild(QDateEdit, "dateEdit")
        self.duracaoInput: QLineEdit = self.findChild(QLineEdit, "duracaoInput")
        self.verdadeiroButton: QRadioButton = self.findChild(QRadioButton, "verdadeiroButton")
        self.falsoButton: QRadioButton = self.findChild(QRadioButton, "falsoButton")
        self.funcionarioBox: QComboBox = self.findChild(QComboBox, "funcionarioBox")
        self.leitorBox: QComboBox = self.findChild(QComboBox, "leitorBox")
        self.itemBox: QComboBox = self.findChild(QComboBox, "itemBox")

        # Carrega os funcionários, leitores e itens no ComboBox ao abrir a janela
        self.carregar_funcionarios()
        self.carregar_leitores()
        self.carregar_itens()

    def carregar_funcionarios(self):
    # Define o método para popular o ComboBox de funcionários.
        """Carrega os funcionários do banco de dados no ComboBox funcionarioBox."""
        if not self.funcionarioBox:
            print("[ERRO] funcionarioBox não encontrado no arquivo emprestimoCadastro.ui")
            return
        self.funcionarioBox.clear()
        try:
            query = "SELECT idFuncionario, nome FROM funcionario"
            funcionarios = self.db_manager.fetch_query(query)
            if funcionarios:
                for funcionario in funcionarios:
                    self.funcionarioBox.addItem(funcionario["nome"], funcionario["idFuncionario"])
                     # Adiciona o nome do funcionário e associa seu ID.

            else:
                self.funcionarioBox.addItem("Nenhum funcionário cadastrado", None)
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao carregar funcionários: {e}")

    def carregar_leitores(self):
    # Define o método para popular o ComboBox de leitores.

        """Carrega os leitores do banco de dados no ComboBox leitorBox."""
        if not self.leitorBox:
            print("[ERRO] leitorBox não encontrado no arquivo emprestimoCadastro.ui")
            return
        self.leitorBox.clear()
        try:
            query = "SELECT idLeitor, nome FROM leitor"
            leitores = self.db_manager.fetch_query(query)
            if leitores:
                for leitor in leitores:
                    self.leitorBox.addItem(leitor["nome"], leitor["idLeitor"])
                    # Adiciona o nome do leitor e associa seu ID.
            else:
                self.leitorBox.addItem("Nenhum leitor cadastrado", None)
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao carregar leitores: {e}")

    def carregar_itens(self):
    # Define o método para popular o ComboBox de itens.

        """Carrega os itens do banco de dados no ComboBox itemBox."""
        if not self.itemBox:
            print("[ERRO] itemBox não encontrado no arquivo emprestimoCadastro.ui")
            return
        self.itemBox.clear()
        try:
            query = "SELECT idItem, titulo FROM item"
            itens = self.db_manager.fetch_query(query)
            if itens:
                for item in itens:
                    self.itemBox.addItem(item["titulo"], item["idItem"])
                    # Adiciona o título do item e associa seu ID.

            else:
                self.itemBox.addItem("Nenhum item cadastrado", None)
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao carregar itens: {e}")

    def go_to_menu(self):# Define o método 'go_to_menu'
        """Volta para a tela do menu."""
        self.stacked_widget.setCurrentWidget(self.stacked_widget.menu_window)

    def salvar_emprestimo(self):# Define o método 'salvar_emprestimo'
        """Salva o empréstimo no banco de dados."""
        data_emprestimo = self.dateEdit.date().toString("yyyy-MM-dd") if self.dateEdit else ""
        duracao_dias_texto = self.duracaoInput.text().strip() if self.duracaoInput else ""

        # Tenta converter para inteiro e valida
        try:
            duracao_dias = int(duracao_dias_texto)
        except ValueError:
            QMessageBox.warning(self, "Atenção", "Duração deve ser um número inteiro!")
            return

        # Determina o status de devolução com base nos botões de rádio.
        if self.verdadeiroButton and self.verdadeiroButton.isChecked():
            devolvido = True
        elif self.falsoButton and self.falsoButton.isChecked():
            devolvido = False
        else:
            devolvido = None

        # Obtém os IDs dos itens selecionados nos ComboBoxes.
        id_funcionario = self.funcionarioBox.currentData() if self.funcionarioBox else None
        id_leitor = self.leitorBox.currentData() if self.leitorBox else None
        id_item = self.itemBox.currentData() if self.itemBox else None

        # Validação: Verifica se todos os campos obrigatórios estão preenchidos.
        if not data_emprestimo or devolvido is None or not id_funcionario or not id_leitor or not id_item:
            QMessageBox.warning(self, "Atenção", "Preencha todos os campos!")
            return

        try:
            query = """
                INSERT INTO emprestimo (data_emprestimo, duracao_dias, devolvido, idFuncionario, idLeitor, idItem)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            
            #passa os valores como parâmetros 
            self.db_manager.execute_query(query, (data_emprestimo, duracao_dias, devolvido, id_funcionario, id_leitor, id_item))
            QMessageBox.information(self, "Sucesso", "Empréstimo cadastrado com sucesso!")
            self.dateEdit.setDate(self.dateEdit.minimumDate())
            self.duracaoInput.clear()
            if self.verdadeiroButton:
                self.verdadeiroButton.setChecked(False)
            if self.falsoButton:
                self.falsoButton.setChecked(False)
            if self.funcionarioBox:
                self.funcionarioBox.setCurrentIndex(0)
            if self.leitorBox:
                self.leitorBox.setCurrentIndex(0)
            if self.itemBox:
                self.itemBox.setCurrentIndex(0)
        except Exception as e:
            QMessageBox.critical(self, "Erro", f"Erro ao salvar empréstimo: {e}")